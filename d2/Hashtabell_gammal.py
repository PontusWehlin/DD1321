import Test_tracks
#Global variabel
List_length = 100000000

class HashNode:
    def __init__(self):
        self.hash = 1

    def __hash__(self, key):
        for i in range(len(key)):
            self.hash *= ord(key[i]) * (i+1)
            if self.hash > List_length:
                self.hash = self.hash%List_length
        self.hash = (self.hash//2)*2
        if self.hash == 0:
            self.hash = 2

    def store(self,key,data):
        self.data = data
        self.key = key
        self.__hash__(key)


class Hashtabell:
    def __init__(self):
        self.dict = [0]*List_length

    def __getitem__(self, key):
        if (key in self.dict) and (self.dict.index(key) == (self.dict.index(key)//2)*2):
            return self.dict[self.dict.index(key)+1]
        else:
            raise KeyError(key + ' not a valid key')

    def __contains__(self, key):
        return key in self.dict

    def store(self,key,data):
        nod = HashNode()
        nod.store(key,data)
        if self.dict[nod.hash] == 0 or (self.dict[nod.hash] == key):
            self.dict[nod.hash] = key
            self.dict[nod.hash+1] = data
        else:
            probing = True
            adjusted = 0
            timeout = 0
            while probing:
                timeout += 1
                if timeout == 10000:
                    if adjusted == 2:
                        print('ERROR')
                        print(nod.hash)
                        break
                    adjusted +=1
                    timeout = 0
                    nod.hash *=2
                nod.hash += 2
                if nod.hash > List_length:
                    nod.hash = nod.hash%List_length
                    nod.hash = (nod.hash//2)*2
                if self.dict[nod.hash] == 0:
                    self.dict[nod.hash] = key
                    self.dict[nod.hash + 1] = data
                    probing = False
    def keys(self):
        keys = []
        for i in range(len(self.dict)//2):
            if self.dict[i*2] != 0:
                keys.append(self.dict[i*2])
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
    print(len(hashdict.keys()))




if __name__ == "__main__":
    main()