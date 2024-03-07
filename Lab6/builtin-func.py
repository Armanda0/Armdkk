#1
from math import *
ans = [1, 2, 3, 4, 5]
print(prod(ans))

#2
s = str(input())
cnt = 0
cnt2 = 0
for i in s:
    if i.islower():
        cnt += 1  
    if i.isupper():
        cnt2 += 1  
print(cnt, cnt2)

#3
s = str(input())
t = (''.join(reversed(s)))
if t == s:
    print('yes')
else:
    print('no')

#4
from math import * 
import time
a, b = int(input()), int(input())
time.sleep(float(b / 1000))
print('Square root of', a, 'after', b, 'miliseconds is', sqrt(a))

#5
a = (True, True, True)
b = (False, True, 56)
print(all(a), all(b))

