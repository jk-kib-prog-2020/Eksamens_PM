#1
print("Mācies, kamēr gudrs tiec,\n Visu labi vērā liec.\nDzīve gudra, viltīga -\n Gudrība tur derīga!")
#2
import sys
print(sys.version)
#3
import math
r = int(input("Ievadiet riņķa radiusu: "))
laukums = math.pi * r * r
print("Laukums ir: ",laukums)
#4
v = (input("Ievadiet vārdu: "))
print(v[::-1])
#5
sk = input("Ievadiet 10 skaitļus ar atsarpēm: ").split(' ')
sum = 0
for i in range(10):
    sum += int(sk[i])
print("Summa: ",sum)
#6
preces = ["ābloi", "bumbieri", "siers", "piens", "kefirs"]
print(preces[0], preces[-1])
#7
x = int(input("Ievadiet skaitli: "))
print(x*x + (x / 2) *2)
#8
y = int(input("Ievadiet skaitli: "))
if 99 < y < 1001: 
    print("Skaitlis atrodas intervālā no 100 līdz 1000")
else:
    print("Skaitlis NEatrodas intervālā no 100 līdz 1000")
#9
mm = int(input("Ievadiet savu augumu centimetros: "))
kg = int(input("Ievadiet savu svaru kilogramos: "))
print("Tavs Ķermeņa Masas Indeks ir: ",kg / mm / mm * 10000 )
#10
print("Man viss izdodas!")