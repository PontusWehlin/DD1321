import timeit


class Song:
    def __init__(self, songname, artist, trackid, songid):
        self.songname = songname
        self.artist = artist
        self.trackid = trackid
        self.songid = songid

    def __lt__(self, other):
        return self.artist < other

def readfile(filename):
    songlist = []
    songdir = {}
    raw_file = open(filename, 'r', encoding='UTF-8')
    for i in range(10000):
        line = raw_file.readline()
        lineparts = line.split('<SEP>')
        song = Song(lineparts[3].rstrip('\n'), lineparts[2], lineparts[0], lineparts[1])
        songlist.append(song)
        songdir[lineparts[2]] = song
    return(songlist, songdir)

def linsearch(list, testartist):
    for i in range(len(list)):
        if testartist == list[i].artist:
            return list[i]


def main():
    filename = "unique_tracks.txt"
    # file_del2 = "sang-artist-data.txt"

    lista, dictionary = readfile(filename)
    antal_element = len(lista)
    print("Antal element =", antal_element)

    sista = lista[len(lista) - 1]
    testartist = sista.artist

    linjtid = timeit.timeit(stmt=lambda: linsearch(lista, testartist), number=100)
    print("Linjärsökningen tog", round(linjtid, 4), "sekunder")


if __name__ == '__main__':
    main()