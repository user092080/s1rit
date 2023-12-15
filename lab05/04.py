import armstrong
start=int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
for i in range(start,end):
        res=armstrong.ams(i)
        if res:
         print(i,"  ")
