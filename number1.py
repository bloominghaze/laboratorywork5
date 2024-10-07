while True:
    try:
        N = int(input("Введіть довжину масиву (ціле число): "))
        if N <= 0:
            print("Довжина масиву має бути додатним числом. Спробуйте ще раз.")
        else:
            break
    except ValueError:
        print("Помилка! Введено некоректне значення. Введіть ціле число.")

array = []
print(f"Введіть {N} елементів масиву (цілі числа):")
i = 0
while i < N:
    try:
        element = int(input(f"Елемент {i+1}: "))
        array.append(element)
        i += 1
    except ValueError:
        print("Помилка! Введено не ціле число. Спробуйте ще раз.")

print("Масив:", array)

product = 1
has_nonzero_odd = False

for num in array:
    if num != 0 and num % 2 != 0:
        product *= num
        has_nonzero_odd = True

if has_nonzero_odd:
    print("Добуток ненульових непарних елементів:", product)
else:
    print("Немає ненульових непарних елементів у масиві.")
