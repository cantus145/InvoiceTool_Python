# 108 3-4
title = "\n108年03-04月"
allinvos = [ "602", "299", "270", "506", "409" ]


# 判斷3位數
def isValidInput(str):
    return len(str) == 3       

def printGoal(invo):
    idx = 5
    while idx > 0:
         result = "中三碼 中三碼 中三碼 中三碼!!!!!!: " + invo
         if idx == 5:
             print("\n")     
         print(result)        
         if idx == 1:
             print("\n")
         idx-=1          

start = True
while (start):
    invo = input(title + "\n輸入後三碼:") .strip()      

    if("....." in invo):
        start = False
        continue

    if len(invo) == 0:
        continue

    if(not isValidInput(invo)):
        print("\n~~ Err ~~ Err ~~ Err ~~\n")
        continue 

    if invo in allinvos:
        printGoal(invo)
    else: 
        print("\n") 
    