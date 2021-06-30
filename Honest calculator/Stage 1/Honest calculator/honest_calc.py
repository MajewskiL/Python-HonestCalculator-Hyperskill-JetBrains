msg_1 = "Do you know what numbers are? Focus!"
msg_2 = "Yes ... an interesting math operation. Did you sleep in class?"

while True:
    calc = input()
    x, oper, y = calc.split(" ")
    if not x.isdigit() or not y.isdigit():
        print(msg_1)
    else:
        if oper not in "*/+-":
            print(msg_2)
        else:
            break
