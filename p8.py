import os
path = os.getcwd()
def os_name(path,num):
    if os.name == 'nt':
        os.mkdir('babuna')
        print('directory created')
        list_dir = os.listdir(path)
        if 'babuna' in list_dir:
            a = os.getcwd()
            os.chdir(a+'/babuna')
            for i in range(1,num+1):
                file_create = ('babuna'+str(i))
                with open(file_create,'w') as a:
                    a.write('omg')
                    b = os.popen('ls-lish')
                    
               
    elif os.name == 'posix':
        os.mkdir('babuna')
        print('direcrory created')
        list_dir = os.listdir(path)
        if 'babuna' in list_dir:
            a = os.getcwd()
            os.chdir(a+'/babuna')
            for i in range(1,num+1):
                file_create = "babuna"+'p'+str(i)
                with open(file_create,'w+') as a:
			
                	a.write('omg')
                	a.close()
			b = os.popen('ls -lish')
			
                	for i in b:
			    c =  i.split(' ')
			    
                        print(c[0])


os_name(path,5)





