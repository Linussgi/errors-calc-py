import numpy as np
import re
import operator

# ops["+"](1,1)

ops = {
    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
    "/" : operator.truediv,
    "^" : operator.pow,
}


def test(re_match, err_1, err_2):
    if re_match.groups(0)[1] == "+" or re_match.groups(0)[1] == "-":
        return [ops[re_match.groups(0)[1]](float(re_match.groups(0)[0]), float(re_match.groups(0)[2])), err_1 + err_2]


def calculate_error(re_match, err_1, err_2):
    if re_match.groups(0)[1] == "+" or re_match.groups(0)[1] == "-":
        return [ops[re_match.groups(0)[1]](float(re_match.groups(0)[0]), float(re_match.groups(0)[2])), err_1 + err_2]
    elif re_match.groups(0)[1] == "*" or re_match.groups(0)[1] == "/":
        new_val = ops[re_match.groups(0)[1]](float(re_match.groups(0)[0]), float(re_match.groups(0)[2]))
        return [new_val, new_val * np.sqrt((err_1 / float(re_match.groups(0)[0])) ** 2 + (err_2 / float(re_match.groups(0)[2])) ** 2)]
    elif re_match.groups(0)[1] == "^":
        new_val = ops[re_match.groups(0)[1]](float(re_match.groups(0)[0]), float(re_match.groups(0)[2]))
        return [new_val, np.abs(new_val) * np.abs(float(re_match.groups(0)[2])) * (float(re_match.groups(0)[0]) / err_1)]
    else:
        return "Operator not recognised"


data = input("Enter calculation: ")
err_num_1 = input("Enter error on first number: ")
err_num_2 = input("Enter error on second number: ")


matches = re.match(r"^([\d\.]+) ?([*^/+-]) ?([\d\.]+)$", data)

print(calculate_error(matches, float(err_num_1), float(err_num_2)))