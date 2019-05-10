#! python3
import sys

number = 10000;
orig_stdout = sys.stdout

f = open('out.txt', 'w')
sys.stdout = f

a = 1
b = 1
i = 1
Listf=[a,b]
while i<1000:
    c = a + b
    a = b
    b = c
    i = i + 1
    Listf.extend([c])
     
print(Listf)