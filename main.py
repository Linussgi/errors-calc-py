import numpy as np
import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "^": operator.pow
}


def calculate_error(groups, err_1, err_2):
    if groups[1] == "+" or groups[1] == "-":
        return [ops[groups[1]](float(groups[0]), float(groups[2])), err_1 + err_2]
    elif groups[1] == "*" or groups[1] == "/":
        new_val = ops[groups[1]](float(groups[0]), float(groups[2]))
        return [new_val, new_val * np.sqrt((err_1 / float(groups[0])) ** 2 + (err_2 / float(groups[2])) ** 2)]
    elif groups[1] == "^":
        new_val = ops[groups[1]](float(groups[0]), float(groups[2]))
        return [new_val, np.abs(new_val) * np.abs(float(groups[2])) * (err_1 / float(groups[0]))]
    else:
        return "Operator not recognised"


data = input("Enter calculation: ")
err_num_1 = float(input("Enter error on first number: "))

matches = data.split(" ")

if matches[1] != "^":
    err_num_2 = float(input("Enter error on second number: "))
else:
    err_num_2 = None

value, error = calculate_error(matches, err_num_1, err_num_2)

print(f"value: {value}")
print(f"error: {error}")
print(f"percentage error: {100 * error/value}")
