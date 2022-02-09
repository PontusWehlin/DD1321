import DictHash

def import_tracks(filename, hashdict):
    file = open(filename,"r",encoding="UTF-8")
    file_lines = file.readlines()
    for line in file_lines:
        line_parts = line.split("<SEP>")
        hashdict.store(line_parts[-1].rstrip("\n"), line_parts[-2])
    return hashdict

def Test(hashdict):
    print("Should be True: ", 'Goodbye' in hashdict)
    print("Should be Waldemar Bastos: ", hashdict["N Gana"])
    print("Should be Martin Sexton: ", hashdict.search("In The Journey"))

def main():
    hashdict = DictHash.DictHash()
    hashdict = import_tracks("unique_tracks.txt", hashdict)
    Test(hashdict)





if __name__ == "__main__":
    main()