dict1={}
dict2={}
num1=int(input("Enter the 1st list size"))
num2=int(input("Enter the 2nd list size"))
for i  in range(num1):
 O1values=input("Enter dict1 values")
 O1size=input("Enter dict1 values size")

 dict1[O1values]=O1size
for i  in range(num2) :
 O2values=input("Enter dict2 values")
 O2size=input("Enter dict2 values size")

 dict2[O2values]=O2size



dict1.update(dict2)

print("Merged dictionary:", dict1)





