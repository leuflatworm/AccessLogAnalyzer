import os
import analysis
import sys

def main():

    print("============================================================================================")
    print("|    AccessLogAnalyzer                                                                     |")
    print("| アクセスログの解析を行います。                                                           |")
    print("| このプログラムはPython 3.7.6にて動作確認を行っています。                                 |")
    print("| コマンドラインオプションを指定しない場合は対話モードで起動します。                       |")
    print("|                                                                                          |")
    print("| 起動時に以下の様に指定した場合は結果のみ出力します。                                     |")
    print("| python3 main.py f=FILE_NAME sd=START_DATE(yyyymmdd) ed=END_DATE(yyyymmdd) ex=EXPORT_FILE |")
    print("============================================================================================")

    Filenames = [] #対象とするファイルのリスト
    sdate = "00000000"#集計を開始する日付
    edate = "99999999"#集計を終了する日付
    ex_file = ""

    ##対象とするファイルの選択を行う
    xxx = "n"
    while xxx == "n":
        print("対象とするファイルを選択してください。(空白区切りの数字またはallが使えます)")
        files = os.listdir("targets")
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



    analysis.analysis(Filenames, sdate, edate, ex_file)


def cmd(opt):
    a = {"s":"00000000", "e":"99999999", "x":"export.csv"}
    print("ok")
    for o in opt[1:]:
        s = o.split("=")
        a[s[0]] = s[1]


    Filenames = a["f"].split(",")
    analysis.analysis(Filenames, a["s"], a["e"], a["x"])







if __name__ == '__main__':
    args = sys.argv
    if len(args) <= 1:
        main()
    else:
        cmd(args)
