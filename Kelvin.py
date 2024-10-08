# Membuat program konversi suhu dari Kelvin ke Celsius, Reamur, dan Fahrenheit

# Kelvin dengan type data float
print("====== PROGRAM KONVERSI SUHU KELVIN KE CELSIUS, REAMUR, DAN FARENHEIT ======")

# Data yang diinputkan harus berupa ! number atau angka !. Jika menginputkan huruf, program akan error.
kelvin = float(input("\nMasukkan suhu dalam kelvin: "))
print("Suhu dalam kelvin adalah",kelvin,"derajat")

# Kelvin ke Celsius
celsius = kelvin - 273
print("Suhu dalam kelvin ke celsius adalah",celsius,"derajat")

# Kelvin ke Reamur
reamur = (5/4) * (kelvin - 273)
print("Suhu dalam kelvin ke reamur adalah",reamur,"derajat")

# Kelvin ke Fahrenheit
fahrenheit = ((9/5) * (kelvin - 273)) + 32
print("Suhu dalam kelvin ke fahrenheit adalah",fahrenheit,"derajat\n")

print("====== PROGRAM KONVERSI SUHU KELVIN KE CELSIUS, REAMUR, DAN FARENHEIT ======")
#