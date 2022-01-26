## LAB5


# global variables

url = "https://cloud.timeedit.net/kth/web/public01/ri.html?h=t&sid=7&p=20201021.x%2C20210117.x&objects=381614.5&ox=0&types=0&fe=0&g=f&ds=f&cch=16-53%2C6-10"
urlfile = "DD1321.htm"
############################################################
#
# imports and defs
#
import re, getopt, sys, urllib.request, json, datetime


class Schemaevent:
    def __init__(self):
        self.veckodag = ''
        self.datum = ''
        self.vecka = ''
        self.info = []
        self.tid = ''

    def __str__(self):
        s = "{} => {:3s}, {:>5s}, {:>3s}, {} ;".format(self.__class__.__name__, self.vecka, self.veckodag,
                                                       self.datum, self.tid)
        for h in self.info:
            s += h + "; "
        return s

    def __contains__(self, x):
        if x in self.vecka:
            return True
        if x in self.veckodag:
            return True
        if x in self.datum:
            return True
        if x in self.tid:
            return True
        if x in self.info:
            return True


###########################################################################
##
## parse_url_file
## Gör om strängen till en lista med schemat
## IN
## En sträng
## OUT
## En lista
def parse_url_file(file_content):
    vek = []
    veckonummer = 'Nan'
    veckodag = 'Nan'
    reg_expr_k = re.compile(
       '.*?td.*?class.*?weekColumn.*?>*(v.*?)<.')

    reg_expr_w = re.compile(
        '.*?td.*?class.*?headline.*?> *([MTOFL][a-ö]+) *20[12][0-9]-0?([123]?[0-9])-0?([123]?[0-9])<.*weekin.*> *(v.*?)<.',
        re.I)

    reg_expr_d = re.compile(
        '.*?td.*?class.*?headline.*?>([MTOFL][a-ö]+) *20[12][0-9]-0?([123]?[0-9])-0?([123]?[0-9])<.')

    reg_expr_t = re.compile('.*?td +id="time.*?>(.+?)<.td')

    reg_expr_i = re.compile('.*?td.*?class.*?column[0-1].*?>(.*?)<.td', re.I)

    lines = file_content.split('\n')
    qq = Schemaevent()
    newEntry = False
    for j, line in enumerate(lines):

        m = reg_expr_k.match(line)
        if (m!= None):
            veckonummer = m.group(1)
            next

        m = reg_expr_i.match(line)
        if (m != None) and len(m.group(1)) > 0:
            qq.info.append(m.group(1))
            next

        m = reg_expr_t.match(line)
        if (m != None):
            if newEntry == True:
                vek.append(qq)
                qq = Schemaevent()
            newEntry = True
            qq.veckodag = veckodag
            qq.vecka = veckonummer
            qq.tid = m.group(1)
            qq.datum = datum
            next

        m = reg_expr_d.match(line)
        if (m != None):
            veckodag = m.group(1)
            datum = m.group(3) + "/" + m.group(2)
            next

        m = reg_expr_w.match(line)
        if (m != None):
            veckodag = m.group(1)
            veckonummer = m.group(4)
            datum = m.group(3) + "/" + m.group(2)
            next
    vek.append(qq)
    return vek


###########################################################################
##
## get file content
## Läser in en fil
## IN
## En sträng
## OUT
## En sträng
def get_file_content(file_name):
    infil = ''
    try:
        infil = open(file_name, 'r')
    except:
        print("No such file", file_name, " please run with --update")
        print("	python", sys.argv[0], "--update")
        sys.exit()

    #file_content = infil.readlines()
    file_content = infil.read()
    return file_content

###########################################################################
##
## usage
##
## IN
##
## OUT
##
def get_url_content(course, start="YYYY-MM-DD", end = "YYYY-MM-DD"):
    schemaurl = "https://www.kth.se/social/api/schema/v2/course/"
    if start == "YYYY-MM-DD":
        start = "?startTime=" + datetime.date.today().strftime("%Y-%m-%d")
    else:
        start = "?startTime=" + start

    if end == "YYYY-MM-DD":
        end = "&endTime=" + str(int(datetime.date.today().strftime("%Y"))+int(datetime.date.today().strftime("%m"))+6//12) + "-" + str((int(datetime.date.today().strftime("%m"))+6)%12) + "-30"
    else:
        end= "&endTime=" + end

    schemaurl += course + start + end

    try:
        request_data = urllib.request.urlopen(schemaurl).read()  # hämtar data från REST-servern
        utf_data = request_data.decode('utf-8')  # översätter u00f6 -> ö
        datastruktur = json.loads(utf_data)  # lägger in i en pythonstruktur

        #for i in range(len(datastruktur["entries"])):
        #    print(datastruktur["entries"][i]["start"])
        #    print(datastruktur["entries"][i]["end"])
        #    print(datastruktur["entries"][i]["title"])
        #    for x in datastruktur["entries"][i]["locations"]:
        #        print(x["name"])

        return datastruktur
    except urllib.error.HTTPError as exception:
        print(exception)
        print("!!Kontrollera kurskoden!!")



###########################################################################
##
## usage
##
## IN
##
## OUT
##
def usage():
    print("Usage example:")
    print("python", sys.argv[0], "--update ")
    print("	updates Time Edit schedule")
    print("python", sys.argv[0], '--check "v 49"')
    print("	checks schedule for week 49")
    print("python", sys.argv[0])
    print("	prints previously downloaded schedule")


###########################################################################
##
## parse_command_line_args
##
## IN
##
## OUT
## Dictionary med kommandot som nyckel
def parse_command_line_args():
    try:
        opts, rest = getopt.getopt(sys.argv[1:], "hc:u", ["help", "check=", "update"])
    except getopt.GetoptError:
        # print help information and exit:
        print("Unknown option")
        usage()
        sys.exit(2)

    todo = {}
    for option, value in opts:
        if option in ("-h", "--help"):
            usage()
            sys.exit()
        elif option in ('--check', '-c'):
            todo["check"] = value
        elif option in ('--update', '-u'):
            todo["update"] = value

    return todo


###########################################################################
##
## print_schedule
##
## IN
##
## OUT
##
def print_schedule(data):
    print("----------- Schedule -------------")
    for item in data:
        print(item)


###########################################################################
##
## search_data
##
## IN
## What - Är vilken vecka som search ska kolla om "check" används i input
## OUT
##
def search_data(what, dataset):
    found = False
    for item in dataset:
        if (what in item):
            found = True
            print(item)
    if (found == False):
        print("Nothing happens", what)


###########################################################################
##
## main
##
## IN
##
## OUT
##
def main():
    global url, urlfile

    # get command line options
    todo = parse_command_line_args()

    # update time edit file
    if 'update' in todo:
        print("fetching url ...")
        webcontent = urllib.request.urlopen(url)
        with open(urlfile, "w") as fil:
            for row in webcontent:
                utf8line = row.decode('utf8')
                fil.write(utf8line)
        print("         done")

    # Get schedule from disc
    filedata = get_file_content(urlfile)
    sched = parse_url_file(filedata)

    get_url_content("DD1321")
    # Do something
    if 'check' in todo:
        search_data(todo["check"], sched)
    else:
        print_schedule(sched)


###########################################################################

if __name__ == "__main__":
    main()

