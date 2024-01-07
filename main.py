import sys


def main():
    def remove_duplicates(array):
        unique_elements = []
        underscore_count = 0

        for num in array:
            if num not in unique_elements:
                unique_elements.append(num)
            else:
                underscore_count += 1

        result = unique_elements + ['_'] * underscore_count
        return result

    n = int(sys.stdin.readline().rstrip())
    input_data = sys.stdin.readline().rstrip()

    sorted_array = list(map(int, input_data.split()))

    # Проверка длины массива
    if len(sorted_array) != n:
        print(
            "Ошибка: полученная длина массива не соответствует указанному значению n.")
        sys.exit(1)

    result = remove_duplicates(sorted_array)
    output = ' '.join(map(str, result))
    print(output)


if __name__ == '__main__':
    main()
