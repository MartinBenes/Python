#print("Ahoj")
#print(25)
#print(2.5)

#print(25 + 2.5)
#print(25/5)
#print(34%8)
#print("Ahoj" + " jak se máš?")

#p = 25
#z = "textik"

#x = "aaa" # mám proměnnou
#print("Ahoj, " + x) # vypíšu text a proměnnou
#x = "Jack" # změním proměnnou
#print("Ahoj, " + x) # vypíšu novou proměnnou
#x = x + "u" # ke staré proměnné přidám 
#print("Ahoj, " + x)

#x = -34 # tohle je cislo, bez uvozovek
#y = 25 

# jedno reseni je zacinat s cislem jako string
# tj ze ho dam do uvozovek a pak pridam str() abych z toho mel text

x = input("Vložte číslo x: ")
y = input("Vložte číslo y: ")

if x > y:
    print(str(x) + " je větší než " + str(y))
if x < y:
    print(str(x) + " je menší než " + str(y))
if x == y:
    print(str(x) + " se rovná " + str(y))

# input --> vlozit hodnotu + napoveda v zavorce
jmeno = input("Napište své jméno: ")
# vystup
print("Ahoj " + jmeno)