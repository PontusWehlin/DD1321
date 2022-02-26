import timeit, random


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

# def quicksort(list):
#     high = len(list) - 1
#     low = 0
#     switched = False        #False = Damen till vänster. True = Damen till höger
#
#     if len(list) < 2:
#         return list
#     else:
#         queen = low
#         check = high
#         while queen != check:
#             if not switched:    #Detta körs när damen är till vänster
#                 if list[check] < list[queen]:
#                     switched = True
#                     list[queen], list[check] = list[check], list[queen]
#                     queen, check = check, queen
#                     check += 1
#                 else:
#                     check -=1
#             else:               #Detta körs när damen är till höger
#                 if list[queen] < list[check]:
#                     switched = False
#                     list[queen], list[check] = list[check], list[queen]
#                     queen, check = check, queen
#                     check -= 1
#                 else:
#                     check += 1
#
#         list[low:queen] = quicksort(list[low:queen])
#         list[(queen+1):high+1] = quicksort(list[(queen+1):high+1])
#         return list

def binarysearch(list, search):
    high = len(list)-1
    mid = high//2
    if search == list[mid]:
        return mid
    elif search < list[mid]:
        binarysearch(list[:mid],search)
    else:
        binarysearch(list[mid+1:],search)


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
    testartist = sort_list[-1].artist
    for i in range(10):
        print(sort_list[i].artist)

    linjsorttid = timeit.timeit(stmt=lambda: linsearch(sort_list, testartist), number=100)
    print('Linjärsökning för sorterad lista tog', round(linjsorttid, 4), 'sekunder')

    sorttid = timeit.timeit(stmt=lambda: quicksort(lista), number=10)
    print("Quicksort tog", round(sorttid, 4), "sekunder")

    timevek = []
    for i in range(1000):
        time = timeit.timeit(stmt= lambda: linsearch(lista, lista[random.randint(0,len(lista)-1)].artist), number= 100)
        timevek.append(time)
    randomtime = sum(timevek)/len(timevek)
    print('Linjärsökning i den osorterade listan för 1000 slumpade element tog i genomsnitt', round(randomtime,4), 'sekunder')


if __name__ == '__main__':
    main()