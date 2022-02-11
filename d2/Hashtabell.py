#Global variabel
List_length = 10000000

class HashNode:
    def __init__(self):
        self.hash = 1
        self.index = 1

    def __hash__(self, key): # Hashningsfunktion som summerar Ascii värdet av varje bokstav samt väger bokstavsordningen
        weight = 1
        for i in range(len(key)):
            self.hash += ord(key[i]) * weight
            weight *= 10
            if self.hash > List_length:
                self.hash = (self.hash % List_length) + 1

    def store(self,key,data):
        self.data = data
        self.key = key
        self.__hash__(key)


class Hashtabell:
    def __init__(self):
        self.dict = [None] * List_length

    def __getitem__(self, key):
        index = self.__index()
        for i in index:
            if self.dict[i].key == key:
                return self.dict[i].data
        raise KeyError('Key not found!')

    def __contains__(self, key):
        keys = self.keys()
        return key in keys

    def __index(self):
        index = []
        for nod in self.dict:
            if nod != None:
                index.append(nod.index)
        return index

    def store(self,key,data):
        nod = HashNode()
        nod.store(key,data)
        if (self.dict[nod.hash] == None) or (self.dict[nod.hash].key == nod.key):
            self.dict[nod.hash] = nod
            nod.index = nod.hash
        else:
            # Här börjar probningen vid krock där indexet i listan dubblas hela tiden
            probing = True
            index = nod.hash
            timeout = 0
            while probing:
                index *= 2
                if index > List_length:
                    index = (index % List_length)+1
                if timeout == 100: #Tillåter funktionen att försöka proba 100 gånger, förhindrar oändliga loopar
                    probing = False
                    print('Error')
                if (self.dict[index] == None) or (self.dict[index].key == nod.key):
                    self.dict[index] = nod
                    nod.index = index
                    probing = False
                timeout += 1

    def remove(self, key):
        if self.__contains__(key):
            index = self.__index()
            for i in index:
                if self.dict[i].key == key:
                    data = self.dict[i].data
                    self.dict[i] = None
        else:
            raise KeyError('Key not found!')
        return data

    def keys(self):
        keys=[]
        for nod in self.dict:
            if nod != None:
                keys.append(nod.key)
        return keys


def import_tracks(filename, hashdict):
    file = open(filename,"r",encoding="UTF-8")
    file_lines = file.readlines()
    for line in file_lines:
        line_parts = line.split("<SEP>")
        hashdict.store(line_parts[-2], line_parts[-1].rstrip("\n"))
    return hashdict


def main():
    hashdict = Hashtabell()
    hashdict = import_tracks("unique_tracks.txt", hashdict)
    print('Imported')
    print(len(hashdict.keys()))
    print("U2" in hashdict)
    print(hashdict['U2'])
    print(hashdict.remove('U2'))
    print('U2' in hashdict)






if __name__ == "__main__":
    main()