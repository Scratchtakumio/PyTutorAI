import importlib

this_py_version = None

def run(module_name):
    global this_py_version  # ← グローバル変数を使う宣言
    this_py_version = module_name  # バージョンを設定
    return this_py_version

# 関数を呼び出してバージョンをセット
run(module_name="")  # 初期バージョンを設定


while True:
    ai_version = input("使いたいAIのバージョンを入力してください（例：1_0_2）: ")
    module_name = f"ver{ai_version}"

    try:
        formatted_version = module_name.replace("_", ".")  # → "ver1.0.2"
        print(f"選択されたバージョンは {formatted_version} です。これでよろしいですか？ (y/n)")
        confirm = input("")

        if confirm == "y":
            print(f"AIバージョン {formatted_version} が選択できました。")
            ai_module = importlib.import_module(module_name)
            break
        elif confirm == "n":
            print("わかりました。では再選択をお願いします。")
        else:
            print("無効な選択です。再度入力してください。")
    except ModuleNotFoundError:
        print(f"指定されたバージョンのAIモジュール（{module_name}）が見つかりませんでした。削除またはダウンロードがされていない可能性があります。")
        continue

