import DictHash

def import_tracks(filename, hashdict):
    file = open(filename,"r",encoding="UTF-8")
    file_lines = file.readlines()
    for line in file_lines:
        line_parts = line.split("<SEP>")
        hashdict.store(line_parts[-2], line_parts[-1].rstrip("\n"))
    return hashdict

def Test(hashdict):
    print("Should be True: ", 'Kris Kross' in hashdict)
    print("Should be Muxima: ", hashdict["Waldemar Bastos"])
    print("Should be Auld Lang Syne: ", hashdict.search("Martin Sexton"))

def main():
    hashdict = DictHash.DictHash()
    hashdict = import_tracks("unique_tracks.txt", hashdict)
    Test(hashdict)





if __name__ == "__main__":
    main()