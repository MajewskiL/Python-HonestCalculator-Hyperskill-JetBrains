msg_0 = "Enter the equation"
msg_1 = "Do you know what the numbers are? Focus!"
msg_2 = "Yes ... an interesting math operation. Did you sleep in class?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to remember the result (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"

memory = "0"

while True:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split(" ")
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue
    if oper not in "*/+-":
        print(msg_2)
    else:
        if oper == "+":
            result = x + y
        elif oper == "-":
            result = x - y
        elif oper == "*":
            result = x * y
        elif oper == "/" and y != 0:
            result = x / y
        else:
            print(msg_3)
            continue
        print(result)
        while True:
            print(msg_4)
            answer = input()
            if answer == "y":
                memory = str(result)
                break
            elif answer == "n":
                break
        while True:
            print(msg_5)
            answer = input()
            if answer == "y":
                break
            elif answer == "n":
                exit()

