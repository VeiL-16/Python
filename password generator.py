import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
let=int(input("enter no of letters"))
num=int(input("enter no of nums"))
sym=int(input("enter no of symbols"))
total=sym+num+let
nc=0
ns=0
nl=0
p=[]
for i in range(0,total+1):
    randomizer=random.randint(0,2)
    if randomizer==0 and nl<let:
        insider=random.choice(letters)
        p.append(insider)
        nl+=1
    elif randomizer==1 and nc<num:
        insider = random.choice(numbers)
        p.append(insider)
        nc+=1
    elif randomizer==2 and ns<sym:
        insider = random.choice(symbols)
        p.append(insider)
        ns+=1
print(p)
password="".join(p)
print(password)

