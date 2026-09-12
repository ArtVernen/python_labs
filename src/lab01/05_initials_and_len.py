a=str(input('ФИО: '))
s=''
k=0
for i in a:
    if i.isupper():
        s+=i
for i in a:
    if i!=' ':
        k+=1
print('Инициалы: ',s ,'.',sep='')
print('Длина (символов):', k+2)