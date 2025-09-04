class MyList:
    def __init__(self, list_len: int):
        self.my_list = []
        for i in range(list_len):
            self.my_list.append(int(input(f"Podaj {i+1} element tablicy: ")))

    @staticmethod
    def _find_max(my_list: list):
        curr_min = 0
        for i, value in enumerate(my_list):
            if value > my_list[curr_min]:
                curr_min = i
        return curr_min, my_list[curr_min]

    def sort(self):
        for i in range(self.my_list.__len__()):
            curr_min_index, curr_min = MyList._find_max(self.my_list[i:])

            tmp = self.my_list[i]
            self.my_list[i] = curr_min
            self.my_list[curr_min_index + i] = tmp

    def print(self):
        print(self.my_list)


if __name__ == "__main__":
    my_list_1 = MyList(10)
    my_list_1.print()
    my_list_1.sort()
    my_list_1.print()
