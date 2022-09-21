def check_formated(arg):
    if len(arg) > 3:
        return "fail"

    elif arg[1].isalpha() and arg[2].isalpha():
        return "fail"
    elif arg[0].isalpha():
        return "fail"
    elif arg[0].isalpha() and arg[1].isalpha():
        return "fail"
    elif arg[1].isalpha():
        return "fail"
    elif arg[2].isalpha() and len(arg) == 4:
        return "fail"
    elif len(arg) == 1:
        return "00" + arg
    elif len(arg) == 2:
        return "0" + arg
    elif len(arg) == 3 and arg[2].isalpha():
        return "0" + arg
    else:
        return arg


arg = input("Get input")
value = check_formated(arg)
if value == "fail":
    print("Wrong input")
else:
    print(value)
