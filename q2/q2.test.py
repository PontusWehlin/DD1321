import sys

## filinläsning - läser in en fil
## input - sträng(filnamn)
## output - lista
def filinläsning(filnamn):
    infil = open(filnamn,'r',encoding='UTF-8')
    filinnehåll = infil.read()
    filrader = filinnehåll.split('\n')
    return filrader

## Testare - testar om ordet som användare angivit finns i listan över genererade lösenord
## Input - Lista, string
##
def testare(passwords, testord):
    if testord not in passwords:
        print('Detta är ett bra lösenord!')
    else:
        print('Detta är inte ett bra lösenord')

def main():

    if len(sys.argv)>2:
        passwords = filinläsning(sys.argv[2])
        testare(passwords, sys.argv[1])
    else:
        print('Usage: ', sys.argv[0],' <ord> <file>')


if __name__ == '__main__':
    main()