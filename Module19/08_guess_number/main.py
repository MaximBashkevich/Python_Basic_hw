import random
max_num = int(input('Введите максимальное число: '))
answer = random.randint(1, max_num)
#boris = (input('Нужное число есть среди вот этих чисел: '))
nums = {0}
while True:
    boris = (input('\nНужное число есть среди вот этих чисел: '))
    if boris == 'Помогите!':
        break
    #boris_lst = boris.split()
    boris_nums = {(int(nums)) for nums in boris.split()}
    #print(boris_nums)
    if answer in boris_nums:
        print('Ответ Артема: Да')
        nums.update(boris_nums)
    else:
        print('Ответ Артема: Нет')
        nums.difference_update(boris_nums)

print('Артём мог загадать следующие числа: ', end='')
nums.discard(0)
for i_num in nums:
    print(i_num, end=' ')

