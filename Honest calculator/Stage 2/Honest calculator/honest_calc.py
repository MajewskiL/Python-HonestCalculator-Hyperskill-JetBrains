message = ["Maybe next time you add your leg to the head?",
           "You must have been good at math, hehe ...",
           "Awesome! You can enter the equation! :)",
           "You gotta be really smart if you divide by zero!",]

while True:
    while True:
        number = input("Enter the equation: ")
        number = number.split(" ")
        oper = number[1]
        result = 0
        try:
            x = float(number[0])
            y = float(number[2])
            if oper not in "+-*/":
                print(message[1])
            else:
                break
        except ValueError:
            print(message[0])
    if oper == "+":
        result = x + y
        break
    elif oper == "-":
        result = x - y
        break
    elif oper == "*":
        result = x * y
        break
    elif oper == "/":
        if y != 0:
            result = x - y
            break
        else:
            print(message[3])

print(message[2])
print(f"{x} {oper} {y} = {result}")

# dodać na wykresie komendę dla input
# result = 0 w deklaracjach
# na wykresie dodać print(message[2])
# w przykładach testowych wziąc -1.1.1. oraz 1-000 żeby
