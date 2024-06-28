"""エントリーポイントのサンプルです。"""

from myproject.some import wide_num_to_float

if __name__ == "__main__":
    print(wide_num_to_float("１．４１４２１４"))  # noqa: RUF001, T201
