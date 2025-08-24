import time # timeモジュールをインポート(time.sleepで使用)

def run():
    import time
    time.sleep(0.2)  # 起動してる感だけ出す
run()  

def parse_version(v):
    return tuple(map(int, v.split(".")))

# 使う変数
enter_boot = ""
enter_ai = ""
this_py_version = "1.0.0"
recommended_py_version = "1.0.6"
user_finish = ["終了", "特にない", "特になし", "もう大丈夫"]

# 起動ログ
print("ai.pyを読み込み中...")
time.sleep(3)
print("バージョンを確認中...")
time.sleep(1.5)
# バージョンを確認
if parse_version(this_py_version) < parse_version(recommended_py_version):
    print(f"おすすめのバージョンは {recommended_py_version} です。このバージョンは更新されていないのでお勧めしません。")
    print(f"現在のバージョンは {this_py_version} です。それでも続けますか？続ける場合はEnterキーを押してください。")
    enter_boot = input("")
#バージョンが確認出来たら起動
if enter_boot != "":
    time.sleep(1)
    exit()
else:
    time.sleep(1.5)
    print("AIを初期化中...")
    time.sleep(3)
    print("AIを起動中...")
    time.sleep(3)
    print("AIが起動しました。続行するにはEnterキーを押してください...")
    enter_ai = input("")
# AI本体(上が基本コードモード、下が補助系コードモード)ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    if enter_ai == "":
        print("Pythonで多用する基本コード復習用のAIです。知りたいコードのキーワードを入力してください。(print, input, import etc...)")
    while True:
        user_please = input("知りたいコード: ")
        if user_please in user_finish:
            print("わかりました。では困ったらまた呼び出してください!")
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
        elif user_please == "補助系コードモード":
            print("わかりました。では補助系コードモードに移行します")
            print("補助系コードモードでは、特定のタスクに対するコードの雛形を提供します。")
            print("知りたいタスクのキーワードを入力してください。(break continue etc...)") # 補助系コードモード    
        while True:
            user_please_auxiliary = input("知りたい補助系コード: ")
# 補助系コードモードーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            if user_please_auxiliary == "break":
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
            elif user_please_auxiliary == "基本コードモード": 
                print("わかりました。では基本コードモードに戻ります")
                print("Pythonで多用する基本コード復習用のAIです。知りたいコードのキーワードを入力してください。(print, input, import etc...)")
                break # ここで基本コードモードに戻る
            elif user_please in user_finish or user_please_auxiliary in user_finish:
                print("わかりました。では困ったらまた呼び出してください")
                print("AIを終了中...")
                time.sleep(3)
                exit()
            else:
                user_please == "" or user_please_auxiliary == ""
                print("そのコードまたは説明は用意されていません。お手数をおかけいたしますがご自分で検索をお願いいたします")
            
