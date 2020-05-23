# UIを担当する。

import os
import analysis
import sys
import divider

##対話モードでのUIと処理
def main():

    print("====================================================================================================")
    print("|    AccessLogAnalyzer                                                                             |")
    print("| アクセスログの解析を行います。                                                                   |")
    print("| このプログラムはPython 3.7.6にて動作確認を行っています。                                         |")
    print("| コマンドラインオプションを指定しない場合は対話モードで起動します。                               |")
    print("|                                                                                                  |")
    print("| 起動時に以下の様に指定した場合は結果のみ出力します。                                             |")
    print("| python3 main.py f=FILE_NAME sd=START_DATE(yyyymmdd) ed=END_DATE(yyyymmdd) ex=EXPORT_FILE l=LEVEL |")
    print("====================================================================================================")

    Filenames = [] #対象とするファイルのリスト
    sdate = "00000000"#集計を開始する日付
    edate = "99999999"#集計を終了する日付
    ex_file = ""
    fn = []

    ##対象とするファイルの選択を行う
    xxx = "n"
    while xxx == "n":
        print("対象とするファイルを選択してください。(空白区切りの数字またはallが使えます)")
        files = os.listdir("targets")
        files.remove("tmp")
        for i in range(len(files)):
            if files[i] in Filenames:
                print("[" + str(i) + "]" + files[i] + " selected!!!")
            else:
                print("[" + str(i) + "]" + files[i])

        select = input().split(" ")

        if select[0] == "all":
            print("全てでよろしいですか？[y/n]")
            ans = input()
            if ans == "y":
                Filenames.extend(files)


        else:
            try:
                for s in select:
                    print(files[int(s)], end=" ")
                    print("でよろしいですか？[y/n]")
                    if input() == "y":
                        for i in select:
                            Filenames.append(files[int(i)])

            except TypeError:
                print("all又は半角英数字で回答してください。")

        for i in range(len(Filenames)):
            print(Filenames[i])

        while True:
            print("以上でよろしいですか？[y/n]")
            ans = input()
            if ans == "y":
                xxx = "y"
                break
            elif ans == "n":
                break



    ##期間の指定
    ##開始時期指定
    while True:
        print("集計を開始する日付を指定しますか？[y/n]")
        ans = input()
        if ans == "y":
            print("集計を開始する日付をyyyymmddで入力してください(例：1970年1月1日 -> 19700101)")
            sdate = input()
            break
        elif ans == "n":
            break
        else:
            print("[y/n]で回答してください。")

    ##終了時期指定
    while True:
        print("集計を終了する日付を指定しますか？[y/n]")
        ans = input()
        if ans == "y":
            print("集計を終了する日付をyyyymmddで入力してください(例：1970年1月1日 -> 19700101)")
            edate = input()
            break
        elif ans == "n":
            break
        else:
            print("[y/n]で回答してください")

    ##時期が正しく入力されているかどうかを確認。正しくない場合には全期間での解析を行う。
    try:
        if int(sdate)>int(edate):
            print("開始時期よりも終了時期が前になっています。（初期設定に戻します。）")
            sdate = "00000000"
            edate = "99999999"
    except ValueError:
        print("値が不正です。（初期設定に戻します。）")
        sdate = "00000000"
        edate = "99999999"

    if sdate == "00000000" and edate == "99999999":
        print("全期間で集計を行います。")
    else:
        print(sdate + "から" + edate + "の期間で集計を行います。")


    ##出力ファイル指定
    while True:
        print("出力ファイル名を指定しますか？[y/n]（指定しない場合はexport.csvとして出力します。）")
        ans = input()

        if ans == "y":
            print("出力ファイル名を入力してください")
            ex_file = input()
            break
        elif ans == "n":
            ex_file = "export.csv"
            break
        else:
            print("[y/n]で回答してください。")
    
    ##メモリ節約レベル（速度とメモリ節約について中間ファイルの細かさで設定を行う。）
    while True:
        print("メモリ節約レベルを指定してください。0~4（0が高速、4がメモリ節約）多くの場合1を推奨します。メモリ不足でエラーが出る場合に数値を上げてください。ログファイルが単一ファイルであり、メモリが十分の場合に0を選択することで最も高速で処理できます。")
        ans = input()
        
        try:
            if 0 <= int(ans) and int(ans) <= 4:
                l = int(ans)
                break
            else:
                print("0~4で指定してください。")
                
        except ValueError:
            print("数値で指定してください。(0~4)")
    
    ##入力データの前処理を行うためにdividerをもちいる。 
    
    try:
        fn = Filenames
        if l != 0:    
            Filenames = divider.divider(Filenames, l)

            

            analysis.analysis(Filenames, sdate, edate, ex_file, fn)
    
            if l != 0:
                for f in Filenames:
                    os.remove("targets/" + f)
                    
    except FileNotFoundError:
        print("対象ファイルが存在しません。正しく exports/ 内に存在しているか確認してください。")


##コマンドラインオプションを用いた解析の処理
def cmd(opt):
    
    ##変数の初期化
    Filenames = []
    fn = []
    l = 1
    a = {"sd":"00000000", "ed":"99999999", "ex":"export.csv", "l":1}
    
    ##コマンドラインオプションをそれぞれ変数に代入
    for o in opt[1:]:
        s = o.split("=")
        a[s[0]] = s[1]
        
    ##全てのファイルが選択されていた場合の処理
    if a["f"] == "all":
        Filenames = os.listdir("targets")
        Filenames.remove("tmp")
    
    #カンマ区切りで与えられたファイル名を分割してリスト化
    else:
        Filenames = a["f"].split(",")
        
    try:
        l = int(a["l"])
    except ValueError:
        print("lの値は0~4で指定してください。")
        
    if not a["sd"].isdecimal() and a["ed"].isdecimal():
        print("sd,edはyyyymmddの形式、半角英数字で入力してください。初期設定に戻します")
        a["sd"] = "00000000"
        a["ed"] = "99999999"
        
    
    fn = Filenames
    
    try:
        if l != 0:
            Filenames = divider.divider(Filenames, l)
        
        
        analysis.analysis(Filenames, a["sd"], a["ed"], a["ex"], fn)
    
        if l != 0:
            for f in Filenames:
                os.remove("targets/" + f)
                
    except FileNotFoundError:
        print("対象ファイルが存在しません。正しく exports/ 内に存在しているか確認してください。")




if __name__ == '__main__':
    args = sys.argv
    if len(args) <= 1:
        main()
    else:
        cmd(args)
