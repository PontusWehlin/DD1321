class HashNode:
    def __init__(self):
        self.hash = 1

    def __hash__(self, key):
        for i in range(len(key)):
            self.hash *= ord(key[i]) * (i+1)
            if self.hash > 10000:
                self.hash = self.hash%10000
        self.hash = (self.hash//2)*2

    def store(self,key,data):
        self.data = data
        self.key = key
        self.__hash__(key)


class Hashtabell:
    def __init__(self):
        self.dict = [0]*10000

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
            timeout = 0
            while probing:
                timeout += 1
                if timeout == 100:
                    print('ERROR')
                    break
                nod.hash *= 2
                if nod.hash > 10000:
                    nod.hash = nod.hash%10000
                    nod.hash = (nod.hash//2)*2
                if self.dict[nod.hash] == 0:
                    self.dict[nod.hash] = key
                    self.dict[nod.hash + 1] = data
                    probing = False


def main():
    hashdict = Hashtabell()
    hashdict.store('Noak','pissmac')
    hashdict.store('PP','HP')
    print(hashdict['PP'])
    print(hashdict['Noak'])




if __name__ == "__main__":
    main()