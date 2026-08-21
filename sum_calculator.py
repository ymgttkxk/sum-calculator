"""空白区切りで入力した整数の合計を表示するプログラム。"""


def main() -> None:
    while True:
        raw_numbers = input("合計したい整数を空白で区切って入力してください: ").strip()

        if not raw_numbers:
            print("数字を1つ以上入力してください。")
            continue

        try:
            total = sum(int(number) for number in raw_numbers.split())
        except ValueError:
            print("整数以外が含まれています。もう一度入力してください。")
            continue

        print(f"合計: {total}")
        break


if __name__ == "__main__":
    main()
