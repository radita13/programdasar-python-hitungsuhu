# Membuat program konversi suhu dari Reamur ke Celsius, Fahrenheit, dan Kelvin

# Reamur dengan type data float
print("====== PROGRAM KONVERSI SUHU REAMUR KE CELSIUS, FARENHEIT, DAN KELVIN ======")

# Data yang diinputkan harus berupa ! number atau angka !. Jika menginputkan huruf, program akan error.
reamur = float(input("\nMasukkan suhu dalam reamur: "))
print("Suhu dalam reamur adalah",reamur,"derajat")

# Reamur ke Celsius
celsius = (5/4) * reamur
print("Suhu dalam reamur ke celsius adalah",celsius,"derajat")

# Reamur ke Fahrenheit
fahrenheit = ((9/4) * reamur) + 32
print("Suhu dalam reamur ke fahrenheit adalah",fahrenheit,"derajat")

# Reamur ke Kelvin
kelvin = reamur + 273
print("Suhu dalam reamur ke kelvin adalah",kelvin,"derajat\n")

print("====== PROGRAM KONVERSI SUHU REAMUR KE CELSIUS, FARENHEIT, DAN KELVIN ======")