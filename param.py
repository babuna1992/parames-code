import os
a = os.popen('touch demo.py')
path = os.getcwd()
d = os.listdir(path)
print(d)
"""
if "demo.py" in d:
	print('file has been created')
else:
	print('File hasn't created')


with open ('demo.py','w') as fh:
	c = 'i am good'
	fh.write(c)
with open('demo.py','r') as fh:
	b = fh.read()
	print(b)
	if c == b:
		print('string matched')
	else:
		print('string not matched')
"""
