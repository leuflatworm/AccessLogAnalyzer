import os


def main():
    list = {}



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
        print("対象とするファイルを選択してください")
        files = os.listdir("targets")
        for i in range(len(files)):
            if files[i] in Filenames:
                print("[" + str(i) + "]" + files[i] + " selected!!!")
            else:
                print("[" + str(i) + "]" + files[i])

        select = int(input())
        print(files[select] + "でよろしいですか？[y/n]")
        if input() == "y":
            Filenames.append(files[select])
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


if __name__ == '__main__':
    main()
