message = ["Maybe next time you add your leg to the head?",
           "You must have been good at math, hehe ...",
           "Awesome! You can enter the equation! :)"]

while True:
    number = input("Enter the equation")
    number = number.split(" ")
    oper = number[1]
    try:
        x = float(number[0])
        y = float(number[2])
        if oper not in "+-*/":
            print(message[1])
        else:
            break
    except ValueError:
        print(message[0])
print(message[2])

# dodać na wykresie komendę dla input
