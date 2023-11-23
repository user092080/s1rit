text=input("enter a line of text")
words=text.split()
word_count={}
for word in words:
 word=word.strip('.,!?()[]{}"\"').lower()
 if word in word_count:
  word_count[word]+=1
 else:
  word_count[word]=1
for word,count in word_count.items():
 print(f"'{word}':{count}")
