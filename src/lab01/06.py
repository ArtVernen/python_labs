n=int(input('Введите количество:'))
o=0
z=0
for i in range(1,n+1):
    s=str(input(f'in_{i}:'))
    if s.find('True')!=-1:
        o+=1
    if s.find('False')!=-1:
        z+=1

print(o,z)


