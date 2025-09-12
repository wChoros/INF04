import random


class ListExcerisise:
    def __init__(
        self,
        list_len: int,
    ):
        self.numbers_list = []
        self.__number_list_len = list_len

        for i in range(list_len):
            self.numbers_list.append(random.randint(1, 1000))

    def print(self) -> None:
        for i, number in enumerate(self.numbers_list):
            print(f"{i}: {number}")

#   **********************************************************************************
#   nazwa metody:                   find
#   opis metody:                    metoda szukająca pierwszego elementu tablicy o podanej wartości
#   parametry:                      number_to_find - wartość szukanego elementu
#   zwracany typ i opis:            int - index znalezionego elementu lub -1 gdy nie znaleziono
#   autor:                          00000000000
#   **********************************************************************************
    def find(self, number_to_find: int):
        for i, number in enumerate(self.numbers_list):
            if number == number_to_find:
                return i
        return -1

    def avg(self):
        return sum(self.numbers_list) / self.__number_list_len

    def print_odd(self) -> int:
        counter = 0
        for number in self.numbers_list:
            if number % 2 == 1:
                print(number)
                counter += 1
        return counter

if __name__ == "__main__":
    list_excerisise = ListExcerisise(50)
    list_excerisise.print()

    found = list_excerisise.find(420)
    if found != -1:
        print(f"Znaleziono 420 na indexsie: {found}")

    print("Liczby nieparzyste:")
    number_of_odds = list_excerisise.print_odd()
    print(f"Razem nieparzystych: {number_of_odds}")
    
    print(f"Średnia wszystkich elementów: {list_excerisise.avg()}")