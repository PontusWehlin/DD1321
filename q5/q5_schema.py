
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

###########################################################################

if __name__ == "__main__":
    main()