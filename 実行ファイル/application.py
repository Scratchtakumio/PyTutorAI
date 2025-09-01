# この作品が対応しているコードは動画をご覧ください！
# https://youtu.be/ofvfetLsmn4
# 関数は追加した日時順に書いております。

import time 
import sys
import platform
import json
import subprocess
from pathlib import Path

def show_version():
    this_py_version = "1.0.7"
    print(f"PytutorAI ver.{this_py_version}")

def show_version_detailed():
    this_py_version = "1.0.7"
    print(f"PytutorAI ver.{this_py_version}")
    print(f"Python Version: {sys.version}")
    print(f"OS: {platform.system()} {platform.release()} ({platform.architecture()[0]})")
    print(f"実行環境: {sys.executable.split('/')[-1]}")
    print(f"最終更新日：2025-08-24")

def ai_mode_switch():
    print("わかりました。特定の数字を入力してください。(数字は別途help.pyを使用)")
    localization_mode()
    global ai_mode 
    user_mode = input("数字： ").strip().lower()
    if user_mode == "1":
        if ai_mode != "basic":
            run()
            progress_bar("基礎文法モードに切り替え中...")
            print("基礎文法モードに切り替えました。")
            ai_mode = "basic"
            return
        else:
            duplicationerror()
    elif user_mode == "2":
        if ai_mode != "detailed":
            run()
            progress_bar("詳細説明モードに切り替え中...")
            print("詳細説明モードに切り替えました。")
            ai_mode = "detailed"
            return 
        else:
            duplicationerror()
    elif user_mode == "3":
        if ai_mode != "module":
            run()
            progress_bar("モジュールモードに切り替え中...")
            print("モジュールモードに切り替えました。")
            ai_mode = "module"
            return 
        else:
            duplicationerror()
    elif user_mode == "4":
        if ai_mode != "advanced":
            run()
            progress_bar("応用モードに切り替え中...")
            print("応用モードに切り替えました")
            ai_mode = "advanced"
            return
        else:
            duplicationerror()
    else:
        print("無効な入力です。入力する前のモードに戻します。")
        return

def help_terminal():
    try:
        subprocess.Popen(['start', 'python', 'help.py'], shell=True)
    except subprocess.CalledProcessError:
        print("help.pyの起動に失敗しました。help.pyが削除または破損している可能性があります。")

base_path = Path(__file__).resolve().parent

with open(base_path / 'input.json', 'r', encoding='utf-8') as f:
    normalinput = json.load(f)
with open(base_path / 'explanationsinput.json', 'r', encoding='utf-8') as f:
    explanationinput = json.load(f)
with open(base_path / 'moduleinput.json', 'r', encoding='utf-8') as f:
    moduleinput = json.load(f)
with open(base_path / 'advancedinput.json', 'r', encoding='utf-8') as f:
    advancedinput = json.load(f)

def application_main(prompt_text, input_dict, user_finish_list):
    user_input = input(prompt_text).strip().lower()
    if user_input in input_dict:
        for line in input_dict[user_input]:
            print(line)
    elif user_input in user_finish_list:
        print("わかりました。では困ったらまた呼び出してください!")
        print("アプリを終了中...")
        time.sleep(2)
        sys.exit()
    elif user_input == "mode -c":
        ai_mode_switch()
    elif user_input in ["version", "-v"]:
        show_version()
    elif user_input == "version -d":
        show_version_detailed()
    elif user_input == "help":
        help_terminal()
    else:
        print("そのコードまたは説明は用意されていません。お手数をおかけいたしますがご自分で検索をお願いいたします")
    return None


def localization_mode():
    global localized_mode
    if ai_mode == "basic":
        localized_mode = "基礎文法モード"
    elif ai_mode == "detailed":
        localized_mode = "詳細説明モード"
    elif ai_mode == "module":
        localized_mode = "モジュールモード"
    elif ai_mode == "advanced":
        localized_mode = "応用モード"

def duplicationerror():
    print(f"入力したモードは現在のモード({localized_mode})と重複しています。再入力しますか？(y/n)")
    enter_mode = ""
    enter_mode = input("").strip().lower()
    if enter_mode == "y":
        print("わかりました。指示に従ってください")
        ai_mode_switch()
    elif enter_mode == "n" or enter_mode != "y":
        print("わかりました。ではモード切り替えを行わず、元のモードに戻します。")
        return

def run():
    time.sleep(0.2)  # 起動してる感だけ出す

def progress_bar(message,duration=2.0, steps=40):
    print(message)
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
progress_bar("application.pyを読みこみ中...")
run()
progress_bar("バージョンを確認中...")
run()
progress_bar("アプリを初期化中...")
user_finish_list = ["終了", "特にない", "特になし", "もう大丈夫"]
ai_mode = "basic"


print("アプリを起動中...")
time.sleep(1.5)
print("アプリが起動しました。続行するにはEnterキーを押してください...")
enter_ai = ""
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
        new_mode = application_main("知りたいコード: ", normalinput, user_finish_list)
        if new_mode:
            ai_mode = new_mode

    if ai_mode == "detailed":
        new_mode = application_main("説明が欲しいコード: ", explanationinput, user_finish_list)
        if new_mode:
            ai_mode = new_mode

    if ai_mode == "module":
        new_mode = application_main("知りたいモジュール: ", moduleinput, user_finish_list)
        if new_mode:
            ai_mode = new_mode

    if ai_mode == "advanced":
        new_mode = application_main("やってみたいこと: ", advancedinput, user_finish_list)
        if new_mode:
            ai_mode = new_mode