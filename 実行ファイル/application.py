# この作品が対応しているコードは動画をご覧ください！
# https://youtu.be/ofvfetLsmn4
import time
from utils import progress_bar
import sys
import platform
import json
import subprocess
from pathlib import Path
# rich を使ったメッセージ表示やプログレスバーを実装したいならimportする↓
# ------ ここから ------
# from rich.prompt import Prompt
# from rich.console import Console
# from rich.progress import Progress
# console = Console()
# ------ ここまで ------

# ------ 定数 ------
APP_VERSION = "1.0.7"
LAST_UPDATE = "2025-08-24"
USER_FINISH = ["終了", "特にない", "特になし", "もう大丈夫"]
MODE_NAMES = {
    "basic": "基礎文法モード",
    "detailed": "詳細説明モード",
    "module": "モジュールモード",
}
USER_COMMANDS = {
    "version": "show_version",
    "-v": "show_version",
    "version --detailed": "show_version_detailed",
    "help": "help_terminal",
    "モード切り替え": "ai_mode_switch",
}
BASE_PATH = Path(__file__).resolve().parent
JSON_FILES: dict[str, str] = {
    "normalinput": "input.json",
    "explanationinput": "explanationsinput.json",
    "moduleinput": "moduleinput.json",
}


def print_version_info(detailed: bool = False) -> None:
    """バージョン情報を表示。detailed=Trueで詳細表示"""
    print(f"PytutorAI ver.{APP_VERSION}")
    if detailed:
        print(f"Python Version: {sys.version}")
        print(
            f"OS: {platform.system()} {platform.release()} ({platform.architecture()[0]})"
        )
        print(f"実行環境: {Path(sys.executable).name}")
        print(f"最終更新日：{LAST_UPDATE}")


def show_version() -> None:
    print_version_info(detailed=False)


def show_version_detailed() -> None:
    print_version_info(detailed=True)


def ai_mode_switch():
    # rich を使うなら↓
    # user_mode = (
    #     Prompt.ask(
    #         "わかりました。特定の数字を入力してください。", choices=["1", "2", "3"]
    #     )
    #     .strip()
    #     .lower()
    # )
    # rich を使わないなら↓
    print(
        "わかりました。特定の数字を入力してください。(数字に関してはupdatelog.txtを参照)"
    )
    user_mode = input("数字： ").strip().lower()
    modes = {"1": "basic", "2": "detailed", "3": "module"}
    mode = modes.get(user_mode, "basic")
    print(MODE_NAMES.get(mode, "デフォルトモード") + "に切り替えました。")
    return mode


def help_terminal():
    help_path = Path(__file__).resolve().parent / "help.py"
    if not help_path.exists():
        print("help.pyが見つかりません。ファイルが存在するか確認してください。")
        return
    try:
        subprocess.Popen(["start", "python", str(help_path)], shell=True)
    except Exception as e:
        print(f"help.pyの起動に失敗しました: {e}")


def load_json(filename):
    file_path = BASE_PATH / filename
    if not file_path.exists():
        print(f"{filename}が見つかりません。ファイルが存在するか確認してください。")
        return {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"{filename}の内容が不正です。JSON形式を確認してください。")
        return {}
    except Exception as e:
        print(f"{filename}の読み込みに失敗しました: {e}")
        return {}


# ...existing code...


def handle_mode(mode: str, input_dict: dict, prompt: str) -> str:
    """各モードのユーザー入力処理"""
    try:
        user_input = input(prompt).strip().lower()
    except (KeyboardInterrupt, EOFError):
        print("入力が中断されました。コマンド一覧: " + ", ".join(USER_COMMANDS.keys()))
        return mode
    if user_input in USER_FINISH:
        print("わかりました。では困ったらまた呼び出してください!")
        print("アプリを終了中...")
        time.sleep(2)
        sys.exit()
    if user_input in USER_COMMANDS:
        command = USER_COMMANDS[user_input]
        if command == "ai_mode_switch":
            return ai_mode_switch()
        elif command == "show_version":
            show_version()
        elif command == "show_version_detailed":
            show_version_detailed()
        elif command == "help_terminal":
            help_terminal()
        return mode
    if user_input in input_dict:
        print("\n".join([str(line) for line in input_dict[user_input]]))
    else:
        candidates = sorted(list(input_dict.keys()))[:5]
        print("その内容は用意されていません。候補: " + ", ".join(candidates) + " ...")
    return mode


def main(input_func=input) -> None:
    """アプリのメイン処理。input_funcはテスト用に差し替え可能"""
    for msg in [
        "application.pyを読みこみ中...",
        "バージョンを確認中...",
        "アプリを初期化中...",
    ]:
        time.sleep(0.2)
        progress_bar(msg)
    ai_mode = "basic"
    json_data = {key: load_json(filename) for key, filename in JSON_FILES.items()}

    print("アプリを起動中...")
    time.sleep(1.5)
    print("アプリが起動しました。続行するにはEnterキーを押してください...")
    enter_ai = input_func("")
    if enter_ai != "":
        print("Enter以外の入力が検知されました。アプリを終了します")
        print("アプリを終了中...")
        time.sleep(2)
        sys.exit(0)
    else:
        print(
            "Pythonで多用する基本コード復習用アプリです。知りたいコードのキーワードを入力してください。(print, input, import etc...)"
        )

    while True:
        if ai_mode == "basic":
            ai_mode = handle_mode("basic", json_data["normalinput"], "知りたいコード: ")
        elif ai_mode == "detailed":
            ai_mode = handle_mode(
                "detailed", json_data["explanationinput"], "説明が欲しいコード: "
            )
        elif ai_mode == "module":
            ai_mode = handle_mode(
                "module", json_data["moduleinput"], "知りたいモジュール: "
            )


if __name__ == "__main__":
    main()
