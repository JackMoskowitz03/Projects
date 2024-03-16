calc=["1","2","3","+",
            "4","5","6","-",
            "7","8","9","*",
            " ","0"," ","/"]

inp=""
inp2=""
inp3=""

def printCalcuator(calc):
    print("--------")
    print("|      |")
    print("--------")
    print(calc[0]+ "|"+calc[1]+"|"+calc[2]+"|"+calc[3])
    print("--------")
    print(calc[4]+ "|"+calc[5]+"|"+calc[6]+"|"+calc[7])
    print("--------")
    print(calc[8]+ "|"+calc[9]+"|"+calc[10]+"|"+calc[11])
    print("--------")
    print(calc[12]+ "|"+calc[13]+"|"+calc[14]+"|"+calc[15])
    print("--------")
printCalcuator(calc)

def userInput(calc):
    inp=input("Input two numbers and a sign for a result, Number 1: ")
    inp2=input("Choose a second Number: ")
    if inp.isdigit() and inp2.isdigit() and 0<=(int(inp))<=999 and 0<=(int(inp2))<=999:
        inp3=input("Now enter a symbol: ")
        if len(inp3)==1 and inp3 in ['+','-','*','/']:
            result(inp,inp,inp3)
        else:
            print("Enter a valid character or symbol: ")


def result(inp,inp2,inp3):
    if inp3 == '+':
        print(f"The Resultis: {int(inp)+int(inp2)}")
    elif inp3 =='-':
        print(f"The Resultis: {int(inp)-int(inp2)}")
    elif inp3 =='*':
        print(f"The Resultis: {int(inp)*int(inp2)}")
    elif inp3 =='/':
        print(f"The Resultis: {int(inp)/int(inp2)}")
userInput(calc)
