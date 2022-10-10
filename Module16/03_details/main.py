shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

total_sum = 0
count_detail = 0
detail = input('Название детали: ')
for i_product in shop:
         if i_product[0] == detail:
                count_detail += 1
                total_sum += i_product[1]

print('Количество деталей - ', count_detail)
print('Общая стоимость -', total_sum)