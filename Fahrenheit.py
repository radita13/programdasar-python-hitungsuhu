# Membuat program konversi suhu dari Fahrenheit ke Celsius, Reamur, dan Kelvin

# Fahrenheit dengan type data float
print("====== PROGRAM KONVERSI SUHU FAHRENHEIT KE CELSIUS, REAMUR, DAN KELVIN ======")

# Data yang diinputkan harus berupa ! number atau angka !. Jika menginputkan huruf, program akan error.
fahrenheit = float(input("\nMasukkan suhu dalam fahrenheit: "))
print("Suhu dalam fahrenheit adalah",fahrenheit,"derajat")

# Fahrenheit ke Celsius
celsius = (5/9) * (fahrenheit - 32)
print("Suhu dalam fahrenheit ke celsius adalah",celsius,"derajat")

# Fahrenheit ke Reamur
reamur = (4/9) * (fahrenheit - 32)
print("Suhu dalam fahrenheit ke reamur adalah",reamur,"derajat")

# Fahrenheit ke Kelvin
kelvin = ((5/9) * (fahrenheit - 32)) + 273
print("Suhu dalam fahrenheit ke kelvin adalah",kelvin,"derajat\n")

print("====== PROGRAM KONVERSI SUHU FAHRENHEIT KE CELSIUS, REAMUR, DAN KELVIN ======")