#Global variabel
List_length = 100000000

class HashNode:
    def __init__(self):
        self.hash = 1

    def __hash__(self, key):
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
        pass

    def __contains__(self, key):
        pass

    def store(self,key,data):
        nod = HashNode()
        nod.store(key,data)
        if (self.dict[nod.hash] == None) or (self.dict[nod.hash].key == nod.key):
            self.dict[nod.hash] = nod
        else:
            probing = True
            index = nod.hash
            timeout = 0
            while probing:
                index *= 2
                if index > List_length:
                    index = (index % List_length)+1
                if timeout == 10000:
                    probing = False
                    print('Error')
                    print(index)

                if (self.dict[index] == None) or (self.dict[index].key == nod.key):
                    self.dict[index] = nod

                timeout += 2


    def keys(self):
        keys=[]
        for nod in self.dict:
            if nod != None:
                keys.append(nod.key)
        return keys

def import_tracks(filename, hashdict):
    file = open(filename,"r",encoding="UTF-8")
    file_lines = file.readlines()
    for line in file_lines[:200]:
        line_parts = line.split("<SEP>")
        hashdict.store(line_parts[-2], line_parts[-1].rstrip("\n"))
    return hashdict


def main():
    hashdict = Hashtabell()
    hashdict = import_tracks("unique_tracks.txt", hashdict)
    print(len(hashdict.keys()))
    print(hashdict.keys()[:50])



if __name__ == "__main__":
    main()