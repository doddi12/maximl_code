# -*- coding: utf-8 -*-
"""maximl_test

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IOf2RC6O8EnwYu-XuFlIyHbB_apKNYiQ
"""



a=input()
b=[]
n=len(a)
for i in range(0,n):
  for j in range(i+1,n+1):
    l=a[i:j]
    b.append(l)
c=[]
for i in b:
  d=set(i)
  c.append(len(d))
print(max(c))

"""# New Section"""



