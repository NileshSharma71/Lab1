inp=int(input("Enter a 5 digit number: "))
a=int(inp/10000)
b=(inp%10000)//1000
c=(inp%1000)//100
d=(inp%100)//10
e=inp%10
print("Reverse of the entered no.:",e,d,c,b,a)
if (a,b,c,d,e)==(e,d,c,b,a):
    print("The no. is Palindrome.")
else:
    print("The no. is not Palindrome.")