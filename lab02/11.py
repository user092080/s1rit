list=[]
n=int(input("Enter thel limit"))
for i in range(n):
  value=int(input("Ente the value:"))
  if value <100:
    list.append(value)
  else:
    list.append("over")
print(list)
