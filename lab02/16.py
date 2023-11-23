str1=input("enter the first string:")
str2=input("enter the second  string:")
if len(str1)<2 or len(str2)<2:
 print("Atleast two characters is required ")
else:
 str3 = str1[0] +str2[1]+ str1[2:] + " " + str2[0] +str1[1]+ str2[2:]
print("REsult:",str3)
