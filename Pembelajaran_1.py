#Multi Variable
a, b, c = "apel","belimbing","ceri"
print(a)
print(b)
print(c)

#Quiz 2
x = 2
y = 6
print(str(x+y)+"5"*4)

#Output
a = 20
print("Nilai a adalah", a)

a= 20 
b= 10
print("Nilai a adalah {0} dan b adalah {1}".format(a,b))

a = 20
b = 10
print(f"Nilai a adalah {a} dan b adalah {b}")

#Input
nama = input("Masukan nama Anda: ")

print(f"Selamat datang, {nama}")

umur = input("Masukan umur Anda: ")

print(f"Umur anda: {umur}")
print(type(umur))

umur = int(input("Masukan umur Anda: "))

print(f"Umur anda: {umur}")
print(type(umur))

#Tipe Data
# a="Halo"
# a=2
# a=25
# a=2j
# a=["apel","belimbing","cherry"]
# a=("apel","belimbing","cherry")
# a={"apel","belimbing","cherry"}
# a={"apel","belimbing","cherry": 2}

#Multiline Strings
a = """Ini adalah contoh
dari multiline
string"""

print(a)

b= '''Ini adalah contoh
dari multiline
string'''

print(b)

#Slicing String
#Slicing dengan ranger tertentu, a[index_start:index_finish]
a = "Halo, Selamat pagi"

print(a[1:4])
#Hasilnya adalah "alo"

a = "Halo, Selamat pagi"

print(a[:5])
#Hasilnya adalah "Halo,"

a = "Halo, Selamat pagi"

print(a[10:])
#Hasilnya adalah "mat pagi"

#Modifikasi String

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World!"
b =  "Hello, World! "
print(a.strip())
print(b.strip())

a = " Hello, World!"

print(a.replace("H", "J"))
print(a.split())

#Escape Characters
text="Helo, Selamat Datang \"Bella\" dari Bnadung."
print(text)

text="Helo, Selamat Datang Bella \n dari Bnadung."
print(text)

#Identasi
"""Hakikat untuk IF Statemane seperti:
IF >= 0
   print("hello")"""