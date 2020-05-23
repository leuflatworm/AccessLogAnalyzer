# AccessLogAnalyzer
Apacheのアクセスログファイルから一時間ごとのリモートホストごとのアクセス数を比較し、多い順に出力します。 

## 依存 Dependence
python3 (python3.7.6にて動作確認済み)


## 使い方 How to use
アクセスログファイルを targets/ にコピーし、main.pyを実行 

各質問に対して[y/n]及び数値で解答することで解析を行い、結果は exports/ に出力されます。 

出力ファイルは同名ファイルが exports/ に存在した場合は追記ではなく上書きされます。 

また、以下の様にコマンドラインオプションを用いることもできます。

```
python3 main.py f=FILE_NAME sd=START_DATE(yyyymmdd) ed=END_DATE(yyyymmdd) ex=EXPORT_FILE_NAME l=SPEED_LEVEL
```

コマンドラインオプションを用いた場合は入力しなかったものはデフォルトの指定なしとして扱われます。


## 出力形式 Output
```
export.csv

対象ファイル："対象ファイル名1","対象ファイル名2","対象ファイル名3","対象ファイル名4",解析時期"開始(yyyymmdd)〜終了(yyyymmdd)

yyyymmdd:hh:00~hh:59, リモートホスト名_1:アクセス数, リモートホスト名_2:アクセス数, リモートホスト名_3:アクセス数,
yyyymmdd:hh:00~hh:59, リモートホスト名_1:アクセス数, リモートホスト名_2:アクセス数, リモートホスト名_3:アクセス数,
```



## 開発者向け
analysis.pyと同ファイルにあるpythonスクリプトからであれば以下のように利用できます。


```
import analysis

analysis.analysis(LOG_FILE_NAMES, START_DATE, END_DATE, EXPORT_FILE_NAME)
```

* LOG_FILE_NAMES -str型の targets/ 内のログファイル名のリスト 又はallで targets/ 内全てのファイルについて解析
* START_DATE -解析の開始する日付をyyyymmdd形式 str型の
* END_DATE -解析の終了する日付をyyyymmdd形式 str型の
* EXPORT_FILE_NAME -出力ファイル名 str型

## メモリ節約レベルについて
メモリ節約に0〜4の5段階を用意しています。このレベルは中間ファイルをどこまで分割するかの設定であり、1はほぼ分割なし、4は細かく分割を行います。0は中間ファイルを一切用いずにメモリ上のみで処理を行うので処理を一段階高速化できますが
