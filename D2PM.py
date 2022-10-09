# mencetak string ada beberapa cara

from re import A


print('Ini namanya single code')
print("ini double code")
print('''ada juga yang tiga''')

# Bedanya dimana?
print("Single code atau double tidak bisa 2 line")
print('''tapi ini bisa 
    2 line 
    atau lebih''')
print('coba\
 coba') # single code bisa dipisah dengan \

#Tipe Data
#Integer, String, Float
print('venu' + '14')
print(14 + 2)
print(14.2 + 2)

print(type(0))
print(type(1))
print(type(2.2))
print(type('venu'))
print(type(['venu','john','budi']))

#Variable

Nama = 'Venu Fitratama'
Alamat = 'Pontianak'

print(Nama)
print(Alamat)
print(type(Nama))
print(type(Alamat))
print(Nama+ Alamat)

#Variabel tidak boleh dimulai dari angka
Tahun1 = 'Tahun Lahir'

x=y=z = 3
print(x)
print(y, z)

#camel case
myVariableName = 'Toko'
#pascal case
myVariableName= 'Toko'
#snake case
my_variable_name= 'Toko'

print("Operator Aritmatika")
a = 56
b = 10
print(a+b) 
print(a/b) #Tambah, Bagi, Kurang, Bagi, Sama Saja
print(a//b) #integer (Pembulatan kebawah dari pembagian)
print(a%b) #Modulus, sisa bagi
print(a**b) #Pangkat

print("Casting")
angka_int = 20
print(float(angka_int))
angka_float = 20.5
print(int(angka_float))

print("Pembulatan dengan Round")
y = 20.56748
x = round(y) #Bulatin keatas
print(x)

y = 20.56748
print(y)
x = round(y,3) #Bulatin keatas + 3 angka dibelakang koma
print(x)

print("Comparison")
a = 40
b = 30 
print(a==b)
print(a<=b)
print(a>=b)
print(a!=b)

print("Manipulasi String")
nama= 'venu fitratama'
print(nama.capitalize())
print(nama.lower())

print('-'*50)

print("Slicing") #Di Excel seperti Left/ Right
print("0")
print(nama[0])
print(":1")
print(nama[:1])
print(":2")
print(nama[:2])
print("1:2")
print(nama[1:2])
print("1:4")
print(nama[1:4])
print("1:4:2")
print(nama[1:4:2]) #Loncat 2 tiap element
print("-1")
print(nama[-1])
print("-4:-2")
print(nama[-4:-2])
print(len(nama)) #Caritau berapa panjang karakter 'nama'

print("Format String")
nama = 'venu fitratama'
umur = 25

#Cara 1
print(' Nama Saya Adalah ' +nama + ' Umur saya adalah ' + str(umur))
#Cara 2
print(f'nama Saya Adalah  {nama}  Umur saya adalah  + {umur}')
print('nama saya adalah {}, umur saya adalah {}'. format (nama, umur))
print('nama saya adalah {1}, umur saya adalah {0}'. format (nama, umur))
print('nama saya adalah %s, umur saya adalah %d'. format (nama, umur))

print("List")
listkendaraan = ['motor','becak','sepeda','pesawat','mobil','kereta api']
print(listkendaraan)
print(listkendaraan[0]) #memanggil motor
print(listkendaraan[1:3]) #Memanggil Becak & Sepeda

print("Ubah Nilai Didalam List")
print(listkendaraan)
listkendaraan[2] = 'kapal laut'
print(listkendaraan)
listkendaraan[2:5] = ['kapal laut']
print(listkendaraan)
listkendaraan.insert(1, 'gojek')
print(listkendaraan)
listkendaraan.append('Grab') #Menambahkan di paling akhir
print(listkendaraan)

list1=['sss','ddd','nnn']
list2= ['www','kkk','lll']
list1.append(list2)
print(list1) #List didalam list
list1.extend(list2)
print(list1) #1 Kesatuan List

list3=['aaa','bbb','ccc']
list3.remove('aaa')
print(list3)

print('-'*50) # angka => huruf besar => huruf kecil
print("ASCII Character")
a=['a','B','1','2','c','A']
print(max(a))
print(min(a))
print(a)

print("Tuple")
tuplekendaraan= ('motor','becak','sepeda','pesawat')
listkendaraan2= ('mobil','jalan kaki')
print(tuplekendaraan)
listkendaraan2= list(tuplekendaraan)
listkendaraan2[2]='kapal laut'
print(listkendaraan2)
tuplekendaraan = tuple(listkendaraan)

print("SET")
mySet = {'motor','becak','sepeda','pesawat','mobil','kereta api'} #Tidak urut
print(mySet)

print("Cari tau dictionary di macOS")
print("PR Caritau kegunaan masing-masing data-data diatas")
#Sering sering latihan Tuple, List, Dictionary, Slicing

print("Dictionaries")
myDict = {"Venu":14, "Fiola":16, "Coki":1}
print(myDict)
print(myDict.keys())

