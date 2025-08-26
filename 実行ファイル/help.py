import time
import sys
import json

enter_ai = ""
enter_boot = ""

def help_using():
    print("使い方:\n知りたいコードを入力するだけ!コードはアプリが解説してくれるからいくらでも使っちゃおう!")
    print("モード説明：\n基礎文法コードモード コード番号1 登録されているキーワードの簡単な説明を聞ける。\n詳細説明モード コード番号2 登録されているすべてのキーワードの細かな説明が聞ける。\nモジュールモード コード番号3 モジュールに関する説明が聞ける。")
    print("モード切り替えと入力すると、モードを変えられる。上記のコード番号のいずれかを入力すると、任意のモードに切り替えられる。")

def help_keyword():
    print("対応キーワード一覧：")
    for keyword in normalinput.keys():
        print(f"{keyword}")

def help_keyword_module():
    print("対応モジュール一覧：")
    for modulekeyword in moduleinput.keys():
        print(f"{modulekeyword}")

def help_command():
    print("version\ncode.pyのバージョンを確認できるコマンド\n--detailed\nversionコマンドの横につけることでcode.pyの詳細が確認できるサブコマンド")

with open('C:\\Users\\takumi\\PyTutorAI\\実行ファイル\\input.json', 'r', encoding='utf-8') as f:
    normalinput = json.load(f)
with open('C:\\Users\\takumi\\PyTutorAI\\実行ファイル\\moduleinput.json', 'r', encoding='utf-8') as f:
    moduleinput = json.load(f)

def run():
    time.sleep(0.2) 

def progress_bar(duration=2.0, steps=40):
    print("code.pyを読み込み中..." )
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
    print("help.pyを読み込み中...")
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
    print("helpコマンドを読み込み中...")
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

print("helpコマンドターミナルを起動中...")
time.sleep(1.5)
print("ターミナルが起動しました。続行するにはEnterキーを押してください...")
enter_ai = input("")
if enter_ai != "":
    print("Enter以外の入力が検知されました。ターミナルを終了します")
    print("helpコマンドターミナルを終了中...")
    time.sleep(2)
    sys.exit()
else:
    print("helpコマンドの横にサブコマンドをつけることでcode.pyの使用方法の確認や特定のキーワードが登録されているかが確認できるターミナルです。")

while True:
    user_help = input("command：").strip().lower()
    if user_help == "help -e":
        print("わかりました。では困ったらまた呼び出してください!")
        print("ターミナルを終了中...")
        time.sleep(2)
        sys.exit()
    elif user_help == "help -u":
        help_using()
    elif user_help == "help -k -n":
        help_keyword()
    elif user_help == "help -k -m":
        help_keyword_module()
    elif user_help == "help -c":
        help_command()
    else:
        print("\"" + user_help + "\"" + "は、コマンドとして登録されていません。入力しなおしてください。")