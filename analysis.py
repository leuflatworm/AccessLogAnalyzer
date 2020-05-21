

month_dict = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}


def host(Files, sd, ed, ex):
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

        f.close()

    access_sorted = sorted(access_list.items(), key=lambda x:x[1], reverse=True)


    w = open("exports/" + ex, mode = "w")

    w.write("対象ファイル：")

    for i in Files:
        w.write(i + ",")

    w.write(",解析時期" + sd + "〜" + ed + "\n")

    for i in range(len(access_sorted)):
        w.write(access_sorted[i][0] + "," + str(access_sorted[i][1]) + "\n")



def time(Files, sd, ed, ex):

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
            if int(sd) <= int(cd) and int(cd) <= int(ed):
                print(cd)

                if cd in access_list:
                    n = access_list[cd]
                    n = n+1
                    access_list[cd] = n

                else:
                    access_list[cd] = 1


    w = open("exports/" + ex, mode = "w")

    w.write("対象ファイル：")

    for i in Files:
        w.write(i + ",")

    w.write(",解析時期" + sd + "〜" + ed + "\n")

    for i in access_list:
            w.write(i + "," + str(access_list[i]) + "\n")




if __name__ == '__main__':
    host()