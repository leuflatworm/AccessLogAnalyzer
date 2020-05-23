# 実際に解析を行う

## 月の表記を数字に変更するための辞書
month_dict = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}

## 対象ファイル、時期、出力ファイルを受け取って解析を行う
def analysis(Files, sd, ed, ex, fn = None):
    
    ##変数の初期化
    access_list = {}
    
    ##ファイルの初期化 同名ファイルが残っていた場合は上書きを行う
    w = open("exports/" + ex, mode = "w")

    w.write("対象ファイル：")
    if fn == None:
        for i in Files:
            w.write(i + ",")
    else:
        for i in fn:
            w.write(i + ",")

    w.write(",解析時期" + sd + "〜" + ed + "\n")
    
    w.close()
    
    ##ファイルごとに解析を行う
    for file in Files:
        access_list = {}
        
        
        f = open("targets/" + file)
        line = f.readline()
        
        ##一行ずつ抽出して処理する。
        while line:
            elm = line.split(" ")
            IP = elm[0]
            date = elm[4]
            dd = date[1:3]
            mm = month_dict[date[4:7]]
            yyyy = date[8:12]
            hh = date[13:15]

            cd = yyyy + mm + dd + hh
            
            
            ##解析対象時期かどうかを判定
            if int(sd + "00") <= int(cd) and int(cd) <= int(ed + "23"):
                
                ##同日同IPからのアクセスがあった場合にはアクセス回数＋1、初アクセスであれば新しく1回で記録
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
                
            line = f.readline()

        ##アクセスを日時順に並べ替え
        access_time_sorted = sorted(access_list.items())

        for i in range(len(access_time_sorted)):
            a = open("exports/" + ex, mode = "a")
            
            ##IPをアクセス回数順に並べ替え
            access_sorted = sorted(access_time_sorted[i][1].items(), key=lambda x:x[1], reverse = True)

            a.write(access_time_sorted[i][0][:8] + ":" + access_time_sorted[i][0][8:10] + ":00~" + access_time_sorted[i][0][8:10] + ":59, ")
            for j in range(len(access_sorted)):
                a.write(access_sorted[j][0] + ":" + str(access_sorted[j][1]) + ", ")

            a.write("\n")
            a.close()
        
        
    print("Done")



if __name__ == '__main__':
    host()
