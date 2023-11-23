str=input("Enter the string")
if str.endswith("ing"):
 str=str+"ly"
else:
 str=str+"ing"
print("Modified Word:",str)
