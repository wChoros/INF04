def nwd(a: int, b: int):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


if __name__ == "__main__":
    first_number = input("Podaj pierwszą liczbę: ")
    second_number = input("Podaj drugą liczbę: ")
    print(
        f"Wynik NWD z {first_number} i {second_number} to {nwd(int(first_number), int(second_number))}"
    )
