input=input("Enter the string")
char_freq={}
for char in input:
 char_freq [char]=char_freq.get(char,0)+1
print("Character Frequency")
for char,freq in char_freq.items():
 print(f"'{char}':{freq}")
