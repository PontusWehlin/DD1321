import math

def Quicksort(list):
    high = len(list) - 1
    low = 0
    switched = False

    if len(list) < 2:
        return list
    else:
        queen = low
        check = high
        while queen != check:
            if not switched:
                if list[check] < list[queen]:
                    switched = True
                    list[queen], list[check] = list[check], list[queen]
                    queen, check = check, queen
                    check += 1
                else:
                    check -=1
            else:
                if list[queen] < list[check]:
                    switched = False
                    list[queen], list[check] = list[check], list[queen]
                    queen, check = check, queen
                    check -= 1
                else:
                    check += 1

        list[low:queen] = Quicksort(list[low:queen])
        list[(queen+1):high+1] = Quicksort(list[(queen+1):high+1])
        return list

def binarysearch(list, search):
    print('test')
    high = len(list)-1
    mid = (high//2)
    if search == list[mid]:
        return mid
    elif search < list[mid]:
        binarysearch(list[0:mid],search)
    else:
        binarysearch(list[mid+1:high],search)

def test():
    v = [5, 3, 7, 6, 2, 4, 8, 9, 1]
    print(v)
    sorted = Quicksort(v)
    print(sorted)
    element = binarysearch(sorted,4)
    print(type(element))
    print(element)



if __name__ == '__main__':
    test()