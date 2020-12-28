import subprocess

list_files = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE)
xx=str(list_files.stdout,'utf-8')
ll = list(xx.split('\n'))
for x in ll:
    print (x)
