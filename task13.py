import re
s1="aneb an4d 89 app45le"
res=re.findall(r'\w\w*\w',s1)
print(res)

 # matches a word containing ab
 
import re
str=input("Enter a string :")
res=re.findall(r'ab\w',str)
for word in res:
   print(word)
   
 #to check for a number at end
   
import re
str=input("Enter a string :")
res=re.findall(r'\w*\d',str)
for word in res:
	print( word)
	
	
#to search the numbers (0-9) of length between 1 to 3 

import re 
str="zero,one,two,three,4,5,six,seven,8,nine"
result=re.findall(r'\b\w{3}\b',str)
print(result)

#to access only uppercase letter 

import re
str=input("Enter string:")
res=re.findall(r'\w[A-Z]\w',str)
print(res)

