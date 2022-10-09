from unittest import TestSuite


print("F U N C T I O N")
#Function selalu dimulai dengan def

#def function.name(parameters):


#TANPA PARAMETER
print("Hai")

def Halo():
    print("Selamat Datang") #Tidak muncul di Teriminal

print('-'*10)
Halo()

print('-'*10)
#DENGAN PARAMETER
def halo2(teks):
    print(teks)

Halo()
halo2('Apa kabar?')

print('-'*10)
#Dengan 2 Parameter
def L_persegi(p,l):
    L=(p*l)
    print(f'Luas dari Persegi yang Lebarnya adalah {l} dan Panjangnya adalah {p} : {L}')

L_persegi(4,3)

def s_persegi(s):
    S=s*s
    return S

print("Luas dari Persegi: %d" % s_persegi(5))

print("- - - - - L A T I H A N - - - - -")
nama_kota=[]

def lihat_kota():
    if len(nama_kota)<=0:
        print("BELUM ADA DATA!")
    else:
        for i in range(len(nama_kota)):
            print("(%d) %s" % (i,nama_kota[i]))

lihat_kota()

def insertKota(kota):
    nama_kota.append(kota)
insertKota('Makassar')

def hapusKota(kota):
    nama_kota.remove(kota)

# TAK PAHAM LE, APE NI
# PERLU DICOBA DI COLLAB.RESEARCH.GOOGLE.COM (.ipynb)

def printinfo( name = "Hacktiv8", age = 25 ):
    print("Nama: ", name)
    print("Umur: ", age)
    return;

printinfo('Venu')

print("- - - - - M O D U L E S - - - - -")
name = 'zack'
devices = ['laptop', 'smartphone', 'tablet']

def display(arg):
    print(f'arg = {arg}')

#pip install feature_engine
#import feature_engine

#https://colab.research.google.com/drive/11YtqVYZLpHbG_hLgnIBBRfnk7l5YTFhP?usp=sharing
