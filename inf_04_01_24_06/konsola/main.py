import random


# ************************************************
# nazwa: throw_cubes
# opis: metoda służąca do losowania tablicy liczb całkowitych <1, 6> w ilości podanej w argumencie
# parametry: number_of_cubes - ilość liczb do wylosowania do tablicy
# zwracany typ i opis: list[int] - lista liczb całkowitych z przedziału <1, 6>, o długości podanej w argumencie
# autor: 00000000000
# ************************************************
def throw_cubes(number_of_cubes: int):
    cubes = []
    for _ in range(number_of_cubes):
        cubes.append(random.randint(1, 6))
    return cubes


def sum_cubes(cubes: list[int]):
    total = 0
    for cube in cubes:
        total += cube

    return total


if __name__ == "__main__":
    is_game_on = True
    while is_game_on:
        num_of_cubes = input("Ile kostek chcesz rzucić?(3 - 10)\n")
        try:
            num_of_cubes = int(num_of_cubes)
        except Exception:
            num_of_cubes = 0

        if num_of_cubes not in range(3, 11):
            continue

        cubes = throw_cubes(num_of_cubes)
        for i, cube_value in enumerate(cubes):
            print(f"Kostka {i + 1}: {cube_value}")

        print(f"Liczba uzyskanych punktów: {sum_cubes(cubes)}")

        if input("Jeszcze raz? (t/n)\n") == "n":
            is_game_on = False
