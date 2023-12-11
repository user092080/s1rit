terms = int(input("Enter the required terms"))
result = list(map(lambda x: 2 ** x, range(terms)))
print("The total terms are:",terms)
for i in range(terms):
   print("2 ^",i,":",result[i])
