# declaration of variables



Lambda=float(input("Input value of Lambda :"))
Mu=float(input("Input value of Mu :"))

numberOfServers=int(input("Enter numbe of servers :"))

# T1=1*(Lambda/Mu+Lambda)+0*(Mu/Mu+Lambda)

# for 1 number of busy server i.e for T1

def getFor1():
    return (1*(Lambda/Mu+Lambda)+0*(Mu/Mu+Lambda))

# for n number of servers the equation becomes
def getForN(number):
    return (number*Lambda/number*Mu+Lambda)+(number*Mu/number*Mu+Lambda)
    

def recursion(num):
    if num==1:
        getFor1()
    return getForN(num)*getForN(num-1)


print(recursion(numberOfServers))
    
        