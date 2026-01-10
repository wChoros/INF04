class Array:
    def __init__(self, arr: list):
        self.arr = arr

    def __str__(self):
        return str(self.arr)

    def merge_sort(self):
        def merge(arr_a: list, arr_b: list):
            arr_c = []
            i = 0
            j = 0
            while True:
                if i >= len(arr_a):
                    arr_c += arr_b[j:]
                    break
                if j >= len(arr_b):
                    arr_c += arr_a[i:]
                    break
                if arr_a[i] > arr_b[j]:
                    arr_c.append(arr_a[i])
                    i += 1
                else:
                    arr_c.append(arr_b[j])
                    j += 1
            return arr_c

        def sort(arr):
            if len(arr) == 1:
                return arr

            arr_a = arr[0:(len(arr)//2)]
            arr_b = arr[(len(arr)//2):]

            if len(arr_a) != 1:
                arr_a = sort(arr_a)
            if len(arr_b) != 1:
                arr_b = sort(arr_b)

            return merge(arr_a, arr_b)

        self.arr = sort(self.arr)
        return self.arr


if __name__ == "__main__":
    arr = []
    arr = [10, 45, 87, 1, 6, 746, 4578]
    array_obj = Array(arr)
    print(array_obj.merge_sort())
