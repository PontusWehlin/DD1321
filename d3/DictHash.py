class DictHash:
    def __init__(self):
        self.__dict = {}

    def store(self,nyckel,data):
        self.__dict[nyckel] = data

    def search(self,nyckel):
        return self.__dict[nyckel]

    def keys(self):
        return list(self.__dict.keys())

    def __getitem__(self, nyckel):
        return self.search(nyckel)

    def __contains__(self, nyckel):
        return nyckel in self.__dict
