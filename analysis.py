

month_dict = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}

test = '10.2.3.4 - - [18/Apr/2005:00:10:47 +0900] "GET / HTTP/1.1" 200 854 "-" "Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)"'


def main(Files, sd, ed, ex):
    access_list = {}

    for file in Files:
        f = open("targets/" + file)
        line = f.readline()


        while line:
            elm = line.split(" ")
            IP = elm[0]
            date = elm[4]
            dd = date[1:3]
            mm = month_dict[date[4:7]]
            yyyy = date[8:12]

            cd = yyyy + mm + dd

            line = f.readline()
            if int(sd) < int(cd) and int(cd) < int(ed):
                print(IP)

                if IP in access_list:
                    n = access_list[IP]
                    n = n+1
                    access_list[IP] = n

                else:
                    access_list[IP] = 1


    for i in access_list:
        print(i + ":" + str(access_list[i]))







if __name__ == '__main__':
    main()
