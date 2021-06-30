msg_1 = "Do you know what numbers are? Focus!"
msg_2 = "Yes ... an interesting math operation. Did you sleep in class?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to remember the result (y / n):"
msg_5 = "Do you want continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msgs = [0] * 3
msgs[0] = "Are you sure? It is only one digit! (y / n)"
msgs[1] = "Don't be silly, it's just one number! Add to memory? (y / n)"
msgs[2] = "Last chance! Do you want to be ashamed for the rest of your days? (y / n)"
memory = "0"


def is_one_digit(v):
    if -10 < v < 10 and v == round(v):
        return True
    return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if v1 == 1 or v2 == 1 and v3 == "*":
        msg += msg_7
    if v1 == 0 or v2 == 0 and v3 == "*":
        msg += msg_8
    if msg:
        msg = msg_9 + msg
        print(msg)


while True:
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
    else:
        if oper not in "*/+-":
            print(msg_2)
        else:
            check(x, y, oper)
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
                if is_one_digit(result):
                    msg_index = 0
                    while msg_index < 3:
                        print(msgs[msg_index])
                        answer = input()
                        if answer == "y":
                            msg_index += 1
                            if msg_index == 3:
                                memory = str(result)
                        elif answer == "n":
                            msg_index = 4
                else:
                    memory = str(result)
            print(msg_5)
            answer = input()
            if answer != "y":
                break
