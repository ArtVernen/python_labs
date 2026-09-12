a=str(input('a: '))
b=str(input('b: '))
a=a.replace(',','.')
b=b.replace(',','.')
a=float(a)
b=float(b)
sum=a+b
avg=(a+b)/2
print('sum=',f'{sum:.2f};',' avg=',f'{avg:.2f}',sep='')

