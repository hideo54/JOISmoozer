#JOISmoozer

##概要
JOIで出力ファイル出しまくるのはとても面倒ですよね。
このプログラムは、与えられた入力ファイルを元に実行ファイルを実行し出力ファイルを生成するといったことを自動で行ってくれます。
JOI予選頑張りましょう。

##バージョン
Ver 1.0

##動作環境
* Python 2.6.*
* Python 2.7.*
format関数を多用しているので、2.6以降が必須です。

###動作確認済み環境
Python 2.7.6 on OS X 10.10.1 (2014/7/19)

##動かし方
1. ソースコード内の5-8行目を、好みの設定に変更する。
デフォルトの設定に習って、問題番号を{prb}, 入力例を{num}としたフォーマットをすること。
2. C, Python以外を使用したい場合は、19行目の後ろに、elifを利用して、好みの設定を追加する。(追加したものはforkしてくださると僕が喜びます。)
3. pythonでプログラムを実行。問題番号を入力して、エラーなく完了したら、成功です。
エラーが発生した場合、設定が原因の場合と、元の実行ファイルが原因の場合が考えられます。エラーを読んで判断してください。

##連絡先
Twitter… [@hideo54](https://www.twitter.com/hideo54)

Email… hideo54.pub@gmail.com

バグがあればご報告ください。
