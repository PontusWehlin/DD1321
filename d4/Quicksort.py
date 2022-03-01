def quicksortwhile(list):
    low = 0
    high = len(list)-1
    pivots = [low, high]

    if len(list) < 2:
        return(list)

    while True:
        queen, check = pivots[0], pivots[1]
        switched = False
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
        print('---------')
        print(pivots)
        if queen in pivots:
            pivots.remove(queen)
            if queen+1 <= len(list):
                pivots.append(queen+1)
        if queen < pivots[0]: pass
        elif queen-1 not in pivots and queen-1 >= 0:
            pivots.append(queen-1)
            if queen+1 not in pivots: pivots.append(queen+1)
        elif queen+1 not in pivots: pivots.append(queen+1)

        if len(pivots) < 2:
            break

        pivots.sort()

        print(pivots)
        if pivots[1] - pivots[0] < 2:
            pivots.pop(0)
        print(pivots)

    return list


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
    sorted = quicksortwhile(v)
    print(sorted)
    #element = binarysearch(sorted,4)
    #print(type(element))
    #print(element)



if __name__ == '__main__':
    test()