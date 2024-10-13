#1)
# a = input("Podaj imię : ")
#print("Hello world", a)

#2)
#var_one =2
#var_two = 3
#var_one += 2
#var_three = var_one
#var_one *= 3
#var_four = var_one/var_two

#3 a)
#age = int(input("Wprowadz swoj wiek: "))
#if age >=18 and 100:
#    print("Autoryzacja uzyskana")
#else: print("Odmowa")

#b)
#a = int(input("Wprowadz liczbe:"))
#if a > 0:
#    print("|a|=", a)
#else: print("|a|=", -a)

#c)
#a = int(input("Podaj liczbę : "))
#b = 10
#if a > b:
#    print("Hello world")
#else: print("You are donkey")


#d)
#a = int(input("Podaj liczbe : "))
#if a > (a+1):
#    print("Jest przysta")
#else: print ("Jest nie parzysta")

#e)
#a = float(input("Podaj liczbe a :"))
#b = float(input("Podaj liczbe b :"))
#if a > b:
#    print(a)
#else: print(b)

#f)
#a = float(input("Podaj liczbe : "))
#if 1 <= a <=10:
#    print("Należy do przedziału [1,10]")
#elif 17 <= a <= 21:
#    print("Należy do przedziału [17,21]")
#else:
#    print("Liczba nie należy do żadnego przedziału")

#g)
#a = int(input("Podaj liczbę całkowitą: "))
#if a % 3 == 0 and a % 5 == 0:
#    print("Liczba jest podzielna przez 3 oraz 5")
#if a % 3 == 0 and a % 5 !=0:
#    print("Liczbna jest podzielna przez 3 ale nie przez 5")
#if a % 3 !=0 and a % 5 == 0:
#    print("Liczba nie jest podzielna przez 3 ale jest przez 5")
#if a % 3 != 0 and a % 5 != 0:
#    print("Liczba nie jest podzielna przez 3 ani 5")

#h)
#a = float(input("Podaj liczbe: "))
#x =input("Podaj znak (+,-,*,/): ")
#b = float(input("Podaj liczbe: "))
#if x == "+":
#    wynik = a + b
#    print(f"Wynik dodawania: {wynik}")
#elif x == "-":
#    wynik = a - b
#    print(f"Wynik odejmowania: {wynik}")
#elif x == "*":
#    wynik = a * b
#    print(f"Wynik mnożenia: {wynik}")
#elif x == "/":
#    wynik = a / b
#    print(f"wynik dzielenia: {wynik}")

#i)
#a = float(input("Podaj temperaturę: "))
#x = input("Podaj na co przekonwertować(f,c): ")
#if x == "f":
#    wynik = (9 / 5 * a + 32)
#    print(f"Twoje Fahrenheit to: {wynik}")
#elif x == "c":
#    wynik = (a - 32) * 5 / 9
#    print(f"Twoje Celsjusze to: {wynik}")

#j)
#x = int(input("Podaj pierwszą liczbę  całkowitą: "))
#y = int(input("Podaj drugą liczbę całkowitą: "))
#z = int(input("Podaj trzecią liczbę całkowitą: "))
#if  x**2 + y**2 == z**2:
#    print("Liczby stanowią trojkę pitagorejska")
#elif x**2 + z**2 == y**2:
#    print("Liczby stanowią trojkę pitagorejska")
#elif y**2 + x**2 == z**2:
#    print("Liczby stanowią trojkę pitagorejska")
#elif y**2 + z++2 == x**2:
#    print("Liczby stanowią trojkę pitagorejska")
#elif z**2 + x**2 == y**2:
#    print("Liczby stanowią trojkę pitagorejska")
#elif z**2 + y**2 == x**2:
#    print("Liczby stanowią trojkę pitagorejska")
#elif  x**2 + y**2 != z**2:
#    print("Liczby nie stanowi trojke pitagorejska")
#elif x**2 + z**2 != y**2:
#    print("Liczby nie stanowi trojkę pitagorejska")
#elif y**2 + x**2 != z**2:
#    print("Liczby nie stanowi trojkę pitagorejska")
#elif y**2 + z++2 != x**2:
#    print("Liczby nie stanowi trojkę pitagorejska")
#elif z**2 + x**2 != y**2:
#    print("Liczby nie stanowi trojkę pitagorejska")
#elif z**2 + y**2 != x**2:
#    print("Liczby nie stanowi trojkę pitagorejska")