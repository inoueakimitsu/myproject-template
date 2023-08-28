"""Some functions."""


def wide_num_to_float(x_str: str) -> float:
    """全角の数字を float に変換します。

    Parameters
    ----------
    x_str : str
        全角の数字(例: '１２３４５')

    Returns
    -------
    float
        float に変換した値
    """
    x = x_str.replace("０", "0")
    x = x.replace("１", "1")
    x = x.replace("２", "2")
    x = x.replace("３", "3")
    x = x.replace("４", "4")
    x = x.replace("５", "5")
    x = x.replace("６", "6")
    x = x.replace("７", "7")
    x = x.replace("８", "8")
    x = x.replace("９", "9")
    x = x.replace("．", ".")

    x = x.replace("零", "0")
    x = x.replace("一", "1")
    x = x.replace("二", "2")
    x = x.replace("三", "3")
    x = x.replace("四", "4")
    x = x.replace("五", "5")
    x = x.replace("六", "6")
    x = x.replace("七", "7")
    x = x.replace("八", "8")
    x = x.replace("九", "9")
    return float(x)


def double_float(x: float) -> float:
    """Return the double of x, assuming x is a float.

    Parameters
    ----------
    x : float

    Returns
    -------
    float
        The double of x.
    """
    return 2.0 * x


def double_int(x: int) -> int:
    """Return the double of x, assuming x is an int.

    Parameters
    ----------
    x : int

    Returns
    -------
    int
        The double of x.
    """
    return 2 * x
