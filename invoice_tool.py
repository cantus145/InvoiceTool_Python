

##########################################################

# 106 11 - 12
title = "\n 106年 11-12 月"
allinvos = [ "343","249","891","491","437"]

##########################################################


# 判斷3位數
def isValidInput(str):
    return len(str) == 3       

def printGoal(invo):
    idx = 5
    while idx > 0:
         result = "中三碼 中三碼 中三碼 !!!!!: " + invo
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


    if(not isValidInput(invo) or not invo.isnumeric()):

        print("\n===   ERR!  非數字!  Not 3 numeric!   ===\n")
        continue
        
    '''
    多行
    註解
    '''

    if invo in allinvos:
        printGoal(invo)
    else: 
        print("\n") 
    