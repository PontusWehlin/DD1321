import DictHash

def import_tracks(filename, hashdict):
    file = open(filename,"r",encoding="UTF-8")
    file_lines = file.read()
    for line in file_lines:
        line_parts = line.split("<SEP>")
        print(len(line_parts))
        hashdict.store(line_parts[-1], line_parts[-2])
    return hashdict


def main():
    hashdict = DictHash.DictHash()
    hashdict = import_tracks("unique_tracks.txt", hashdict)





if __name__ == "__main__":
    main()