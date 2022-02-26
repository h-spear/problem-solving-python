# https://www.acmicpc.net/problem/4836


def check_rule_1(dances):
    success = True
    for i, dance in enumerate(dances):
        if dance == "dip":
            if i - 1 >= 0 and dances[i - 1] == "jiggle":
                continue
            if i - 2 >= 0 and dances[i - 2] == "jiggle":
                continue
            if i + 1 < len(dances) and dances[i + 1] == "twirl":
                continue
            dances[i] = "DIP"
            success = False
    return success


def check_rule_2(dances):
    if len(dances) < 3:
        return False
    if dances[-3] != "clap":
        return False
    if dances[-2] != "stomp":
        return False
    if dances[-1] != "clap":
        return False
    return True


def check_rule_3(dances):
    if "twirl" in dances:
        if "hop" not in dances:
            return False
    return True


def check_rule_4(dances):
    if dances[0] == "jiggle":
        return False
    return True


def check_rule_5(dances):
    if "dip" in dances or "DIP" in dances:
        return True
    return False


while 1:
    try:
        dances = list(input().split())
        form_check = [
            check_rule_1(dances),
            check_rule_2(dances),
            check_rule_3(dances),
            check_rule_4(dances),
            check_rule_5(dances),
        ]

        nums = [i + 1 for i, x in enumerate(form_check) if x == False]
        correct = form_check.count(True)
        if correct == 5:
            print("form ok:", " ".join(dances))
        elif correct == 4:
            print(
                "form error {}:".format(form_check.index(False) + 1), " ".join(dances)
            )
        else:
            print("form errors", end="")
            print(" {}".format(nums[0]), end="")
            for i in range(1, len(nums) - 1):
                print(", {}".format(nums[i]), end="")
            print(" and {}:".format(nums[-1]), " ".join(dances))
    except:
        break
