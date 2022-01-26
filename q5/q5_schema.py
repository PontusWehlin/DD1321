
import sys, json, q5

###########################################################################
##
## usage
##
## IN
##
## OUT
##
def usage():
    print("Usage examples:")
    print("python3", sys.argv[0], "course code")
    print("Prints the schedule for that course")
    print('python3", sys.argv[0], "course code start "YYYY-MM-DD"')
    print('Prints the schedule for that course starting at that date')
    print('python3", sys.argv[0], "course code end "YYYY-MM-DD"')
    print('Prints the schedule for that course ending at that date')

###########################################################################
##
## usage
## 
## IN
##
## OUT
##
def main():
    if len(sys.argv) == 1:
        usage()
        exit()
    elif len(sys.argv) == 2:
        datastruktur = q5.get_url_content(sys.argv[1])

    for i in range(len(datastruktur["entries"])):
        print(datastruktur["entries"][i]["start"][:13], end="-")
        print(datastruktur["entries"][i]["end"][11:13], end=" ")
        print("{:<20}".format(datastruktur["entries"][i]["title"]), end=" ")
        for x in datastruktur["entries"][i]["locations"]:
            print(x["name"], end=" ")
        print()


###########################################################################

if __name__ == "__main__":
    main()