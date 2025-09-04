class Osoba:
    num_instances = 0

    def __init__(self, id: int = 0, name: str = ""):
        self._id = id
        self._name = name
        Osoba.num_instances += 1

    def copy_values(self, object_to_copy_from: "Osoba"):
        self._id = object_to_copy_from._id
        self._name = object_to_copy_from._name
        Osoba.num_instances += 1

    def say_hi(self, your_name: str):
        print(f"Cześć {your_name}, mam na imię {self._name if self._name else "Brak Danych"}")

if __name__ == "__main__":
    print(f"Liczba zarejestrowanych osób to {Osoba.num_instances}")
    osoba_1 = Osoba()
    
    osoba_2_id = input("Podaj id osoby 2: ")
    osoba_2_age = input("Podaj imie osoby 2: ")

    osoba_2 = Osoba(osoba_2_id, osoba_2_age)
    
    osoba_3 = Osoba()
    osoba_3.copy_values(osoba_2)

    for osoba in [osoba_1, osoba_2, osoba_3]:
        osoba.say_hi("Jan")

    print(f"Liczba zarejestrowanych osób to {Osoba.num_instances}")
