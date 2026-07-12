import re
print("poczatek")

plik = "U.S. Military Deaths by cause 1980-2010.csv"
F = open(plik, "r", encoding='utf-8')

linie = F.readlines()
naglowki = linie.pop(0) #usuwamy wszystkie slowa z pierwszej linii i zapisujemy je do nazwy naglowki
kategorie = re.split(r"," , naglowki) #dzielimy naglowki na kategorie

hasz = dict()
    
#teraz idziemy przez wszystkie linie
for i in range(len(linie)):
    kolumny = re.split(r"," , linie[i]) #dzielimy linie na kolumny

    hasz[kolumny[0]] = dict() 
    for j in range(6, len(kategorie)): #dzielimy kategorie od 6 miejsca gdzie jest accident i idziemy do konca kategori, j to jest wartosc z danej kategori
        hasz[kolumny[0]][kategorie[j]] = int(float(kolumny[j])) #kol[0] to rok, kat[j] to jest kategoria, kol[j] wartosc z danej kategorii, int zeby widzial jak liczby a nie napis

for rok in hasz:
    print(rok, hasz[rok])

suma = dict() #suma dla kategorii

#Szukmy najczesctrzej przyczny smierci w kazdej kategorii, czyli sumujemy wartosci z danej kategorii idac latami
for i in range(6, len(kategorie)): #czyta jedna kategorie
    suma[kategorie[i]] = 0 #ustawiamy poczatkowa wartosc sumy na 0
    for rok in hasz.keys(): #czyta wszystkie lata dla danej kategorii
        suma[kategorie[i]] = suma[kategorie[i]] + hasz[rok][kategorie[i]] #dodaje wartosci z danej kategorii do sumy idac latami

print()
print("suma:", suma)

maxzgony = 0 
maxkategoria = ""

for kat in suma: #szukamy max wartosci dla danej kategorii i zapisujemy ja do maxzgony po czym idziemy dalej i ktora jest wieksza sie zapisuje
    if maxzgony < suma[kat]:#badamy czy wartosc zgonow jest wieksza od maxzgonow
        maxzgony = suma[kat]#jeski jest to zapisujemy
        maxkategoria = kat #jesli jest to zapisujemy nazwe 

print()
print("Najczesciej wystepujaca przyczyna smierci:", maxkategoria, "z", maxzgony, "zgonami")


maxzgonyrok = 0
maxrok = ""

for rok in hasz: #szukamy roku w ktorym umarlo nawiecej zolnierzy i zapisujemy do maxzgonyrok 
   sumarok = 0 
   for j in range(6, len(kategorie)): #czyta wlasciwe kategorie
       sumarok = sumarok + hasz[rok][kategorie[j]] #dodaje wartosci z danej kategorii do sumy dla danego roku
   if maxzgonyrok < sumarok: #badamy czy wartosc zgonow jest wieksza od maxzgonow
        maxzgonyrok = sumarok #jesli jest to zapisujemy
        maxrok = rok #jesli jest to zapisujemy rok
print("Rok z najwieksza liczba zgonow: ", maxrok)

#Gnuplot
W = open("wykres.txt", "w", encoding="utf-8")
W.write(" #Rok łączna liczba zgonów\n")

for rok in hasz: #petla po kolej widzi lata
    sumarok = 0 # dla kazdego roku ustawiay licznik zgonow = 0
    for j in range(6,len(kategorie)):
        sumarok = sumarok + hasz[rok][kategorie[j]]

    W.write(rok + " " + str(sumarok)+ "\n")

Gnu = open('maluj.plt', 'w', encoding='utf-8') #otwieramy plik do zapisu
Gnu.write('set terminal postscript eps enhanced solid lw 2.2 color font "Helvetica,22"\n')#ustawiamy parametry wykresu, grubosci i kolory i czcionki
Gnu.write('set out "wykres.eps"\n')#ustawiamy nazwe pliku do ktorego zapisujemy wykres
Gnu.write('set xlabel "Lata" font "Helvetica,22"\n')#podpisanie osi X
Gnu.write('set ylabel "Liczba zgonow" font "Helvetica,22"\n') #podpisanie osi Y
Gnu.write("set boxwidth 0.7 relative\n") #Ustawia szerokość każdego słupka na 70% dostępnego miejsca. Dzięki temu słupki nie zlewają się w jedną wielką plamę, tylko mają między sobą estetyczne odstępy.
Gnu.write("set style fill solid 0.8\n") # Wypełnia wnętrze słupków kolorem.
Gnu.write("plot 'wykres.txt' u 1:2 w boxes lc rgb '#2342ba' title '' \n") #narysuj wykres na podstawoe pliku wykres.txt, 1 ocznacza oś x 2 os Y, lp linia i punkty
#lt rgb to kolor linii, lw to grubosc a ps to wielkosc punktow

F.close()
W.close()
Gnu.close()
import subprocess
command = "gnuplot < maluj.plt"
result = subprocess.run(command, capture_output=True, shell=True, text=True)

print("Koniec")
