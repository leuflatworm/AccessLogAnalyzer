month_dict = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}


##メインの処理です。
def divider(Files, l):
    date_list = []

    for file in Files:
        f = open("targets/" + file)
        line = f.readline()

        ##一行ずつ読み込むことでメモリを節約します。
        while line:
            ##ログデータの中から日付データを取り出します。
            elm = line.split(" ")
            date = elm[4]
            dd = date[1:3]
            mm = month_dict[date[4:7]]
            yyyy = date[8:12]
            hh = date[13:15]
            
            cd = ""
            
            ##  メモリ節約レベルによって中間ファイルを「年で分ける、月で分ける、日で分ける、時間で分ける」の中から選びます。   
            if l == 1:
                cd = yyyy
            elif l == 2:
                cd = yyyy + mm
            elif l == 3:
                cd = yyyy + mm + dd
            elif l == 4:
                cd = yyyy + mm + dd + hh    
             
            ##中間ファイルの出力先
            out = "tmp/" + cd

            ##日付けごとに対応する中間ファイルに書き込んでいきます。
            w = open("targets/" + out, mode="a")
            w.write(line)
            w.close()
            
            if out not in date_list:
                date_list.append(out)

            
                        
            line = f.readline()
            
    ##中間ファイルを日付順に並べます。
    date_list.sort()
        
    ##中間ファイルのリストを返します
    return date_list


if __name__ == '__main__':
    devider()
