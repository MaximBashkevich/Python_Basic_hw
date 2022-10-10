def subsequence(number, start=1):
    if number == start:
        print(start)
        return

    print(start)
    return subsequence(number, start + 1)


start = 1
number = int(input('Введите число: '))
subsequence(number)
