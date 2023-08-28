#question8
bs=float(input("Enter basic salary: "))
hra=0.2*bs
ta=0.05*bs
da=0.1*bs
gs=bs+hra+ta+da
print("Gross Salary =",bs+hra+ta+da)
#question9
if gs<300000:
    print("No imcome tax for you!")
if gs>=300000 and gs<1000000:
    print("payable tax= ",0.1*gs)
if gs>=1000000 and gs<2500000:
    print("payable tax= ",0.2*gs)
if gs>=2500000:
    print("payable tax= ",0.3*gs)