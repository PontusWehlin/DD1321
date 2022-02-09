class DictHash:
    def __init__(self):
        self.__dict = {}

    def store(self,nyckel,data):
        self.__dict[nyckel] = data

    def search(self,nyckel):
        return self.__dict[nyckel]

    def keys(self):
        return self.__dict.keys()

    def __getitem__(self, nyckel):
        return self.search(nyckel)

    def __contains__(self, nyckel):
        return nyckel in self.__dict

def Test():
    hash = DictHash()
    hash.store('Ay-money','Mac')
    hash.store('PP','HP')
    hash.store('Ameer','MSI')

    print('______TEST_______')
    print(hash.search('PP'))
    print(hash['Ay-money'])
    print('Noak' in hash)

if __name__ == '__main__':
    Test()