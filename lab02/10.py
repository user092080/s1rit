inp=input("Ente the string")
n=len(inp)
if n>=2:
  new=inp[-1]+inp[1:n-1]+inp[0]
  print(new)
else:
 print("Insufficient string characters")

