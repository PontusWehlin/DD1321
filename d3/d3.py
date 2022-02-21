from DictHash import DictHash
from linkedQFile import LinkedQ
import sys

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

def makechildren(word, valid_words, old_words):
    alph = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','å','ä','ö']
    variations = []
    for i in range(len(word)):
        for a in alph:
            new_word = word[:i] + a + word[(i+1):]
            if (new_word not in variations) and (new_word in valid_words) and (new_word not in old_words.keys()):
                variations.append(new_word)
    return variations

def import_file(filename):
    file = open(filename,'r',encoding='UTF-8')
    lines = file.readlines()
    words = DictHash()
    for i in lines:
        words.store(i.rstrip('\n'), 1)
    return words

def writechain(Node):
    if Node != None:
        writechain(Node.parent)
        print(Node.word)

def main():
    if len(sys.argv) < 3:
        print("Start- och slutord saknas")
        print("Använd programmet så här: \n\t python3", sys.argv[0], " [startord] [slutord]")
        sys.exit()

    start_word = sys.argv[1]
    end_word = sys.argv[2]
    valid_words = import_file('word3.txt')
    old_words = DictHash()
    wordQ = LinkedQ()

    wordQ.enqueue(ParentNode(start_word))
    found = False
    while not found:
        if wordQ.isEmpty():
            print('No way found')
            found = True #debatable bool name
        else:
            parent = wordQ.dequeue()
            children = makechildren(parent.word, valid_words, old_words)
            for i in children:
                old_words.store(i,1)
                wordQ.enqueue(ParentNode(i,parent))
                if i == end_word:
                    writechain(ParentNode(i,parent))
                    found = True


if __name__ == "__main__":
    main()