msg_0 = "Enter the equation"
msg_1 = "Do you know what the numbers are? Focus!"
msg_2 = "Yes ... an interesting math operation. Did you sleep in class?"

while True:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split(" ")
    try:
        x = float(x)
        y= float(y)
    except ValueError:
        print(msg_1)
        continue
    if oper not in "*/+-":
        print(msg_2)
    else:
        break
