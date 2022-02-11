import DictHash

def makechildren(word):
    alph = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','å','ä','ö']
    variations = []
    for i in range(len(word)):
        for a in alph:
            new_word = word[:i] + a + word[(i+1):]
            if new_word not in variations:
                variations.append(new_word)
    return variations

def main():
    children = makechildren('tes')
    print(len(children))

if __name__ == "__main__":
    main()