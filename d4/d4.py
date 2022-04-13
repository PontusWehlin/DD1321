import timeit, random, Quicksort, Quicksort_length, sys
import Quicksort_recursiv as Qr
import Quicksort_recursiv_length as Qr_l
import Mergesort as Ms
import Mergesort_length as Ms_l
import matplotlib.pyplot as plt

sys.setrecursionlimit(10**6)


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
    raw_file.close()
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
    #Quicksort.quickSortIterative(list, 0, len(list)-1)
    #Qr.quicksort(list)
    Ms.mergeSort(list)
    return list

def quicksort_length(list):
    #Quicksort_length.quickSortIterative(list, 0, len(list)-1)
    #Qr_l.quicksort(list)
    Ms.mergeSort(list)
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

def method_1(list, k):
    for i in range(k - 1):
        list.pop(linesearch_length(list))
    index = linesearch_length(list)

def method_2(list, k):
    sort_length = quicksort_length(list)

def timing():
    filename = "unique_tracks.txt"

    lista, dictionary = readfile(filename, 10**6)
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
    print("Mergesort tog", round(sorttid, 4), "sekunder")

    time = timeit.timeit(stmt=lambda: linsearch_artist(lista, lista[random.randint(0, len(lista) - 1)].artist), number=1000)
    print('Linjärsökning i den osorterade listan för 1000 slumpade element tog i genomsnitt', round(time/1000, 4),
          'sekunder')

    bintid = timeit.timeit(stmt=lambda: binarysearch(sort_list, sort_list[-10]), number=100)
    print('Binärsökning tog', round(bintid, 4), 'sekunder')

    dicttid = timeit.timeit(stmt=lambda: dictionary[testartist], number=100)
    print('Uppslagning i pythons dictionary tog', round(dicttid, 4), 'sekunder')

def main():
    filename = "unique_tracks.txt"
    file_del2 = "sang-artist-data.txt"

    list, dictionary = readfile(filename, 10**6)
    antal_element = len(list)

    sortlist = quicksort(list)
    list = addsonglength(file_del2, sortlist)
    print("Antal element =", antal_element)

    sort_length = quicksort_length(list.copy())
    print('Sorterad')
    quicksorttime = timeit.timeit(stmt=lambda: quicksort_length(list.copy()), number = 10)
    print('Tid tagen för sortering:', round(quicksorttime/10,4), 'sekunder')
    k = 3
    k_values = []
    lin_time = []
    quick_time = []
    while k <= 30:
        print('--')
        k_values.append(k)
        #Metod 1 - linjärsök och plocka bort den längsta
        method1time = timeit.timeit(stmt=lambda: method_1(list.copy(), k), number = 10)
        print('Med ett k på',k,'tog metod 1',round((method1time/10),4),'sekunder')
        lin_time.append(round(method1time/10,4))

        #Metod 2 - Sortera och plocka ut den k längsta låten
        method2time = timeit.timeit(stmt=lambda: sort_length[k], number= 10)
        print('Med ett k på', k, 'tog metod 2', round((quicksorttime+method2time)/10, 4), 'sekunder')
        #method2time = timeit.timeit(stmt=lambda: quicksort_length(list.copy())[k], number= 10)
        #print('Med ett k på', k, 'tog metod 2', round(method2time, 4), 'sekunder')

        quick_time.append(round((quicksorttime+method2time)/10, 4))

        k += 3

    plt.plot(k_values, lin_time, label = 'Method 1')
    plt.plot(k_values, quick_time, label = 'Method 2')
    plt.xlabel('k value')
    plt.ylabel('time (s)')
    plt.legend()
    plt.title('Number of songs: ' + str(len(list.copy())))
    plt.show()

if __name__ == '__main__':
    print('Välj en av följande')
    print('1. Tidtagning')
    print('2. Annat')
    i = int(input('-> '))
    if i == 1:
        timing()
    elif i == 2:
        main()