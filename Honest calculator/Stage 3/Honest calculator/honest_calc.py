msg_1 = "Do you know what numbers are? Focus!"
msg_2 = "Yes ... an interesting math operation. Did you sleep in class?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to remember the result (y / n):"
msg_5 = "Do you want continue calculations? (y / n):"

memory = "0"

while True:
    calc = input()
    x, oper, y = calc.split(" ")
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    if not x.isdigit() or not y.isdigit():
        print(msg_1)
    else:
        if oper not in "*/+-":
            print(msg_2)
        else:
            x = int(x)
            y = int(y)
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
            print(msg_4)
            answer = input()
            if answer == "y":
                memory = str(result)
            print(msg_5)
            answer = input()
            if answer != "y":
                break
