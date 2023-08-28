s1=float(input("Enter value of side1: "))
s2=float(input("Enter value of side2: "))
s3=float(input("Enter value of side3: "))
if s1<0 or s2<0 or s3<0:
    print("Invalid Input!")
if (s1+s2>s3 or s1+s3>s2 or s2+s3>s1) and(s1>0 and s2>0 and s3 >0):
    print("All three sides form triangle.")