s=int(input("Enter a 3 digit number: "))
g=s/100
k=int(g)
op=(s%100)//10
kl=s%10
if k**3 +op**3 +kl**3 ==s:
    print("The number is an armstrong number.")
else:
    print("The number is not an armstrong number.")