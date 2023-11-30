def interest(x,y,r):
 si=(x*y*r)/100
 print("Simple Interest",si)
 print("End Balance=",x+si)


age=int(input("Enter the age of customer"))
if(age>=60):
  R=12
else:
  R=10
principal=int(input("Enter the principal amount"))
time=int(input("Enter the time period in years"))
interest(principal,time,R)
