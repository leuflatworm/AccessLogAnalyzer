

month_dict = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}


def analysis(Files, sd, ed, ex):

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
            hh = date[13:15]

            cd = yyyy + mm + dd + hh

            line = f.readline()
            if int(sd + "00") <= int(cd) and int(cd) <= int(ed + "23"):

                if cd in access_list:
                    if IP in access_list[cd]:
                        n = access_list[cd][IP]
                        n = n+1
                        access_list[cd][IP] = n

                    else:
                        access_list[cd][IP] = 1

                else:
                    access_list[cd] = {}
                    access_list[cd][IP] = 1


    access_time_sorted = sorted(access_list.items())


    w = open("exports/" + ex, mode = "w")

    w.write("対象ファイル：")

    for i in Files:
        w.write(i + ",")

    w.write(",解析時期" + sd + "〜" + ed + "\n")

    for i in range(len(access_time_sorted)):
        print("-----------------------------------------------------------------------")
        print(access_time_sorted[i][0])
        access_sorted = sorted(access_time_sorted[i][1].items(), key=lambda x:x[1], reverse = True)
        print(access_sorted)
        w.write(access_time_sorted[i][0][:8] + ":" + access_time_sorted[i][0][8:10] + ":00~" + access_time_sorted[i][0][8:10] + ":59, ")
        for j in range(len(access_sorted)):
            print(access_sorted[j][0] + " : " + str(access_sorted[j][1]))
            w.write(access_sorted[j][0] + ":" + str(access_sorted[j][1]) + ", ")

        w.write("\n")


    w.close()



if __name__ == '__main__':
    host()
