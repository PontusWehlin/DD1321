from linkedQFile import LinkedQ

def skapa_ordningen():
    in_data = input('Ange en ordning av kort: ')
    ordning = in_data.split(' ')
    kö = LinkedQ()
    for siffra in ordning:
        kö.enqueue(int(siffra))
    return kö

def main():
    kö = skapa_ordningen()
    resultat = []
    while not kö.isEmpty():
        kö.enqueue(kö.dequeue())
        resultat.append(kö.dequeue())
    print(resultat)

if __name__ == '__main__':
    main()