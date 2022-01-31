
import sys, json, q5, re

###########################################################################
##
## usage
## prints help when programmed is used wrong
## IN
##
## OUT
##
def usage():
    print(' ')
    print("Usage examples:")
    print("python3", sys.argv[0], '"course code"')
    print("Prints the schedule for that course")
    print(' ')
    print("python3", sys.argv[0], '"course code" start YYYY-MM-DD')
    print('Prints the schedule for that course starting at that date')
    print(' ')
    print("python3", sys.argv[0], '"course code" end YYYY-MM-DD"')
    print('Prints the schedule for that course ending at that date')
    print(' ')
    print('Start and end time can be combined:')
    print('python3', sys.argv[0], '"course code" start YYYY-MM-DD end YYYY-MM-DD')
    sys.exit()

###########################################################################
##
## usage
##
## IN
## Dictionary with "entries" key
## OUT
##
def print_schedule(datastruktur):
    for i in range(len(datastruktur["entries"])):
        print(datastruktur["entries"][i]["start"][:13], end="-")
        print(datastruktur["entries"][i]["end"][11:13], end=" ")
        print("{:<20}".format(datastruktur["entries"][i]["title"]), end=" ")
        for x in datastruktur["entries"][i]["locations"]:
            print(x["name"], end=" ")
        print()

###########################################################################
##
## usage
## checks if the input date(s) is enterd in correct form
## IN
##
## OUT
##
def check_input_date():
    reg_expr = re.compile('.*20[12][0-9]-0?([01][0-9])-0?([0123][0-9])')
    if len(sys.argv) == 4:
        if sys.argv[2] not in ['start', 'end']:
            print(sys.argv[2], 'is not a valid input argument')
            sys.exit()
        else:
            date = reg_expr.match(sys.argv[3])
            if date == None:
                print('Invalid date, make sure to enter as "YYYY-MM-DD"')
                sys.exit()
            else:
                return()
    elif len(sys.argv) == 6:
        if sys.argv[2] != 'start' or sys.argv[4] != 'end':
            print(sys.argv[2],'or', sys.argv[4], 'is not valid input arguments or in wrong order')
            sys.exit()
        else:
            if reg_expr.match(sys.argv[3]) == None:
                print('Invalid start date, make sure to enter as "YYYY-MM-DD"')
                sys.exit()
            elif reg_expr.match(sys.argv[5]) == None:
                print('Invalid end date, make sure to enter as "YYYY-MM-DD"')
                sys.exit()
            return()
    else:
        usage()

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
        sys.exit()
    elif len(sys.argv) == 2:
        datastruktur = q5.get_url_content(sys.argv[1]) #Gets the schedule from rest api, using function from q5.py
    else:
        check_input_date()
        if len(sys.argv) == 4:
            if sys.argv[2] == 'start':
                datastruktur = q5.get_url_content(sys.argv[1], start=sys.argv[3])
            else:
                datastruktur = q5.get_url_content(sys.argv[1], end=sys.argv[3])
        else:
            datastruktur = q5.get_url_content(sys.argv[1], start=sys.argv[3], end=sys.argv[5])
    print_schedule(datastruktur)


###########################################################################

if __name__ == "__main__":
    main()