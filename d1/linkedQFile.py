class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedQ:
    def __init__(self):
        self.__first = None
        self.__last = None

    def enqueue(self, value):
        if self.__first == None:
            self.__first = Node(value)
            self.__last = self.__first
        else:
            self.__last.next = Node(value)
            self.__last = self.__last.next

    def dequeue(self):
        return_value = self.__first.value
        self.__first = self.__first.next
        return return_value

    def isEmpty(self):
        if self.__first == None:
            return True
        else:
            return False
    def remove(self,x):
        try:
            if self.__first == None:
                pass
            elif x == 1:
                self.__first = self.__first.next
            else:
                nod = self.__first
                for i in range(x-2):
                    nod = nod.next
                nod.next = nod.next.next
        except AttributeError:
            pass


def basictest():
    print('Test: Kontrollerar 2 tomma köer...')
    kö = LinkedQ()
    print(kö.isEmpty())
    kö.enqueue(7)
    kö.dequeue()
    print(kö.isEmpty())

    print('\nTest: Kontrollerar så dequeue kommer i rätt ordning...')
    kö.enqueue(1)
    kö.enqueue(2)
    kö.enqueue(3)
    ordning = []
    ordning.append(kö.dequeue())
    ordning.append(kö.dequeue())
    ordning.append(kö.dequeue())
    print(ordning)

    print('\nTest: Kontrollerar om det går att ta bort ett element i mitten av kön och ett element som inte finns i kön...')
    kö.enqueue(1)
    kö.enqueue(2)
    kö.enqueue(3)
    kö.remove(2)
    kö.remove(1)
    kö.remove(3)
    kö.remove(1)
    print(kö.isEmpty())

    print('\nTest: Kontrollerar om det går att ta bort det elementet bakifrån...')
    kö.enqueue(1)
    kö.enqueue(2)
    kö.remove(2)
    kö.remove(1)
    print(kö.isEmpty())


if __name__ == '__main__':
    basictest()