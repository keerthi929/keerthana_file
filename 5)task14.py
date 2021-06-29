
#try and catch

try:
	name=input('Enter filename:')
	f=open(name,'r')
except IOError:
	print('File not found:',name)
else:
	n=len(f.readlines())
	print(name,'has',n,'lines')
	f.close()
	
	
	#output
	
Enter filename:ex.py
File not found: ex.py
Enter filename:abcd
File not found: abcd

[Program finished]