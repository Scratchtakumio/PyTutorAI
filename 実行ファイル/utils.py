import sys
import time


def progress_bar(message: str, duration: float = 2.0, steps: int = 40) -> None:
    """進捗バーを表示（application.py, help.py共通）"""
    print(message)
    sys.stdout.write("[")
    sys.stdout.flush()
    for i in range(steps):
        time.sleep(duration / steps)
        sys.stdout.write("■")
        sys.stdout.flush()
    sys.stdout.write("]")
    sys.stdout.flush()
    print(" 100%")
