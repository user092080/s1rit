lst1=[]
lst2=[]
l1=int(input("Enter the limit of first list : "))
for i in range(l1):
        n1=int(input("Enter the value : "))
        lst1.append(n1)
l2=int(input("Enter the limit of second list : " ))
for i in range(l2):
        n2=int(input("Enter the value : "))
        lst2.append(n2)
if l1==l2:
        print("Both lists having same length")
else:
        print("lists having different length")
#print(lst1)
sum1=0

for i in lst1:

        sum1=sum1+i
print("Sum of elements in list1: ",sum1)

sum2=0
for i in lst2:
        sum2=sum2+i
print("Sum of elements in list2: ",sum2)

if sum1==sum2:
        print("Sum of 2 lists are equal!!")
else:
        print("Sum of 2 lists are not equal :)")
flag=0
for i in lst1:
        for j in lst2:
                if i==j:
                        print("common element",j,"Found : (")
                        flag=1

if flag==0:
        print("There is no common elements")

