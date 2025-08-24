import time 
import sys

def parse_version(v):
    return tuple(map(int, v.split(".")))

enter_boot = "" 
enter_ai = ""
this_py_version = "1.0.4"
recommended_py_version = "1.0.6"
user_finish = ["終了", "特にない", "特になし", "もう大丈夫"]
ai_mode = "basic"

def run():
    time.sleep(0.2)  # 起動してる感だけ出す

def progress_bar(duration=2.0, steps=40):
    print("ai.pyを読み込み中..." )
    sys.stdout.write("[")  # 左枠
    sys.stdout.flush()
    for i in range(steps):
        time.sleep(duration / steps)
        sys.stdout.write("■")
        sys.stdout.flush()
    sys.stdout.write("]")  # 右枠
    sys.stdout.flush()

    percent = int((i + 1) / steps * 100)
    print(f" {percent}%")
    print("読み込み完了")

run()
progress_bar()

def progress_bar(duration=2.0, steps=40):
    print("バージョンを確認中...")
    sys.stdout.write("[")  # 左枠
    sys.stdout.flush()
    for i in range(steps):
        time.sleep(duration / steps)
        sys.stdout.write("■")
        sys.stdout.flush()
    sys.stdout.write("]")  # 右枠
    sys.stdout.flush()
    percent = int((i + 1) / steps * 100)
    print(f" {percent}%")

run()
progress_bar()

if parse_version(this_py_version) < parse_version(recommended_py_version):
    print(f"おすすめのバージョンは {recommended_py_version} です。このバージョンは更新されていないのでお勧めしません。")
    print(f"現在のバージョンは {this_py_version} です。それでも続けますか？続ける場合はEnterキーを押してください。")
    enter_boot = input("")

if enter_boot != "":
    time.sleep(1)
    exit()
else:
    print("バージョン確認完了")

def progress_bar(duration=2.0, steps=40):
    print("AIを初期化中...")
    sys.stdout.write("[")  # 左枠
    sys.stdout.flush()
    for i in range(steps):
        time.sleep(duration / steps)
        sys.stdout.write("■")
        sys.stdout.flush()
    sys.stdout.write("]")  # 右枠
    sys.stdout.flush()

    percent = int((i + 1) / steps * 100)
    print(f" {percent}%")
    print("AI初期化完了")

run()
progress_bar()

print("AIを起動中...")
time.sleep(1.5)
print("AIが起動しました。続行するにはEnterキーを押してください...")
enter_ai = input("")
if enter_ai == "":
    print("Pythonで多用する基本コード復習用のAIです。知りたいコードのキーワードを入力してください。(print, input, import etc...)")

while True:
    if ai_mode == "basic":
        user_please = input("知りたいコード: ")
        if user_please in user_finish:
            print("わかりました。では困ったらまた呼び出してください!")
            print("AIを終了中...")
            time.sleep(2)
            break
        elif user_please == "print":
            print("printは、コンソールに文字列や変数の値を表示するために使用します。")
            print("例: print('Hello, World!')")
            print("使い方： print('表示したい内容')")
        elif user_please == "input":
            print("inputは、ユーザーからの入力を受け取るために使用します。")
            print("例: user_input = input('何か入力してください: ')")
            print("使い方： input('ユーザーに打ってほしい内容')")
        elif user_please == "import":
            print("importは、他のモジュールやライブラリを読み込むために使用します。")
            print("例: import math")
            print("使い方： import モジュール名")
        elif user_please == "if":
            print("ifは、条件に応じて処理を分岐させるために使用します。")
            print("例: if x > 0:")
            print("使い方： if 条件(条件はほとんどは自分で作った変数とそれに対応する数字が入る):")
        elif user_please == "for":
            print("forは、繰り返し処理を行うために使用します。")
            print("例: for i in range(5):")
            print("使い方： for 変数 in range(繰り返し回数):")
        elif user_please == "while":
            print("whileは、条件が真である限り繰り返し処理を行うために使用します。")
            print("例: while x < 5:")
            print("使い方： while 条件(繰り返しを終了する場合はbreakを使う):")
        elif user_please == "break":
            print("breakは、ループを強制的に終了させるために使用します。")
            print("例: for i in range(10):\n    if i == 5:\n        break")
            print("使い方： if 条件:\n    break")
        elif user_please == "continue":
            print("continueは、ループの現在の反復をスキップして次の反復に進むために使用します。")
            print("例: for i in range(10):\n    if i == 5:\n        continue")
            print("使い方： if 条件:\n    continue")
        elif user_please == "return":
            print("returnは、関数から値を返すために使用します。")
            print("例: return 値")
            print("使い方： return 戻り値")
        elif user_please == "pass":
            print("passは、何もしないことを明示するために使用します。")
            print("例: pass")
            print("使い方： pass")
        elif user_please == "else":
            print("else、elif(else ifの略)は、if文の条件が偽である場合に実行される処理を定義するために使用します。")
            print("elseの例: if x > 0:\n    print('Positive')\nelse:\n    print('Non-positive')")
            print("elifの例: if x > 0:\n    print('Positive')\nelif x < 0:\n    print('Negative')\nelse:\n    print('Zero')")
            print("elseの使い方： if 条件:\n    処理\nelse:\n    処理")
            print("elifの使い方： if 条件:\n    処理\nelif 条件:\n    処理\nelse:\n    処理")
        elif user_please == "int" or user_please == "int()":
            print("int()は、文字列や浮動小数点を整数に変換するために使用します。")
            print("例: x = int("")")
            print("使い方: int(変換したい値)")
        elif user_please == "str" or user_please == "str()":
            print("str()は、数値やほかの肩を文字列に変換するために使用します。")
            print("例: s = str(100)")
            print("使い方: str(変換したい値)")
        elif user_please == "float" or user_please == "float()":
            print("float()は、整数や文字列を浮動小数点に変換するために使用します。")
            print("f = float(\"3.14\")")
            print("使い方: float(変換したい値)")
        elif user_please == "list":
            print("listは、リスト操作に必要はリストそのものを作成するために使用します。")
            print("例: example_list = list((1, 2, 3))")
            print("使い方: list(リストに入れたい数字)")
        elif user_please == "len" or user_please == "len()":
            print("len()は、オブジェクト(ここではリストの長さ)の長さを返す(出力)ために使用します。")
            print("例: len([1, 2, 3]) # ここでは3が出力される")
            print("使い方: len(オブジェクト)")
        elif user_please == "append" or user_please == "append()":
            print("append()は、inputなどで受け取った要素をリストに追加したいときに使用します。")
            print("例: example.append(4)")
            print("使い方: リスト.append(要素)")
        elif user_please == "remove" or user_please == "remove()":
            print("remove()は、inputなどで受け取った要素をリストにその要素が入っているときに限りリストから削除します。")
            print("例: example_list.remove(2)")
            print("使い方: リスト.remove(要素)")
        elif user_please == "dict":
            print("dictは、辞書(キーと値のペア)を作成するときに使用します。")
            print("例: example_dict = dict(name=\"Alice\", age=25)")
            print("使い方: 辞書.get(キー, デフォルト値)")
        elif user_please == "get" or user_please == "get()":
            print("get()は、その辞書に登録されていて、なおかつ()のなかにあるキーに対応する値を取得するときに使用します。(キーが存在しないときはNoneを返す)")
            print("例: example_dict.get(\"name\")")
            print("使い方: 辞書.get(キー, デフォルト値)")
        elif user_please == "keys" or user_please == "keys()":
            print("keys()は、その辞書に登録されているすべてのキーを取得するときに使用します。")
            print("例: example_dict.keys()")
            print("使い方: 辞書.keys()")
        elif user_please == "def":
            print("defは、関数そのものを定義する時に使用します。")
            print("例: \ndef greet(): \nprint(\"Hello,world\")")
            print("使い方: def 関数名(引数):")
        elif user_please == "lambda":
            print("lambdaは、名前なし関数を使いたいときに使用します。")
            print("例: square = lambda x: x ** 2")
            print("使い方: lambda 引数: 式")
        elif user_please == "open" or user_please == "open()":
            print("open()は、ファイル操作を行うファイルを開くときに使用します。モード指定可能です。")
            print("例: f = open(\"data.txt\", \"r\")")
            print("使い方: open(ファイル名, モード)")
        elif user_please == "read" or user_please == "read()":
            print("read()は、読み込んだファイルの内容を読み取るときに使用します。")
            print("例: data = f.read()")
            print("使い方: ファイルオブジェクト.read()")
        elif user_please == "write" or user_please == "write()":
            print("write()は、openで読み込んだファイルに文字列を書き込む時に使用します。")
            print("例: f.write(\"Hello\")")
            print("使い方: ファイルオブジェクト.write(文字列)")
        elif user_please == "with":
            print("withは、ファイル操作の終了を自動的に処理するコードです。")
            print("例: \nwith open(\"data.txt\", \"r\") as f: \n    data  f.read()")
            print("使い方: 上記の通り")
        elif user_please == "モード切り替え":
            print("わかりました。特定の数字を入力してください。(数字に関してはupdatelog.txtを参照)")
            user_mode = input("数字： ")
            if user_mode == "1":
                ai_mode = "basic"
                print("基礎文法モードに切り替えました。")
            elif user_mode == "2":
                ai_mode = "detailed"
                print("詳細説明モードに切り替えました。")
            elif user_mode == "3":
                ai_mode = "module"
                print("モジュールモードに切り替えました。")
        else:
            print("そのコードまたは説明は用意されていません。お手数をおかけいたしますがご自分で検索をお願いいたします")
    elif ai_mode == "detailed":
        user_explanation = input("説明が欲しいコード: ")
        if user_explanation in user_finish:
            print("わかりました。では困ったらまた呼び出してください!")
            print("AIを終了中...")
            time.sleep(2)
            break
        elif user_explanation == "print":
            print("printは、コンソールに文字列や変数の値を表示するために使用します。")
            print("例: print('Hello, World!')")
            print("使い方： print('表示したい内容')")
            print("使用頻度：非常に高い\nモジュールのあとに使うことが多い")
        elif user_explanation == "input":
            print("inputは、ユーザーからの入力を受け取るために使用します。")
            print("例: user_input = input('何か入力してください: ')")
            print("使い方： input('ユーザーに打ってほしい内容')")
            print("使用頻度：ほとんどの.pyで使う\nユーザーからの入力を受け取る場面でよく使われる。(inputの派生としてint(input())などもある)\nint(input())はユーザーからの入力を数値変換する際に使う。")
        elif user_explanation == "import":
            print("importは、他のモジュールやライブラリを読み込むために使用します。")
            print("例: import math")
            print("使い方： import モジュール名")
            print("使用頻度：ほとんどの.pyで使う\ntimeやos、mathなどなにかしらの動きをさせる元を読み込む際に使われる。\n例として出たtimeは時間を扱う際に必須のモジュールである。")
        elif user_explanation == "if":
            print("ifは、条件に応じて処理を分岐させるために使用します。")
            print("例: if x > 0:")
            print("使い方： if 条件(条件はほとんどは自分で作った変数とそれに対応する数字が入る):")
            print("使用頻度：非常に高い\n対話や条件分岐、AI作成を行う際に必須のコードである。\nif文の後にelif文(else ifの略)を使うことで、さらに細かい条件分岐が可能になる。")
        elif user_explanation == "for":
            print("forは、繰り返し処理を行うために使用します。")
            print("例: for i in range(5):")
            print("使い方： for 変数 in range(繰り返し回数):")
            print("使用頻度：あまり高くない\n繰り返し処理を行いたい場面でよく使われる。")
        elif user_explanation == "while":
            print("whileは、条件が真である限り繰り返し処理を行うために使用します。")
            print("例: while x < 5:")
            print("使い方： while 条件(繰り返しを終了する場合はbreakを使う):")
            print("使用頻度：高い\nループ処理を行う際に使用される。forよりも簡単。\nただし、無限ループに注意が必要である。")
        elif user_explanation == "break":
            print("breakは、ループを強制的に終了させるために使用します。")
            print("例: for i in range(10):\n    if i == 5:\n        break")
            print("使い方： if 条件:\n    break")
            print("使用頻度：あまり高くない(繰り返しがある場合は非常に高い)\nループ処理を強制的に終了させる際に使用される。")
        elif user_explanation == "continue":
            print("continueは、ループの現在の反復をスキップして次の反復に移るために使用します。")
            print("例: for i in range(10):\n    if i == 5:\n        continue")
            print("使い方： if 条件:\n    continue")
            print("使用頻度：あまり高くない(繰り返しがある場合は非常に高い)\nループの現在の反復をスキップして次の反復に移る際に使用される。")
        elif user_explanation == "pass":
            print("passは、何もしないことを明示するために使用します。")
            print("例: if 条件:\n    pass")
            print("使い方： if 条件:\n    pass")
            print("使用頻度：あまり高くない\n処理を一時的にスキップしたい場合に使用される。")
        elif user_explanation == "return":
            print("returnは、関数から値を返すために使用します。")
            print("例: return x + 1")
            print("使い方： return 戻したい値")
            print("使用頻度：関数を使うならほとんどの.pyで使う\n関数を定義した際に、処理結果を返すために使用される。\nwhileやforと似たような使い方をするが、returnは関数の中でしか使えない。")
        elif user_explanation == "else":
            print("elseは、if文の条件が偽である場合に実行される処理を定義するために使用します。")
            print("例: if x > 0:\n    print('Positive')\nelse:\n    print('Non-positive')")
            print("使い方： if 条件:\n    処理\nelse:\n    処理")
            print("使用頻度：非常に高い\nifとセットで使う場合がほとんど。\nより複雑な条件分岐を使う際に使用される。\nelif文(else ifの略)を使うことで、さらに細かい条件分岐が可能になる。")
        elif user_explanation == "math":
            print("mathモジュールは、数学関連の関数や定数を提供します。")
            print("例: import math")
            print("使い方： import math")
            print("使用頻度：高い\n数学的な計算を行う際に使用される。\n例えば、平方根や三角関数などの計算が可能。")
        elif user_explanation == "datetime":
            print("datetimeモジュールは、日付や時刻を扱うためのクラスや関数を提供します。")
            print("例: import datetime")
            print("使い方： import datetime")
            print("使用頻度：高い\n日付や時刻の操作を行う際に使用される。\n例えば、現在の日付や時刻の取得、日付の計算などが可能。")
        elif user_explanation == "random":
            print("randomモジュールは、ランダムな数字を生成するための関数を提供します。")
            print("例: import random")
            print("使い方： import random")
            print("使用頻度：高い\nランダムな値が必要な場面で使用される。\n例えば、サイコロの目を生成する場合やstepを使用するときなど。")
        elif user_explanation == "os":
            print("osモジュールは、オペレーティングシステム(要はパソコン本体)との対話を行うための機能を提供します。")
            print("例: import os")
            print("使い方： import os")
            print("使用頻度：高い\nファイルやディレクトリの操作を行う際に使用される。\n例えば、ファイルの削除やディレクトリの作成などが可能。")
        elif user_explanation == "sys":
            print("sysモジュールは、Pythonの実行環境に関する情報を提供します。")
            print("例: import sys")
            print("使い方： import sys")
            print("使用頻度：高い\nPythonの実行環境に関する情報を取得する際に使用される。\n例えば、コマンドライン引数の取得や標準入出力の操作などが可能。")
        elif user_explanation == "re":
            print("reモジュールは、正規表現を使用して文字列の処理を行うための関数を提供します。")
            print("例: import re")
            print("使い方： import re")
            print("使用頻度：まあまあ\n文字列のパターンマッチングや置換を行う際に使用される。")
        elif user_explanation == "json":
            print("jsonモジュールは、JSON形式のデータを扱うための関数を提供します。")
            print("例: import json")
            print("使い方： import json")
            print("使用頻度：状況による\nJSONデータの読み書きを行う際に使用される。")
        elif user_explanation == "time":
            print("timeモジュールは、時間に関する機能を提供します。")
            print("例: import time")
            print("使い方： import time")
            print("使用頻度：高い\n時間の計測や待機を行う際に使用される。")
        elif user_explanation == "collections":
            print("collectionsモジュールは、データ構造を拡張するための関数を提供します。")
            print("例: import collections")
            print("使い方： import collections")
            print("使用頻度：高い\nリストや辞書などのデータ構造を扱う際に使用される。")
        elif user_explanation == "itertools":
            print("itertoolsモジュールは、AIの操作を強化するための関数を提供します。")
            print("例: import itertools")
            print("使い方： import itertools")
            print("使用頻度：高い\nAIの操作をより強化したい際に使用される。")
        elif user_explanation == "subprocess":
            print("subprocessモジュールは、外部プロセスを生成し、制御するための関数を提供します。")
            print("例: import subprocess")
            print("使い方： import subprocess")
            print("使用頻度：高い\n外部コマンドの実行やプロセスの管理を行う際に使用される。")
        elif user_explanation == "int" or user_explanation == "int()":
            print("int()は、文字列や浮動小数点を整数に変換するために使用します。")
            print("例: x = int(\"5\")")
            print("使い方: int(変換したい値)")
            print("使用頻度: 高い")
        elif user_explanation == "str" or user_explanation == "str()":
            print("str()は、数値やほかの型を文字列に変換するために使用します。")
            print("例: s = str(100)")
            print("使い方: str(変換したい値)")
            print("使用頻度: 高い")
        elif user_explanation == "float" or user_explanation == "float()":
            print("float()は、整数や文字列を浮動小数点に変換するために使用します。")
            print("例: f = float(\"3.14\")")
            print("使い方: float(変換したい値)")
            print("使用頻度: 中くらい")
        elif user_explanation == "list":
            print("listは、リスト操作に必要なリストそのものを作成するために使用します。")
            print("例: example_list = list((1, 2, 3))")
            print("使い方: list(リストに入れたい値)")
            print("使用頻度: 高い")
        elif user_explanation == "len" or user_explanation == "len()":
            print("len()は、オブジェクト(ここではリストなど)の長さを返すために使用します。")
            print("例: len([1, 2, 3]) # ここでは3が出力される")
            print("使い方: len(オブジェクト)")
            print("使用頻度: 高い")
        elif user_explanation == "append" or user_explanation == "append()":
            print("append()は、inputなどで受け取った要素をリストに追加したいときに使用します。")
            print("例: example.append(4)")
            print("使い方: リスト.append(要素)")
            print("使用頻度: 高い")
        elif user_explanation == "remove" or user_explanation == "remove()":
            print("remove()は、inputなどで受け取った要素をリストにその要素が入っているときに限りリストから削除します。")
            print("例: example_list.remove(2)")
            print("使い方: リスト.remove(要素)")
            print("使用頻度: 中くらい")
        elif user_explanation == "dict":
            print("dictは、辞書(キーと値のペア)を作成するときに使用します。")
            print("例: example_dict = dict(name=\"Alice\", age=25)")
            print("使い方: dict(キー=値)")
            print("使用頻度: 高い")
        elif user_explanation == "get" or user_explanation == "get()":
            print("get()は、その辞書に登録されていて、なおかつ()のなかにあるキーに対応する値を取得するときに使用します。(キーが存在しないときはNoneを返す)")
            print("例: example_dict.get(\"name\")")
            print("使い方: 辞書.get(キー, デフォルト値)")
            print("使用頻度: 高い")
        elif user_explanation == "keys" or user_explanation == "keys()":
            print("keys()は、その辞書に登録されているすべてのキーを取得するときに使用します。")
            print("例: example_dict.keys()")
            print("使い方: 辞書.keys()")
            print("使用頻度: 中くらい")
        elif user_explanation == "def":
            print("defは、関数そのものを定義する時に使用します。")
            print("例: \ndef greet(): \n    print(\"Hello,world\")")
            print("使い方: def 関数名(引数):")
            print("使用頻度: 高い")
        elif user_explanation == "lambda":
            print("lambdaは、名前なし関数を使いたいときに使用します。")
            print("例: square = lambda x: x ** 2")
            print("使い方: lambda 引数: 式")
            print("使用頻度: 中くらい")
        elif user_explanation == "open" or user_explanation == "open()":
            print("open()は、ファイル操作を行うファイルを開くときに使用します。モード指定可能です。")
            print("例: f = open(\"data.txt\", \"r\")")
            print("使い方: open(ファイル名, モード)")
            print("使用頻度: 高い")
        elif user_explanation == "read" or user_explanation == "read()":
            print("read()は、読み込んだファイルの内容を読み取るときに使用します。")
            print("例: data = f.read()")
            print("使い方: ファイルオブジェクト.read()")
            print("使用頻度: 高い")
        elif user_explanation == "write" or user_explanation == "write()":
            print("write()は、openで読み込んだファイルに文字列を書き込む時に使用します。")
            print("例: f.write(\"Hello\")")
            print("使い方: ファイルオブジェクト.write(文字列)")
            print("使用頻度: 高い")
        elif user_explanation == "with":
            print("withは、ファイル操作の終了を自動的に処理するコードです。")
            print("例: \nwith open(\"data.txt\", \"r\") as f: \n    data = f.read()")
            print("使い方: with open(...) as 変数:")
            print("使用頻度: 高い")
        elif user_explanation == "モード切り替え":
            print("わかりました。特定の数字を入力してください。(数字に関してはupdatelog.txtを参照)")
            user_mode = input("数字： ")
            if user_mode == "1":
                ai_mode = "basic"
                print("基礎文法モードに切り替えました。")
            elif user_mode == "2":
                ai_mode = "detailed"
                print("詳細説明モードに切り替えました。")
            elif user_mode == "3":
                ai_mode = "module"
                print("モジュールモードに切り替えました。")
        else:
            print("そのコードまたは説明は用意されていません。お手数をおかけいたしますがご自分で検索をお願いいたします")
    elif ai_mode == "module":
        user_module = input("知りたいモジュール:")
        if user_module in user_finish:
            print("わかりました。では困ったらまた呼び出してください!")
            print("AIを終了中...")
            time.sleep(2)
            break
        elif user_module == "math":
            print("mathモジュールは、数学関連の関数や定数を提供します。")
            print("例: import math")
            print("使い方： import math")
        elif user_module == "datetime":
            print("datetimeモジュールは、日付や時刻を扱うためのクラスや関数を提供します。")
            print("例: import datetime")
            print("使い方： import datetime")
        elif user_module == "random":
            print("randomモジュールは、ランダムな数字を生成するための関数を提供します。")
            print("例: import random")
            print("使い方： import random")
        elif user_module == "os":
            print("osモジュールは、オペレーティングシステム(要はパソコン本体)との対話を行うための機能を提供します。")
            print("例: import os")
            print("使い方： import os")
        elif user_module == "sys":
            print("sysモジュールは、Pythonの実行環境に関する情報を提供します。")
            print("例: import sys")
            print("使い方： import sys")
        elif user_module == "re":
            print("reモジュールは、正規表現を使用して文字列の処理を行うための関数を提供します。")
            print("例: import re")
            print("使い方： import re")
        elif user_module == "json":
            print("jsonモジュールは、JSON形式のデータを扱うための関数を提供します。")
            print("例: import json")
            print("使い方： import json")
        elif user_module == "time":
            print("timeモジュールは、時間に関する機能を提供します。")
            print("例: import time")
            print("使い方： import time")
        elif user_module == "collections":
            print("collectionsモジュールは、データ構造を拡張するための関数を提供します。")
            print("例: import collections")
            print("使い方： import collections")
        elif user_module == "itertools":
            print("itertoolsモジュールは、AIの操作を強化するための関数を提供します。")
            print("例: import itertools")
            print("使い方： import itertools")
        elif user_module == "subprocess":
            print("subprocessモジュールは、外部プログラムを実行するための関数を提供します。")
            print("例: import subprocess")
            print("使い方： import subprocess")
        elif user_module == "モード切り替え":
            print("わかりました。特定の数字を入力してください。(数字に関してはupdatelog.txtを参照)")
            user_mode = input("数字： ")
            if user_mode == "1":
                ai_mode = "basic"
                print("基礎文法モードに切り替えました。")
            elif user_mode == "2":
                ai_mode = "detailed"
                print("詳細説明モードに切り替えました。")
            elif user_mode == "3":
                ai_mode = "module"
                print("モジュールモードに切り替えました。")
        else:
            print("そのモジュールは用意されていません。お手数をおかけいたしますがご自分で検索をお願いいたします")