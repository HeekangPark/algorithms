def alpha_num_mapper(alpha):
    alpha = alpha.lower()
    if alpha in ["a", "b", "c"]:
        return 2
    elif alpha in ["d", "e", "f"]:
        return 3
    elif alpha in ["g", "h", "i"]:
        return 4
    elif alpha in ["j", "k", "l"]:
        return 5
    elif alpha in ["m", "n", "o"]:
        return 6
    elif alpha in ["p", "q", "r", "s"]:
        return 7
    elif alpha in ["t", "u", "v"]:
        return 8
    elif alpha in ["w", "x", "y", "z"]:
        return 9

def time_to_dial(num):
    return num + 1

print(sum([time_to_dial(alpha_num_mapper(l)) for l in list(input())]))
