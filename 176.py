print("Name: KAMRAN SAIF\nRoll_no: SP19-BCS-176\n\n")
f = open("validInput.txt", "r")
inp = f.readlines()
Input=[]
f = open("production.txt", "r")
pro = f.readlines()
production=[]
f = open("table.txt", "r")
table = f.readlines()
Table=[]
f = open("non-terminal.txt", "r")
nt = f.readlines()
Non_Terminal = []
ii = []

for i in inp:
    Input.append(i.replace("\n",""))
for i in pro:
    production.append(i.replace("\n",""))
for i in nt:
    Non_Terminal.append(i.replace("\n",""))
for i in table:
    Table.append(i.split())

stack = [0]

def shift(val):
    val = val[1 : :]
    stack.append(val)
    print("Printing Stack after shifting: ",stack)

def reduction(val):
    val = int(val[1 : :])

    prod = production[val]
    length = len(prod)

    length = length * 2
    for l in range(0,length):
        stack.pop()

    print("Printing Stack : ",stack)

    stack.append(Non_Terminal[val])
    print("Printing Stack : ",stack)

    row = int(stack[-2])+1

    for t in Table:
        column = int(t.index(stack[-1]))
        break

    stack.append(Table[row][column])
    print("Printing Stack : ",stack)

    for t in Table:
        column = int(t.index(i))
        break

    row = int(stack[-1]) + 1

    print("IN REDUCTION: row:",row,"\tcolumn:",column)
    val = Table[row][column]
    print("Value from table obtained: ",val)

    if val[0] == "S":
        stack.append(i)
        shift(val)
    elif val[0] == "R":
        reduction(val)
    elif (val == "acc"):
        print("Successfuly Parsed")
    else:
        print("Input is not valid")


for gg in Input:
    if '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' in gg:
        ii.append('a')
        if '.' in gg:
            ii.pop()
            ii.append('b')
        if '+' in gg:
            ii.pop()
            ii.append('+')
        if '*' in gg:
            ii.pop()
            ii.append('*')
        if '(' in gg:
            ii.pop()
            ii.append('(')
        if ')' in gg:
            ii.pop()
            ii.append(')')
        if '$' in gg:
            ii.pop()
            ii.append('$')
        
    

global G
global F

def semantic(tabvalue, num):
    tabvalue = (int(tabvalue[1::]))
    print("\nNow in the semantic : ")
    if(tabvalue == 7):
        print()
    elif(tabvalue == 6):
        F = int(num)
        print("b is reduce, value is ",F)
    elif (tabvalue == 5):
        G = int(num)
        print("a is reduce, value is ",G)
    elif (tabvalue == 4):
        print("T*F reduce")
    elif (tabvalue == 3):
        print("F is reduce")
    elif (tabvalue == 2):
        print("E+T is reduce")
    elif (tabvalue == 1):
        print("E-T is reduce")
print("Input: ",Input)
counter = 0
print("After tokenization: ",ii)
for i in ii:
    for t in Table:
        column = int(t.index(i))
        break
    
    counter = counter + 1
    print("Input number:",counter)
    row = int(stack[-1])+1

    print("IN MAIN FUNCTION: row:",row,"\tcolumn:",column)
    
    val = Table[row][column]
    print("Value from table obtained: ",val)

    if(val[0] == "S"):
        stack.append(i)
        shift(val)
    elif(val[0]=="R"):
        reduction(val)
        semantic(val,row)
    elif(val == "acc"):
        print("Successfuly Parsed")
    else:
        print("Input is not valid")


