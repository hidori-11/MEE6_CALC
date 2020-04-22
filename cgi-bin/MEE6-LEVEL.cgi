#!/usr/local/bin/python3

# ↑pythonを実行するために必要なおまじない的なサムシング
# 文字の中身は環境によって変わる　こいつのせいで実行できねぇってトラブルも多い(3敗)

# python標準ライブラリのインポート C++で言うinclude
import cgi
import sys
import io
import math

# HTTPサーバー上で動くので標準出力の文字コードをUTF-8に指定
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# HTMLヘッダの指定とか
print("Content-Type: text/html;charset=utf-8\n\n")

# 入力フォームから送信されてきたデータを受け取る
form = cgi.FieldStorage()

try:  # try句　こいつの中で例外(エラー)が上がるとexcept句に飛ぶ

    now = float(form["now"].value)
    total = float(form["total"].value)

    # 入力フォームから受け取ったデータのうち、
    # expというデータの値(元はstring)をfloatに変換して1000倍して格納
    exp = (total - now) * 1000

    # 入力フォームのexpというデータの値(string)を
    # "."という文字で分割する(exp_periodは配列 input"0.05"なら["0"."05"]みたいになる)
    exp_period = form["now"].value.split(".")

    # 小数点の桁数ごとにlow.highの範囲？を変える
    # exp_period配列の1番目(pythonの配列は0番目が存在する)を参照し
    # Len関数で文字数を取得
    if(len(exp_period[1]) == 1):

        lowr = math.ceil((exp - 50) / 37)
        highr = math.ceil((exp + 49) / 22)
        aver = math.ceil(exp * 2 / 59)

    elif(len(exp_period[1]) == 2):

        lowr = math.ceil((exp - 5) / 37)
        highr = math.ceil((exp + 4) / 22)
        aver = math.ceil(exp * 2 / 59)

    elif(len(exp_period[1]) == 3):
        lowr = math.ceil(exp / 37)
        highr = math.ceil(exp / 22)
        aver = math.ceil(exp * 2 / 59)

    else:
        # 小数点以下1~3桁以外のときはエラーとして処理させる
        # raiseすると例外をあげられる
        raise ValueError

    # exp=0のときはlowも0にしとく
    if exp == 0:
        lowr = 0

    # 結果書き出し
    print("<html><body><p>")
    print("min=あと" + str(int(lowr)) + "コメ、最短所要時間" + str(int(lowr / 60)) + "h" + str(int(lowr % 60)) + "m <br>")
    print("max=あと" + str(int(highr)) + "コメ、最長所要時間" + str(int(highr / 60)) + "h" + str(int(highr % 60)) + "m <br>")
    print("ave=あと" + str(int(aver)) + "コメ、平均所要時間" + str(int(aver / 60)) + "h" + str(int(aver % 60)) + "m <br>")

    if aver <= 40:
        print("あと少し!  fight!")

    if aver > 100:
        print("先は長い!  fight!")
    print("</p></body></html>")
# エラー起きたときはココに飛ぶ
except:
    print("<html><body><p>")
    print("入力値が不正です <br>")
    print("</p></body></html>")

