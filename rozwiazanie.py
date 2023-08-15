# 1. Tworzymy listę w której przechowamy uczniów, od razu indeks zerowy zajmujemy "".
uczniowie = [""]

# 2. Przechodzimy przez kolejne linijki, czyli uczniów z listy.
for uczen in open("lista_uczniow.txt", "r"):
  # 3. Z odczytanej linijki tworzymy dwuelementową listę w formacie - [imie, nazwisko\n]
  uczen = uczen.split(" ")
  # 4. Z nazwiska musimy usunąć znak nowej linii.
  uczen[1] = uczen[1].rstrip("\n")
  # 5. Konwertujemy "ucznia" z listy na krotkę.
  uczen = tuple(uczen)
  # 6. Dodajemy go do listy
  uczniowie.append(uczen)

# 7. Wyświetlamy uczniów tak jak wcześniej, jedynie pominąłem stworzenie niepotrzebnych zmiennych 
# imie i nazwisko.
for numer, uczen in enumerate(uczniowie):
    if numer == 0:
        continue
    
    print(numer, ":", uczen[0], uczen[1])

