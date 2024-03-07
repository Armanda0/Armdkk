#1
import os
p = os.listdir(r'C:\Users\Lenovo\OneDrive\Рабочий стол\PP II')
for i in p:
    print(i)
for i in p:
    if os.path.isdir(i) or os.path.isfile(i):
        print(i)
for i in p:
    if os.path.isfile(i):
        print(i)

#2
import os
p = os.listdir(r'C:\Users\Lenovo\OneDrive\Рабочий стол\PP II')
print('Exists:', os.access(__file__, os.F_OK))
print('Readable:', os.access(__file__, os.R_OK))
print('Writable:', os.access(__file__, os.W_OK))
print('Executable:', os.access(__file__, os.X_OK))

#3
import os
p = (r"C:\Users\Lenovo\OneDrive\Рабочий стол\PP II")

if os.path.exists(p):
    print("file and dir portions of the path")
    print(os.path.basename(p))
    print(os.path.dirname(p))
else:
    print("pass doesnt exist!")


#4
import os
f = open(r"C:\Users\Lenovo\OneDrive\Рабочий стол\PP II\lab06\dir-and-files\sumtext.txt")
cnt = 0
for lines in f:
    cnt += 1
print("files has {} lines".format(cnt))

#5
import os
f = open(r"C:\Users\Lenovo\OneDrive\Рабочий стол\PP II\lab06\dir-and-files\iwrotelist.txt", "a")
a = ["i", "wrote", "some", "stuff"]
for i in a:
    f.write(i)

#6
import os
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    f = open("{}.txt".format(i), "x")

#7
import os
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    f = open("{}.txt".format(i), "x")

#8
import os
p=(r"C:\Users\Lenovo\OneDrive\Рабочий стол\PP II\lab06\dir-and-files\willbedeleted.txt")
if os.path.exists(p):
    os.remove(p)
else:
    print("this file doesnt exist")

