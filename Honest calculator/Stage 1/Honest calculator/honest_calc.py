msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

while True:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split(" ")
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue
    if oper not in "*/+-":
        print(msg_2)
    else:
        break
