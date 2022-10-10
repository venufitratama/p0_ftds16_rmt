#Kelvin to Celcius
Kelvin = float(input('Masukkan suhu dalam Kelvin : '))
Celcius = (Kelvin - 273.15)
print('Celcius : ', Celcius, 'C')

#Celcius to Kelvin
Celcius = float(input('Masukkan suhu dalam Celcius : '))
Kelvin = (Celcius + 273.15)
print('Kelvin : ', Kelvin, 'K')

#Celcius to Fahrenheit
Fahrenheit = ((9/5)) * Celcius + 32
print("Suhu" , Celcius, "C dalam Fahrenheit adalah ", Fahrenheit, "F")
#Kelvin to Fahrenheit
Fahrenheit = (Kelvin-273.15) * 9/5 + 32
print("Suhu" , Kelvin, "K dalam Fahrenheit adalah", Fahrenheit, "F")

#Fahrenheit ke Celcius
Celcius = (Fahrenheit - 32) * 5/9
print("Suhu" , Fahrenheit, "F dalam Celcius adalah ", Celcius, "C")
#Fahrenheit ke Kelvin
Kelvin = (Fahrenheit - 32) * 5/9 + 273.15
print("Suhu" , Fahrenheit, "F dalam Kelvin adalah ", Kelvin, "K")
