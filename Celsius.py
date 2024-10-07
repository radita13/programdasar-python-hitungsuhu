# Membuat program konversi suhu dari Celsius ke Fahrenheit, Reamur, dan Kelvin

# Celsius dengan data type float
print("====== PROGRAM KONVERSI SUHU CELSIUS KE FARENHEIT, REAMUR, DAN KELVIN ======")

# Data yang diinputkan harus berupa ! number atau angka !. Jika menginputkan huruf, program akan error.
celsius = float(input("\nMasukkan suhu dalam celsius: "))
print("Suhu dalam celsius adalah",celsius,"derajat")

# Celsius ke Reamur
reamur = (4/5) * celsius
print("Suhu dalam celsius ke reamur adalah",reamur,"derajat")

# Celsius ke Fahrenheit
fahrenheit = ((9/5) * celsius) + 32
print("Suhu dalam celsius ke fahrenheit adalah",fahrenheit,"derajat")

# Celsius ke Kelvin
kelvin = celsius + 273
print("Suhu dalam celsius ke kelvin adalah",kelvin,"derajat\n")

print("====== PROGRAM KONVERSI SUHU CELSIUS KE FARENHEIT, REAMUR, DAN KELVIN ======")