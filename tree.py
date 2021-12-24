from colored import fg
import random
import time
def get_radom_color():
    christmas_colors = [fg('blue'),fg('red'),
     fg('green'),fg('gold_3a'),fg('grey_69')]
    return random.choice(christmas_colors)
#Christmas tree
def triangle_shape(n):
    for i in range(n):
        for _ in range(n-i):
            print(get_radom_color() + ' ', end='')
        for _ in range(2*i+1):
            if(i == 0):
                print(get_radom_color() + '*',end='')
            else:
                print(get_radom_color() +  '^',end='')
        print()
# base of the tree
def pole_shape(n):
    n= 2*n+1
    midle = int(n/2)
    for i in range(n):
        if (i-1 == midle or i+1==midle):
            print(fg('green') + "|",end="")
        else:
            print(fg('green') + "_",end="")
height = 20
message = "Merry Christmas and Happy new Year!!!"
m_white_spaces = int((2*height+1 - len(message)) / 2)    
triangle_shape(height)
pole_shape(height)
print()
while(True):
    print(m_white_spaces * ' '+get_radom_color() + message, end="")
    print('\b' * (len(message)+m_white_spaces), end = "")
    time.sleep(0.25)
