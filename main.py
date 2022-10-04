import numpy as np
import re
import operator

ops = {
    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
    "/" : operator.truediv,
    "^" : operator.pow
}


def calculate_error(re_groups, err_1, err_2):
    if re_groups[1] == "+" or re_groups[1] == "-":
        return [ops[re_groups[1]](float(re_groups[0]), float(re_groups[2])), err_1 + err_2]
    elif re_groups[1] == "*" or re_groups[1] == "/":
        new_val = ops[re_groups[1]](float(re_groups[0]), float(re_groups[2]))
        return [new_val, new_val * np.sqrt((err_1 / float(re_groups[0])) ** 2 + (err_2 / float(re_groups[2])) ** 2)]
    elif re_groups[1] == "^":
        new_val = ops[re_groups[1]](float(re_groups[0]), float(re_groups[2]))
        return [new_val, np.abs(new_val) * np.abs(float(re_groups[2])) * (float(re_groups[0]) / err_1)]
    else:
        return "Operator not recognised"


data = input("Enter calculation: ")
err_num_1 = input("Enter error on first number: ")
err_num_2 = input("Enter error on second number: ")


matches = re.match(r"^([\d\.]+) ?([*^/+-]) ?([\d\.]+)$", data)

print(calculate_error(matches.groups(), float(err_num_1), float(err_num_2)))
