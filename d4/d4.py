import timeit, sys
sys.setrecursionlimit(100000)


class Song:
    def __init__(self, songname, artist, trackid, songid):
        self.songname = songname
        self.artist = artist
        self.trackid = trackid
        self.songid = songid

    def __str__(self):
        return(self.songname + ' - ' + self.artist)

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


# ##### Taget från föreläsnings anteckningar
# def quicksort(data):
#     sista = len(data) - 1
#     qsort(data, 0, sista)
#
# def qsort(data, low, high):
#     pivotindex = (low + high) // 2
#     # flytta pivot till kanten
#     data[pivotindex], data[high] = data[high], data[pivotindex]
#
#     # damerna först med avseende på pivotdata
#     pivotmid = partitionera(data, low - 1, high, data[high])
#
#     # flytta tillbaka pivot
#     data[pivotmid], data[high] = data[high], data[pivotmid]
#
#     if pivotmid - low > 1:
#         qsort(data, low, pivotmid - 1)
#     if high - pivotmid > 1:
#         qsort(data, pivotmid + 1, high)
#
# def partitionera(data, v, h, pivot):
#     while True:
#         v = v + 1
#         while data[v].artist < pivot.artist:
#             v = v + 1
#         h = h - 1
#         while h != 0 and data[h].artist > pivot.artist:
#             h = h - 1
#         data[v], data[h] = data[h], data[v]
#         if v >= h:
#             break
#     data[v], data[h] = data[h], data[v]
#     return v
def quickSort(arr, low, high):
    high = len(arr)-1
    low = 0
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] < pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


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

    sort_list = quickSort(lista, 0, len(lista)-1)
    print(type(sort_list))
    linjsorttid = timeit.timeit(stmt=lambda: linsearch(sort_list, testartist), number=100)
    print('Linjärsökning för sorterad lista tog', round(linjsorttid, 4), 'sekunder')


if __name__ == '__main__':
    main()