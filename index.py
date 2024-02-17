# TURTLE PROGRAMMER v. 0.5
from turtle import *

pr = textinput("CODE", "Type your program here (use only ^, <, >, v or use on start: f or digit(from 1 to 9) or type \"u\" or \"d\"): ")
fpr = list(pr)

def encode(list):
    try:
        int(list[0])
    except ValueError:
        if list[0] == "f":
            while True:
                for i in range(len(list) - 1):
                    if list[i + 1] == "<":
                        left(90)
                    elif list[i + 1] == ">":
                        right(90)
                    elif list[i + 1] == "^":
                        forward(20)
                    elif list[i + 1] == "v":
                        backward(20)
                    elif list[i+1]=="u":
                        penup()
                    elif list[i+1]=="d":
                        pendown()
                    else:
                        print("WRONG CODE!")
                        break
        else:
            for i in range(len(list)):
                if list[i] == "<":
                    left(90)
                elif list[i] == ">":
                    right(90)
                elif list[i] == "^":
                    forward(20)
                elif list[i] == "v":
                    backward(20)
                elif list[i+1]=="u":
                    penup()
                elif list[i+1]=="d":
                    pendown()
                else:
                    print("WRONG CODE!")
                    break
    else:
        for j in range(int(list[0])):
            for i in range(len(list) - 1):
                if list[i + 1] == "<":
                    left(90)
                elif list[i + 1] == ">":
                    right(90)
                elif list[i + 1] == "^":
                    forward(20)
                elif list[i + 1] == "v":
                    backward(20)
                elif list[i+1]=="u":
                        penup()
                elif list[i+1]=="d":
                    pendown()
                else:
                    print("WRONG CODE!")
                    break

encode(fpr)
hideturtle()

exitonclick()