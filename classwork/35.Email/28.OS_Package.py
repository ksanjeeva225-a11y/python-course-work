#1.Operations to create a directory and a sub-directory inside it.
import os

os.mkdir("Batch-41")
os.makedirs("Batch-41/demo")

#2.delete the directory created in step 1.
import os
import shutil
shutil.rmtree("Batch-41")

#3.list all the files and directories in the current directory.
import os

res = os.listdir()
print(res)

#4.find the current working directory.
import os

print(os.getcwd())

#5.path existence check.
import os

path = os.path.join('batch-41', 'demo.txt')

print(os.path.exists(path))

with open(path,'w') as file:
    file.write("Hello world")

#6.
import os

print(os.getcwd())
