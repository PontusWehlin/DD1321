import timeit


class Song:
    def __init__(self, songname, artist, trackid, songid):
        self.songname = songname
        self.artist = artist
        self.trackid = trackid
        self.songid = songid

    def __lt__(self, other):
        return self.artist < other.artist

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


##### Taget från föreläsnings anteckningar
def quicksort(data):
    sista = len(data) - 1
    qsort(data, 0, sista)

def qsort(data, low, high):
    pivotindex = (low + high) // 2
    # flytta pivot till kanten
    data[pivotindex], data[high] = data[high], data[pivotindex]

    # damerna först med avseende på pivotdata
    pivotmid = partitionera(data, low - 1, high, data[high])

    # flytta tillbaka pivot
    data[pivotmid], data[high] = data[high], data[pivotmid]

    if pivotmid - low > 1:
        qsort(data, low, pivotmid - 1)
    if high - pivotmid > 1:
        qsort(data, pivotmid + 1, high)

def partitionera(data, v, h, pivot):
    while True:
        v = v + 1
        while data[v] < pivot:
            v = v + 1
        h = h - 1
        while h != 0 and data[h] > pivot:
            h = h - 1
        data[v], data[h] = data[h], data[v]
        if v >= h:
            break
    data[v], data[h] = data[h], data[v]
    return v


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

    sort_list = quicksort(lista)
    linjsorttid = timeit.timeit(stmt=lambda: linsearch(sort_list, testartist), number=100)
    print('Linjärsökning för sorterad lista tog', round(linjsorttid, 4), 'sekunder')


if __name__ == '__main__':
    main()