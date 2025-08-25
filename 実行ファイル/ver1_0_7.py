# この作品が対応しているコードは動画をご覧ください！
# https://youtu.be/ofvfetLsmn4
import time 
import sys
import platform
import json


def parse_version(v):
    return tuple(map(int, v.split(".")))

enter_boot = "" 
enter_ai = ""
this_py_version = "1.0.7"
user_finish = ["終了", "特にない", "特になし", "もう大丈夫"]
ai_mode = "basic" 

def show_version():
    print(f"PytutorAI ver.{this_py_version}")

def show_version_detailed():
    print(f"PytutorAI ver.{this_py_version}")
    print(f"Python Version: {sys.version}")
    print(f"OS: {platform.system()} {platform.release()} ({platform.architecture()[0]})")
    print(f"実行環境: {sys.executable.split('/')[-1]}")
    print(f"最終更新日：2025-08-24")

def ai_mode_switch():
    print("わかりました。特定の数字を入力してください。(数字に関してはupdatelog.txtを参照)")
    user_mode = input("数字： ").strip().lower()
    if user_mode == "1":
        print("基礎文法モードに切り替えました。")
        return "basic"
    elif user_mode == "2":
        print("詳細説明モードに切り替えました。")
        return "detailed"
    elif user_mode == "3":
        print("モジュールモードに切り替えました。")
        return "module"
    else:
        print("無効な入力です。デフォルトモードに設定します。")
        return "basic"

with open('C:\\Users\\takumi\\PyTutorAI\\実行ファイル\\input.json', 'r', encoding='utf-8') as f:
    normalinput = json.load(f)
with open('C:\\Users\\takumi\\PyTutorAI\\実行ファイル\\explanationsinput.json', 'r', encoding='utf-8') as f:
    explanationinput = json.load(f)
with open('C:\\Users\\takumi\\PyTutorAI\\実行ファイル\\moduleinput.json', 'r', encoding='utf-8') as f:
    moduleinput = json.load(f)

def run():
    time.sleep(0.2)  # 起動してる感だけ出す

def progress_bar(duration=2.0, steps=40):
    print("ver1_0_7.pyを読み込み中..." )
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

def progress_bar(duration=2.0, steps=40):
    print("アプリを初期化中...")
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
    print("アプリ初期化完了")

run()
progress_bar()

print("アプリを起動中...")
time.sleep(1.5)
print("アプリが起動しました。続行するにはEnterキーを押してください...")
enter_ai = input("")
if enter_ai != "":
    print("Enter以外の入力が検知されました。アプリを終了します")
    print("アプリを終了中...")
    time.sleep(2)
    sys.exit()
else:
    print("Pythonで多用する基本コード復習用アプリです。知りたいコードのキーワードを入力してください。(print, input, import etc...)")

while True:
    if ai_mode == "basic":
        user_please = input("知りたいコード: ").strip().lower()
        if user_please in explanationinput:
            for line in explanationinput[user_please]:
                print(line)
        elif user_please == "モード切り替え":
            ai_mode = ai_mode_switch()
        elif user_please == "version" or user_please == "-v":
            show_version()
        elif user_please == "version --detailed":
            show_version_detailed()
        elif user_please in user_finish:
            print("わかりました。では困ったらまた呼び出してください!")
            print("アプリを終了中...")
            time.sleep(2)
            sys.exit()
        else:
            print("そのコードまたは説明は用意されていません。お手数をおかけいたしますがご自分で検索をお願いいたします")

    if ai_mode == "detailed":
        user_explanation = input("説明が欲しいコード: ").strip().lower()
        if user_explanation in explanationinput:
            for line in explanationinput[user_please]:
                print(line)
        elif user_explanation in user_finish:
            print("わかりました。では困ったらまた呼び出してください!")
            print("アプリを終了中...")
            time.sleep(2)
            sys.exit()
        elif user_explanation == "モード切り替え":
            ai_mode = ai_mode_switch()
        elif user_explanation == "version" or user_please == "-v":
            show_version()
        elif user_explanation == "version --detailed":
            show_version_detailed()
        else:
            print("そのコードまたは説明は用意されていません。お手数をおかけいたしますがご自分で検索をお願いいたします")

    if ai_mode == "module":
        user_module = input("知りたいモジュール:").strip().lower()
        if user_module in moduleinput:
            for line in moduleinput[user_module]:
                print(line)
        elif user_module in user_finish:
            print("わかりました。では困ったらまた呼び出してください!")
            print("アプリを終了中...")
            time.sleep(2)
            sys.exit()
        elif user_module == "モード切り替え":
            ai_mode = ai_mode_switch()
        elif user_module == "version" or user_please == "-v":
            show_version()
        elif user_module == "version --detailed":
            show_version_detailed()
        else:
            print("そのモジュールは用意されていません。お手数をおかけいたしますがご自分で検索をお願いいたします")