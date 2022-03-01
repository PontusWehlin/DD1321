import timeit, random


class Song:
    def __init__(self, songname, artist, trackid, songid):
        self.songname = songname
        self.artist = artist
        self.trackid = trackid
        self.songid = songid
        self.length = None

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
        list[index].length = lineparts[3]
    return list

def linsearch(list, testartist):
    for i in range(len(list)):
        if testartist == list[i].artist:
            return list[i]

def quicksort(list):
    quickSortIterative(list, 0, len(list)-1)
    return list

##### TAGET FRÅN STACKOVERFLOW #######
# This function is same in both iterative and recursive
def partition(arr, l, h):
    i = (l - 1)
    x = arr[h]

    for j in range(l, h):
        if arr[j] < x:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
        elif arr[j] == x:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return (i + 1)

# Function to do Quick sort
# arr[] --> Array to be sorted,
# l  --> Starting index,
# h  --> Ending index
def quickSortIterative(arr, l, h):
    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * (size)

    # initialize top of stack
    top = -1

    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    # Keep popping from stack while is not empty
    while top >= 0:

        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        # Set pivot element at its correct position in
        # sorted array
        p = partition(arr, l, h)

        # If there are elements on left side of pivot,
        # then push left side to stack
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

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
    # file_del2 = "sang-artist-data.txt"

    lista, dictionary = readfile(filename, 1000)
    antal_element = len(lista)
    print("Antal element =", antal_element)

    sista = lista[len(lista) - 1]
    testartist = sista.artist

    linjtid = timeit.timeit(stmt=lambda: linsearch(lista, testartist), number=100)
    print("Linjärsökningen tog", round(linjtid, 4), "sekunder")

    sort_list = quicksort(lista)
    testartist = sort_list[-1].artist

    linjsorttid = timeit.timeit(stmt=lambda: linsearch(sort_list, testartist), number=100)
    print('Linjärsökning för sorterad lista tog', round(linjsorttid, 4), 'sekunder')

    sorttid = timeit.timeit(stmt=lambda: quicksort(lista), number=1)
    print("Quicksort tog", round(sorttid, 4), "sekunder")

    timevek = []
    for i in range(1000):
        time = timeit.timeit(stmt=lambda: linsearch(lista, lista[random.randint(0, len(lista) - 1)].artist), number=100)
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

    list, dictionary = readfile(filename, 1000000)
    antal_element = len(list)
    print("Antal element =", antal_element)

    sortlist = quicksort(list)
    list = addsonglength(file_del2, sortlist)
    for i in range(10):
        print(list[i].artist)
        print(list[i].songname)
        print(list[i].length)

if __name__ == '__main__':
    print('Choose one of the following')
    print('1. Timing of sorting')
    print('2. Other')
    i = int(input('-> '))
    if i == 1:
        timing()
    elif i == 2:
        main()