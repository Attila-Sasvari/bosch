import re


# regular expression to identify trajectory elements
traj_regexp = r'y\s?\=\s?(?P<m>\-?\d+)x\s?(?P<operator>[+\-])\s?(?P<b>\d+)'


def will_hit(traj: str, coords: tuple) -> bool:
    """Calculate whether the meteor hits the character or not."""
    if type(traj) is not str:
        return False

    if type(coords) is not tuple:
        return False

    if len(coords) != 2:
        return False

    x, y = coords

    # setup default values
    m = 0
    b = 0
    operator = "+"

    traj_calc = re.search(traj_regexp, traj, re.I)

    if traj_calc is not None:
        m = int(traj_calc["m"])
        operator = traj_calc["operator"]
        b = int(traj_calc["b"])
    else:
        raise ValueError(
            "The provided trajectory does not follow the expected format.")

    # print the equation after normalization and substitution
    # print(f"{y} == {m} * {x} {operator} {b}")

    if b == 0:
        return False

    if operator == "+":
        return y == m * x + b
    elif operator == "-":
        return y == m * x - b
