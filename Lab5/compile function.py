#The findall() Function

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

#The search() Function

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

#The split() Function

import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

#The sub() Function
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)