#zadanie 1.1
hello = "Hello"
student = "Kamil"
wynik = "{}, {}".format(hello,student)
print(wynik)

#zadanie 1.2
student = input("Podaj imię: ")
komunikat = "Hello, {}!".format(student)
print(komunikat)

#zadanie 1.3
studenci = ["Ania", "Kuba", "Piotr", "Jan"]
liczba_studentow = len(studenci)
print("Liczba studentów wynosi: ", liczba_studentow)

#zadanie 1.4
studenci = ["Ania", "Kuba", "Piotr", "Jan"]

for student in studenci:
    print("Hello", student)

#zadanie 1.5
liczba = 3
potega = 4
wynik = liczba**potega
print("Wynik wynosi: ", wynik)

#zadanie 1.6
ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = 0

for znak in ciag_znakow:
    if znak == "(":
        liczba_nawiasow_otwierajacych += 1

print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))