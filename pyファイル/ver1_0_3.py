import time 
import sys

def parse_version(v):
    return tuple(map(int, v.split(".")))

enter_boot = "" 
enter_ai = ""
this_py_version = "1.0.3"
recommended_py_version = "1.0.4"
user_finish = ["終了", "特にない", "特になし", "もう大丈夫"]
ai_mode = "basic"

def run():
    time.sleep(0.2)  # 起動してる感だけ出す

def progress_bar(duration=2.0, steps=40):
    print("ai.pyを読み込み中...")
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
            print("print関数は、コンソールに文字列や変数の値を表示するために使用します。")
            print("例: print('Hello, World!')")
            print("使い方： print('表示したい内容')")
        elif user_please == "input":
            print("input関数は、ユーザーからの入力を受け取るために使用します。")
            print("例: user_input = input('何か入力してください: ')")
            print("使い方： input('ユーザーに打ってほしい内容')")
        elif user_please == "import":
            print("import文は、他のモジュールやライブラリを読み込むために使用します。")
            print("例: import math")
            print("使い方： import モジュール名")
        elif user_please == "if":
            print("if文は、条件に応じて処理を分岐させるために使用します。")
            print("例: if x > 0:")
            print("使い方： if 条件(条件はほとんどは自分で作った変数とそれに対応する数字が入る):")
        elif user_please == "for":
            print("for文は、繰り返し処理を行うために使用します。")
            print("例: for i in range(5):")
            print("使い方： for 変数 in range(繰り返し回数):")
        elif user_please == "while":
            print("while文は、条件が真である限り繰り返し処理を行うために使用します。")
            print("例: while x < 5:")
            print("使い方： while 条件(繰り返しを終了する場合はbreakを使う):")
        elif user_please == "モード切り替え":
            print("わかりました。特定の数字を入力してください。(数字に関してはupdatelog.txtを参照)")
            user_mode = input("数字： ")
            if user_mode == "1":
                ai_mode = "basic"
                print("基本コードモードに切り替えました。")
            elif user_mode == "2":
                ai_mode = "auxiliary"
                print("補助系コードモードに切り替えました。")
            elif user_mode == "3":
                ai_mode = "detailed"
                print("詳細説明モードに切り替えました。")
            elif user_mode == "4":
                ai_mode = "module"
                print("モジュールモードに切り替えました。")
            else:
                print("無効なモードか、現在追加されていないモードです。")
        else:
            print("そのコードまたは説明は用意されていません。お手数をおかけいたしますがご自分で検索をお願いいたします")
    elif ai_mode == "auxiliary":
        user_please_auxiliary = input("知りたい補助系コード: ")
        if user_please_auxiliary in user_finish:
            print("わかりました。では困ったらまた呼び出してください!")
            print("AIを終了中...")
            time.sleep(2)
            break
        elif user_please_auxiliary == "break":
            print("break文は、ループを強制的に終了させるために使用します。")
            print("例: for i in range(10):\n    if i == 5:\n        break")
            print("使い方： if 条件:\n    break")
        elif user_please_auxiliary == "continue":
            print("continue文は、ループの現在の反復をスキップして次の反復に進むために使用します。")
            print("例: for i in range(10):\n    if i == 5:\n        continue")
            print("使い方： if 条件:\n    continue")
        elif user_please_auxiliary == "return":
            print("return文は、関数から値を返すために使用します。")
            print("例: return 値")
            print("使い方： return 戻り値")
        elif user_please_auxiliary == "pass":
            print("pass文は、何もしないことを明示するために使用します。")
            print("例: pass")
            print("使い方： pass")
        elif user_please_auxiliary == "else":
            print("else文、elif文(else ifの略)は、if文の条件が偽である場合に実行される処理を定義するために使用します。")
            print("else文の例: if x > 0:\n    print('Positive')\nelse:\n    print('Non-positive')")
            print("elif文の例: if x > 0:\n    print('Positive')\nelif x < 0:\n    print('Negative')\nelse:\n    print('Zero')")
            print("else文の使い方： if 条件:\n    処理\nelse:\n    処理")
            print("elif文の使い方： if 条件:\n    処理\nelif 条件:\n    処理\nelse:\n    処理")
        elif user_please_auxiliary == "モード切り替え":
            print("わかりました。特定の数字を入力してください。(数字に関してはupdatelog.txtを参照)")
            user_mode = input("数字： ")
            if user_mode == "1":
                ai_mode = "basic"
                print("基本コードモードに切り替えました。")
            elif user_mode == "2":
                ai_mode = "auxiliary"
                print("補助系コードモードに切り替えました。")
            elif user_mode == "3":
                ai_mode = "detailed"
                print("詳細説明モードに切り替えました。")
            elif user_mode == "4":
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
            print("print関数は、コンソールに文字列や変数の値を表示するために使用します。")
            print("例: print('Hello, World!')")
            print("使い方： print('表示したい内容')")
            print("使用頻度：非常に高い\nモジュールのあとに使うことが多い")
        elif user_explanation == "input":
            print("input関数は、ユーザーからの入力を受け取るために使用します。")
            print("例: user_input = input('何か入力してください: ')")
            print("使い方： input('ユーザーに打ってほしい内容')")
            print("使用頻度：ほとんどの.pyで使う\nユーザーからの入力を受け取る場面でよく使われる。(inputの派生としてint(input())などもある)\nint(input())はユーザーからの入力を数値変換する際に使う。")
        elif user_explanation == "import":
            print("import文は、他のモジュールやライブラリを読み込むために使用します。")
            print("例: import math")
            print("使い方： import モジュール名")
            print("使用頻度：ほとんどの.pyで使う\ntimeやos、mathなどなにかしらの動きをさせる元を読み込む際に使われる。\n例として出たtimeは時間を扱う際に必須のモジュールである。")
        elif user_explanation == "if":
            print("if文は、条件に応じて処理を分岐させるために使用します。")
            print("例: if x > 0:")
            print("使い方： if 条件(条件はほとんどは自分で作った変数とそれに対応する数字が入る):")
            print("使用頻度：非常に高い\n対話や条件分岐、AI作成を行う際に必須のコードである。\nif文の後にelif文(else ifの略)を使うことで、さらに細かい条件分岐が可能になる。")
        elif user_explanation == "for":
            print("for文は、繰り返し処理を行うために使用します。")
            print("例: for i in range(5):")
            print("使い方： for 変数 in range(繰り返し回数):")
            print("使用頻度：あまり高くない\n繰り返し処理を行いたい場面でよく使われる。")
        elif user_explanation == "while":
            print("while文は、条件が真である限り繰り返し処理を行うために使用します。")
            print("例: while x < 5:")
            print("使い方： while 条件(繰り返しを終了する場合はbreakを使う):")
            print("使用頻度：高い\nループ処理を行う際に使用される。forよりも簡単。\nただし、無限ループに注意が必要である。")
        elif user_explanation == "break":
            print("break文は、ループを強制的に終了させるために使用します。")
            print("例: for i in range(10):\n    if i == 5:\n        break")
            print("使い方： if 条件:\n    break")
            print("使用頻度：あまり高くない(繰り返しがある場合は非常に高い)\nループ処理を強制的に終了させる際に使用される。")
        elif user_explanation == "continue":
            print("continue文は、ループの現在の反復をスキップして次の反復に移るために使用します。")
            print("例: for i in range(10):\n    if i == 5:\n        continue")
            print("使い方： if 条件:\n    continue")
            print("使用頻度：あまり高くない(繰り返しがある場合は非常に高い)\nループの現在の反復をスキップして次の反復に移る際に使用される。")
        elif user_explanation == "pass":
            print("pass文は、何もしないことを明示するために使用します。")
            print("例: if 条件:\n    pass")
            print("使い方： if 条件:\n    pass")
            print("使用頻度：あまり高くない\n処理を一時的にスキップしたい場合に使用される。")
        elif user_explanation == "return":
            print("return文は、関数から値を返すために使用します。")
            print("例: return x + 1")
            print("使い方： return 戻したい値")
            print("使用頻度：関数を使うならほとんどの.pyで使う\n関数を定義した際に、処理結果を返すために使用される。\nwhileやforと似たような使い方をするが、returnは関数の中でしか使えない。")
        elif user_explanation == "else":
            print("else文は、if文の条件が偽である場合に実行される処理を定義するために使用します。")
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
        elif user_explanation == "モード切り替え":
            print("わかりました。特定の数字を入力してください。(数字に関してはupdatelog.txtを参照)")
            user_mode = input("数字： ")
            if user_mode == "1":
                ai_mode = "basic"
                print("基本コードモードに切り替えました。")
            elif user_mode == "2":
                ai_mode = "auxiliary"
                print("補助系コードモードに切り替えました。")
            elif user_mode == "3":
                ai_mode = "detailed"
                print("詳細説明モードに切り替えました。")
            elif user_mode == "4":
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
                print("基本コードモードに切り替えました。")
            elif user_mode == "2":
                ai_mode = "auxiliary"
                print("補助系コードモードに切り替えました。")
            elif user_mode == "3":
                ai_mode = "detailed"
                print("詳細説明モードに切り替えました。")
            elif user_mode == "4":
                ai_mode = "module"
                print("モジュールモードに切り替えました。")
        else:
            print("そのモジュールは用意されていません。お手数をおかけいたしますがご自分で検索をお願いいたします")