from main import Array
from random import randint

if __name__ == "__main__":
    arr = Array([randint(1,1000) for _ in range(10)])
    print(f"Tablica przed sortowaniem: {arr}")
    arr.merge_sort()
    print(f"Tablica po sortowaniu {arr}")