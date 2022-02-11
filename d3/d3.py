import DictHash

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
    words = DictHash.DictHash()
    for i in lines:
        words.store(i.rstrip('\n'), 1)
    return words

def main():
    valid_words = import_file('word3.txt')
    old_words = DictHash.DictHash()
    children = makechildren('fan', valid_words, old_words)
    for i in children:
        old_words.store(i,1)
    print(old_words.keys())
    print(len(children))


if __name__ == "__main__":
    main()