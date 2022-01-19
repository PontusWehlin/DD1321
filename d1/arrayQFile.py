from array import array

class ArrayQ:
    def __init__(self):
        self.__array = array('b')
    def enqueue(self,data):
        self.__array.append(data)
    def dequeue(self):
        return self.__array.pop(0)
    def isEmpty(self):
        if len(self.__array) == 0:
            return True
        else:
            return False

def basictest():
    q = ArrayQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()
    if (x == 1 and y == 2):
        print('Test OK!')
    else:
        print('FAILED expected x=1 and y=2 but got x=',x,'y=',y)

if __name__ == '__main__':
    basictest()