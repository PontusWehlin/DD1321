## Storbokstav - Tar in en liten bokstav och skickar tillbaka stor bokstav
## Indata - Sträng
## Utdata - Sträng
def storbokstav(bokstav):
    alfabetet = {'a':'A', 'b':'B','c':'C','d':'D','e':'E','f':'F','g':'G','h':'H'
                 ,'i':'I','j':'J','k':'K','l':'L','m':'M','n':'N','o':'O','p':'P'
                 ,'q':'Q','r':'R','s':'S','t':'T','u':'U','v':'V','w':'W','x':'X'
                 ,'y':'Y','z':'Z','å':'Å','ä':'Ä','ö':'Ö'}
    if bokstav in alfabetet:
        bokstav = alfabetet[bokstav]
    else:
        print(bokstav, ' finns inte i alfabetet.')
    return(bokstav)

## Filinläsning - Läser in en fil från samma mapp som programmet ligger i
## Indata - Sträng, filnamn
## Utdata - list, raderna i filen
def filinläsning(filnamn):
    infil = open(filnamn, 'r', encoding='UTF-8')
    fil = infil.read()
    fillista = fil.split("\n")
    infil.close()
    return fillista

## Filsparning - Sparar ner en ordlista i en fil
## Indata - (sträng,lista)
## Utdata -
def filsparning(filnamn, ordlista):
    utfil = open(filnamn, 'w', encoding='UTF-8')
    ordlista = [s + '\n' for s in ordlista]
    utfil.writelines(ordlista)
    utfil.close()

## Enstor - Tar in ett ord och skickar ut en lista med ordet där varje ord har EN unik stor bokstav
## Indata - Sträng
## Utdata - Lista
def enstor(ord):
    ordvar = []
    for i in range(len(ord)):
        tempord = ord
        tempord = tempord[:i] + storbokstav(tempord[i]) + tempord[i+1:]
        ordvar.append(tempord)
    return(ordvar)

## Tvåstor - Tar in ett ord och skickar ut en lista med ordet där varje ord har TVÅ unika stora bokstäver
## Indata - Sträng
## Utdata - Lista
def tvåstor(ord):
    ordvar = []
    for i in range(len(ord)-1):
        for k in range(i+1,len(ord)):
            tempord = ord
            tempord = tempord[:i] + storbokstav(tempord[i]) + tempord[i+1:k] + storbokstav(tempord[k]) + tempord[k+1:]
            ordvar.append(tempord)
    return ordvar

## Skjutinspecial - Tar in lista med ord och skickar ut en lista med orden med inskjutna specialtecken
## Indata - Lista eller sträng
## Utdata - Lista
def skjutinspecial(orden, antalSpecialtecken = 14):
    specialtecken = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/']
    ordvar = []
    if type(orden) == list:
        for j in range(len(orden)):
            ord = orden[j]
            for i in range(len(ord)+1):
                for k in range(antalSpecialtecken):
                    tempord = ord
                    tempord = tempord[:i] + specialtecken[k] + tempord[i:]
                    ordvar.append(tempord)
    # Denna bit används för tillfällen när endast ett ord skickas in
    else:
        ord = orden
        for i in range(len(ord) + 1):
            for k in range(antalSpecialtecken):
                tempord = ord
                tempord = tempord[:i] + specialtecken[k] + tempord[i:]
                ordvar.append(tempord)
    return ordvar

## Variator - Tar in ett ord, applicerar Enord, Tvåord och skjutinspecial, och skickar sedan tillbaka en lista med resultatet
## Indata - Sträng
## Utdata - Lista
def variator(ord):
    ordvar = [ord]
    enord = enstor(ord)
    ordvar.extend(enord)
    tvåord = tvåstor(ord)
    ordvar.extend(tvåord)
    ordspec = skjutinspecial(ordvar)
    ordvar.extend(ordspec)
    return ordvar
## Komplexitet - Tar in ett ord och kollar hur många kombinationer av ordet som skapas av olika många specialtecken
## Indata - sträng
## Utdata - dictionary
def komplexitet(ord):
    komplex = {}
    for i in range(15):
        komplex[i] = len(skjutinspecial(ord, antalSpecialtecken=i))+1
    return komplex


def main():
    filnamn = input('Vilket namn ska den sparade filen ha? ')
    filord = filinläsning("p2_passwords.txt")
    orddict = {}
    ordlista = []
    for i in range(len(filord)):
        tempdict = {}
        tempordlista = variator((filord[i]))
        for k in range(len(tempordlista)):
            if tempordlista[k] not in tempdict:
                tempdict[tempordlista[k]] = 1
                ordlista.append(tempordlista[k])
        orddict[filord[i]] = len(tempdict)
    filsparning(filnamn, ordlista)
    for key in sorted(orddict, key=len):
        print("{:<8} {:<5}".format(key, orddict[key]))

    # Komplexitets undersökning
    komplexdict = {}
    for i in orddict:
        if len(i) not in komplexdict:
            komplexdict[len(i)] = orddict[i]

    # Printar ut resultat av komplexitetsundersökningen
    print('\nKomplexitets undersökning:\n')
    print("Antal bokstäver : Antal kombinationer.")
    for key in sorted(komplexdict):
        print("{:<2}: {:<4}".format(key, komplexdict[key]))
    print("\nFör password")
    print("Antal inskjutna specialtecken : Antal kombinationer")
    komplex = komplexitet("password")
    for key in sorted(komplex):
        print("{:<2}: {:<4}".format(key, komplex[key]))

if __name__ == "__main__":
    main()