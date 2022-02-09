class HashNode:
    def __init__(self):
        self.hash = 0

    def __hash__(self, key):
        for i in range(len(key)):
            self.hash += ord(key[1])
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

    def store(self,key,data):
        nod = HashNode()
        nod.store(key,data)
        self.dict[nod.hash] = key
        self.dict[nod.hash+1] = data



def main():
    nod = HashNode()
    nod.store('Hej', 1)
    print(nod.hash)


if __name__ == "__main__":
    main()