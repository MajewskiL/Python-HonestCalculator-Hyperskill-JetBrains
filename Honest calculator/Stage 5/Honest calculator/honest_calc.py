message = ["Maybe next time you add your leg to the head?",
           "You must have been good at math, hehe ...",
           "Awesome! You can enter the equation! :)",
           "You gotta be really smart if you divide by zero!",
           "Are you sure you won't remember a one-digit number? y/n: ",
           "Hey man, it's only one digit... y/n: ",
           "Really...? y/n: ",]


#  not done, prepare function
def check_function(num1, operator, num2):
    return False


memory = 0
while True:
    while True:
        while True:
            number = input("Enter the equation: ")
            number = number.split(" ")
            oper = number[1]
            result = 0
            try:
                if number[0] == "M":
                    x = memory
                else:
                    x = float(number[0])
                if number[2] == "M":
                    y = memory
                else:
                    y = float(number[2])
                if oper not in "+-*/":
                    print(message[1])
                ans = check_function(x, oper, y)
                if ans:
                    print(ans)
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
                result = x / y
                break
            else:
                print(message[3])
    print(message[2])
    print(f"{x} {oper} {y} = {result}")
    ans = input("Do you want remember the result? y/n: ")
    if ans == "y":
        if -10 < result < 10 and result == int(result):
            i = 4
            while True:
                ans = input(message[i])
                if ans == "y":
                    i += 1
                else:
                    break
                if i > 6:
                    memory = result
                    break
        else:
            memory = result
    ans = input("Do you want to coninue? y/n: ")
    if ans == "n":

        break

# dodać na wykresie komendę dla input
# result = 0 w deklaracjach
# na wykresie dodać print(message[2])
# dać zmienną to pytań y/n
# zmienna result ma być zainicjowna przed pętlami!!!!
# zmienną wskazującą na komentarz zrobić 'i'
# jest źle z memory result, jak nie mięsci się w -10<x>10 to trzeba zapisać
# NA wykresie x będzie inne bo dojdzie procedura
