import numpy as np
import operator
from typing import Union

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "^": operator.pow
}


def calculate_error(groups: list, err_1: float, err_2: float) -> Union[list[float], str]:
    num_1 = float(groups[0])
    oper = groups[1]
    num_2 = float(groups[2])
    if oper == "+" or oper == "-":
        return [ops[oper](num_1, num_2), err_1 + err_2]
    elif oper == "*" or oper == "/":
        new_val = ops[oper](num_1, num_2)
        return [new_val, new_val * np.sqrt((err_1 / num_1) ** 2 + (err_2 / num_2) ** 2)]
    elif oper == "^":
        new_val = ops[oper](num_1, num_2)
        return [new_val, np.abs(new_val) * np.abs(num_2) * (err_1 / num_1)]
    else:
        return "Operator not recognised"


data = input("Enter calculation (include spaces between operator and numbers): ")  # Example: 2 * 4
err_num_1 = float(input("Enter error on first number: "))

matches = data.split(" ")

if matches[1] != "^":
    err_num_2 = float(input("Enter error on second number: "))
else:
    err_num_2 = None  # Error calc not supported for error on exponent

value, error = calculate_error(matches, err_num_1, err_num_2)

print(f"value: {value}")
print(f"error: {error}")
print(f"percentage error: {100 * error/value}")
