class HashNode:
    def __init__(self):
        self.hash = 0
    def __hash__(self, key):
        for i in range(len(key)):
            self.hash += ord(key[1])
    def store(self,key,data):
        self.data = data
        self.key = key
        self.__hash__(key)


def main():
    nod = HashNode()
    nod.store('Hej', 1)
    print(nod.hash)


if __name__ == "__main__":
    main()