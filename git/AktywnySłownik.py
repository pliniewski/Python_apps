definicje =  {}

while(True):
    print("1: Dodaj definicję")
    print("2: Znajdź definicję")
    print("3: Usuń definicję")
    print("4: Zakończ program")
    print()

    wybor = input("Co chcesz zrobić?")
    print()
    if wybor == "1":
        klucz = input("Podaj klucz do zdefiniowania: ")
        definicja = input("Podaj definicja do zdefiniowania: ")
        definicje[klucz] = definicja
        print("Deninicja dodana pomyślnie")
        print()
    elif wybor == "2":
        klucz = input("Czego szukasz? ")
        if klucz in definicje:
            print(definicje[klucz])
            print()
        else:
            print("Nie znaleziono definicji o nazwie: ", klucz)
            print()
    elif wybor == "3":
        klucz = input("Podaj klucz do usunięcia: ")
        if klucz in definicje:
            del(definicje[klucz])
            print("Usunięto definicję o nazwie: ", klucz)
            print()
        else:
            print("Nie znaleziono definicji o nazwie: ", klucz)
            print()
    elif wybor == "4":
        print("Do zobaczenia!")
        break
    else:
        print("Podałeś nieprawidłowy numer. Spróbuj jeszcze raz.")
        print()
