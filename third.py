import os
path = os.getcwd()
print("current path is: ",path)
a = os.popen('mkdir dir')
a.close()
list_dir = os.listdir(path)
print("list dir is: ",list_dir)
b = os.chdir(path + '/dir')
new_path = os.getcwd()
for i in range(1,11):
	d = 'babu' + str(i)
	c = os.popen('dd if=/dev/urandom of='+d+' bs=1M count=1')
	c.close()
e = os.popen('ls -lish')
for i in e:
    print(i)
