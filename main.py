import os
import analysis

def main():

    print("==========================================================")
    print("=AccessLogAnalyzer                                       =")
    print("=アクセスログの解析を行います。                          =")
    print("=このプログラムはPython 3.7.6にて動作確認を行っています。=")
    print("==========================================================")

    Filenames = [] #対象とするファイルのリスト
    sdate = "00000000"#集計を開始する日付
    edate = "99999999"#集計を終了する日付

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
            print(files[select] + "でよろしいですか？[y/n]")
            if input() == "y":
                for i in select:
                    Filenames.append(files[int(i)])

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

    print("どちらの解析を行いますか？")
    print("[t]各時間帯毎のアクセス件数を知りたい")
    print("[h]リモートホスト別のアクセス件数知りたい")
    analysisType = ""
    ans = input()
    if ans =="t":
        analysisType = "t"
    elif ans =="h":
        analysisType = "h"





    ##期間の指定
    print("集計を開始する日付を指定しますか？[y/n]")
    ans = input()
    if ans == "y":
        print("集計を開始する日付をyyyymmddで入力してください(例：1970年1月1日 -> 19700101)")
        sdate = input()

    print("集計を終了する日付を指定しますか？[y/n]")
    ans = input()
    if ans == "y":
        print("集計を終了する日付をyyyymmddで入力してください(例：1970年1月1日 -> 19700101)")
        edate = input()

    if int(sdate)>int(edate):
        print("期間が不正です。")

    print(sdate + "から" + edate + "の期間で集計を行います。")

    print("出力ファイル名を指定しますか？[y/n]（指定しない場合はexport.csvとして出力します。）")
    ans = input()

    ex_file = "export.csv"
    if ans == "y":
        print("出力ファイル名を入力してください")
        ex_file = input()


    if analysisType == "t":
        analysis.time(Filenames, sdate, edate, ex_file)

    elif analysisType == "h":
        analysis.host(Filenames, sdate, edate, ex_file)


if __name__ == '__main__':
    main()
