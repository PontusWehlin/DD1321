import timeit, random, Quicksort, Quicksort_length


class Song:
    def __init__(self, songname, artist, trackid, songid):
        self.songname = songname
        self.artist = artist
        self.trackid = trackid
        self.songid = songid
        self.length = 0

    def __str__(self):
        return(self.songname + ' - ' + self.artist)

    def __lt__(self, other):
        if isinstance(other, str): return self.artist < other
        return self.artist < other.artist

    def __gt__(self, other):
        if isinstance(other, str): return self.artist > other
        return self.artist > other.artist

def readfile(filename, amount):
    songlist = []
    songdir = {}
    raw_file = open(filename, 'r', encoding='UTF-8')
    for i in range(amount):
        line = raw_file.readline()
        lineparts = line.split('<SEP>')
        song = Song(lineparts[3].rstrip('\n'), lineparts[2], lineparts[0], lineparts[1])
        songlist.append(song)
        songdir[lineparts[2]] = song
    return(songlist, songdir)

def addsonglength(filename, list):
    raw_file = open(filename, 'r', encoding='UTF-8')
    for i in range(999988):
        line = raw_file.readline()
        lineparts = line.split('\t')
        index = binarysearch(list, lineparts[1])
        list[index].length = float(lineparts[3])
    return list

def linsearch_artist(list, testartist):
    for i in range(len(list)):
        if testartist == list[i].artist:
            return list[i]

# Hittar den längsta låten och retunerar dess index
def linesearch_length(list):
    max = list[0].length
    index = 0
    for i in range(len(list)):
        if list[i].length == None:
            pass
        elif max < list[i].length:
            max = list[i].length
            index = i
    return index

def quicksort(list):
    Quicksort.quickSortIterative(list, 0, len(list)-1)
    return list

def quicksort_length(list):
    Quicksort_length.quickSortIterative(list, 0, len(list)-1)
    return list

def binarysearch(list, search):
    low = 0
    high = len(list) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if list[mid] < search:
            low = mid + 1
        elif list[mid] > search:
            high = mid - 1
        else:
            return mid
    return -1

def timing():
    filename = "unique_tracks.txt"

    lista, dictionary = readfile(filename, 1000)
    antal_element = len(lista)
    print("Antal element =", antal_element)

    sista = lista[len(lista) - 1]
    testartist = sista.artist

    linjtid = timeit.timeit(stmt=lambda: linsearch_artist(lista, testartist), number=100)
    print("Linjärsökningen tog", round(linjtid, 4), "sekunder")

    sort_list = quicksort(lista)
    testartist = sort_list[-1].artist

    linjsorttid = timeit.timeit(stmt=lambda: linsearch_artist(sort_list, testartist), number=100)
    print('Linjärsökning för sorterad lista tog', round(linjsorttid, 4), 'sekunder')

    sorttid = timeit.timeit(stmt=lambda: quicksort(lista), number=1)
    print("Quicksort tog", round(sorttid, 4), "sekunder")

    timevek = []
    for i in range(1000):
        time = timeit.timeit(stmt=lambda: linsearch_artist(lista, lista[random.randint(0, len(lista) - 1)].artist), number=100)
        timevek.append(time)
    randomtime = sum(timevek) / len(timevek)
    print('Linjärsökning i den osorterade listan för 1000 slumpade element tog i genomsnitt', round(randomtime, 4),
          'sekunder')

    bintid = timeit.timeit(stmt=lambda: binarysearch(sort_list, sort_list[-10]), number=100)
    print('Binärsökning tog', round(bintid, 4), 'sekunder')

    dicttid = timeit.timeit(stmt=lambda: dictionary[testartist], number=100)
    print('Uppslagning i pythons dictionary tog', round(dicttid, 4), 'sekunder')

def main():
    filename = "unique_tracks.txt"
    file_del2 = "sang-artist-data.txt"

    list, dictionary = readfile(filename, 1000)
    antal_element = len(list)

    sortlist = quicksort(list)
    list = addsonglength(file_del2, sortlist)
    print("Antal element =", antal_element)

    k = 10
    #Metod 1 - linjärsök och plocka bort den längsta
    list_1 = list
    for i in range(k-1):
        list_1.pop(linesearch_length(list_1))
    index = linesearch_length(list_1)
    print('Den k:te längsta låten är',list_1[index].songname,'längden',list_1[index].length)

    #Metod 2 - Sortera och plocka ut den k längsta låten
    sort_length = quicksort_length(list)
    print('Den k:te längsta låten är', sort_length[k - 2],'längden', sort_length[k-2].length)
    print('Den k:te längsta låten är', sort_length[k - 1],'längden', sort_length[k-1].length)
    print('Den k:te längsta låten är', sort_length[k],'längden', sort_length[k].length)
    print('Den k:te längsta låten är', sort_length[k + 1],'längden', sort_length[k+1].length)


if __name__ == '__main__':
    print('Välj en av följande')
    print('1. Tidtagning')
    print('2. Annat')
    i = int(input('-> '))
    if i == 1:
        timing()
    elif i == 2:
        main()