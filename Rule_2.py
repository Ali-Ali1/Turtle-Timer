import turtle
import time




def rule_2(minss, brk):
    while minss:
        mins, secs = divmod(minss, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, 'remaining')
        time.sleep(1)
        minss -= 1
    work = turtle.Turtle()

    work.write("Take a Break!", font=("Verdana",30, "normal"))

      

    while brk:
        mins, secs = divmod(brk, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, 'remaining')
        time.sleep(1)
        brk -= 1

    turtle.bye


rule_2(10, 10)

