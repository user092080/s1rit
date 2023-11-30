def series(n):
 f=1
 s=0
 for i in range (1, n+1):
   f=f*i
   print(f)

 for i in range (1, n+1):
  x=pow(n,n)
  s=s+(x/f)
 print("Sum of Series:",s)

n=int(input("Enter the value of limit"))
series(n)
