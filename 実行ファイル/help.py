import time
import sys
import json
from pathlib import Path
from utils import progress_bar

HELP_COMMANDS = {
    "help -e": "exit",
    "help -u": "help_using",
    "help -k -n": "help_keyword",
    "help -k -m": "help_keyword_module",
    "help -c": "help_command",
}

BASE_PATH = Path(__file__).resolve().parent


def load_json(filename: str) -> dict:
    """JSONファイルを読み込む。失敗時は空dictを返す"""
    file_path = BASE_PATH / filename
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


normalinput = load_json("input.json")
moduleinput = load_json("moduleinput.json")


def help_using() -> None:
    """使い方説明"""
    print(
        "使い方:\n知りたいコードを入力するだけ!コードはアプリが解説してくれるからいくらでも使っちゃおう!"
    )
    print(
        "モード説明：\n基礎文法コードモード コード番号1 登録されているキーワードの簡単な説明を聞ける。\n詳細説明モード コード番号2 登録されているすべてのキーワードの細かな説明が聞ける。\nモジュールモード コード番号3 モジュールに関する説明が聞ける。"
    )
    print(
        "モード切り替えと入力すると、モードを変えられる。上記のコード番号のいずれかを入力すると、任意のモードに切り替えられる。"
    )


def help_keyword() -> None:
    """対応キーワード一覧表示"""
    print("対応キーワード一覧：")
    for keyword in normalinput.keys():
        print(f"{keyword}")


def help_keyword_module() -> None:
    """対応モジュール一覧表示"""
    print("対応モジュール一覧：")
    for modulekeyword in moduleinput.keys():
        print(f"{modulekeyword}")


def help_command() -> None:
    """コマンド説明表示"""
    print(
        "version\ncode.pyのバージョンを確認できるコマンド\n--detailed\nversionコマンドの横につけることでcode.pyの詳細が確認できるサブコマンド"
    )


## utils.pyのprogress_barのみ利用


def main():
    progress_bar("help.pyを読み込み中...")
    print("helpコマンドターミナルを起動中...")
    time.sleep(1.5)
    print("ターミナルが起動しました。続行するにはEnterキーを押してください...")
    try:
        enter_ai = input("")
    except (KeyboardInterrupt, EOFError):
        print("中断されました。helpコマンドターミナルを終了します")
        sys.exit()
    if enter_ai != "":
        print("Enter以外の入力が検知されました。ターミナルを終了します")
        print("helpコマンドターミナルを終了中...")
        time.sleep(2)
        sys.exit()
    else:
        print(
            "helpコマンドの横にサブコマンドをつけることでcode.pyの使用方法の確認や特定のキーワードが登録されているかが確認できるターミナルです。"
        )

    while True:
        try:
            user_help = input("command：").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("中断されました。helpコマンドターミナルを終了します")
            sys.exit()
        if user_help in HELP_COMMANDS:
            cmd = HELP_COMMANDS[user_help]
            if cmd == "exit":
                print("わかりました。では困ったらまた呼び出してください!")
                print("ターミナルを終了中...")
                time.sleep(2)
                sys.exit()
            elif cmd == "help_using":
                help_using()
            elif cmd == "help_keyword":
                help_keyword()
            elif cmd == "help_keyword_module":
                help_keyword_module()
            elif cmd == "help_command":
                help_command()
        else:
            print(
                f'"{user_help}"は、コマンドとして登録されていません。入力しなおしてください。'
            )


if __name__ == "__main__":
    main()
