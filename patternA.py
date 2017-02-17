#patternA.py
#create pattern A

#Leah Yassky
#09.11.16

n = eval(input("Enter a positive integer: "))

for j in range(1, n+1):
    for i in range(1, n+1):
        print(i, " ", end="")
    print("")   
    
