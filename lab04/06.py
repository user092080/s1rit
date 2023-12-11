r_area= lambda len,ht : len*ht
t_area= lambda  b,h: .5*b*h
c_area= lambda  rad : 3.14*rad*rad

print("1.Calculate Area Of Rectangle")
print("2.Calculate Area Of Triangle")
print("3.Calculate Area Of Circle")

c=int(input("Ente your choice"))
if(c==1):
 len=int(input("Enter length values"))
 ht=int(input("Enter heightt values"))
 print("Area of Rectangle is",r_area(len,ht))

elif(c==2):
 b=int(input("Enter breadth values"))
 h=int(input("Enter heigth values"))
 print("Area of Triangle is",t_area(b,h))

elif(c==3):
 rad=int(input("Enter radius"))
 print("Area of Circle is",c_area(rad))

else:
 print("Invalid choice")









