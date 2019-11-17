## libary imports
import sys,os,time

#Opening_Text_time
## variable definition:
info = "had an apple,\n\
ate the apple.\n\
no more apple."

## function definition:
def Time(info):
    for char in info:
        sys.stdout.write(char)
        sys.stdout.flush()
    
        if char !="\n":
           time.sleep(0.1)
        else:
           time.sleep(1)

os.system("cls")
Time(info)
os.system("cls")