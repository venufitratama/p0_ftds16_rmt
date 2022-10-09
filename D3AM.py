from re import A
from tkinter import E


print('-'*50)
print("C O N D I T I O N")

if True:
    print('haloo')

print('-'*20)
b = 5
if 3<b:
    print('3 lebih kecil daripada 5')
    print(f'1<{b}')

print('-'*20)
c = 6
d = 6
if c<=d:
    print('nilai c adalah',f'{c}', 'nilai d adalah',f'{d}')

print('-'*20)
e = 7
f = 7
if c>d:
    print('benar', 'nilai e adalah',f'{e}', 'nilai f adalah',f'{f}')
else:
    print('salah')

print('-'*20)
g = 7
h = 7
if g>h:
    print('benar', 'nilai e adalah',f'{e}', 'nilai f adalah',f'{f}')
elif g<h:
    print('benar', 'nilai e adalah',f'{e}', 'nilai f adalah',f'{f}')
else:
    print('salah')

print("LATIHAN CONDITION")
score = 80

if score>=80 and score<=100:
    print('Grade A')
elif score>=60 and score<=80:
    print('Grade B')
elif score>=40 and score<=60:
    print('Grade C')
elif score>=20 and score<=40:
    print('Grade D')
elif score<=20 and score>=0:
    print('Grade E')
else:
    print('Salah input nilai')

k0ta=['A','B','C']
nama_kota='A'

if nama_kota in k0ta:
    print(f'{nama_kota} merupakan bagian dari k0ta')

print('-'*60)
print(" - - - - - L O O P I N G - - - - - ")
print('-'*60)
print("While Loop")

a=1

while a<=10:
    print('berhasil nilai a adalah:', f'{a}')
    a = a+0.5

print("For Loop")

for c in range (1,3):
    print('berhasil nilai c adalah :', f'{c}')

kota=['A','B','C']

for nama_kota in kota:
    print(f'{nama_kota} merupakan bagian dari kota')

print('-'*25)
d = ['1','2','3','4','5','6']
for d in range(1,6):
    print(f'{d+2}')

print('-'*25)
for e in range (1,3):
    print(f'{c*3}')

print('-'*25)
a = 1
b = 1
while a<5:
    while b<6:
        print(f'nilai perkalian {a} x {b} = {b*a}')
        b=b+1
    print('*'*20)
    a=a+1
    b=1
    
print('-'*25)
for a in range (1,5):
    for b in range (1,6):
        print(f'nilai perkalian {a} x {b} = {b*a}')
    print('*'*20)
    a=a+1

print("Flow Control Statement")
print("1. Continue")
print("2. Break")

for b in range (1,6):
    if b == 3:
        continue
    print(f'nilai perkalian {b}')
print('*'*25)
for b in range (1,10):
    if b in (3,6):
        continue
    print(f'nilai perkalian {b}')
print('*'*25)
for b in range (1,10):
    print(f'nilai perkalian {b}')
    if b == 3:
        break

print("LATIHAN FLOW CONTROL STATEMENT")
kamus={'Raka':100,'Hana':90,'Dian':55}

def NilaiGrade(nilai):
    if nilai < 0 or nilai > 100:
        return "error"
    if nilai >= 80 and nilai <= 100:
        return "A"
    if nilai >= 70 and nilai <= 80:
        return "B"
    if nilai >= 60 and nilai < 70:
        return "C"
    if nilai >= 50 and nilai < 60:
        return "D"
    if nilai <50:
        return "E"

kamus={'Raka':100,'Hana':90,'Dian':55}

for key in kamus:
    print(f'{key} grade: {NilaiGrade(kamus[key])}')

#https://colab.research.google.com/drive/1wcMXU7Wu0RJ2wljR0rUFjISIHh5FJn2c?usp=sharing
