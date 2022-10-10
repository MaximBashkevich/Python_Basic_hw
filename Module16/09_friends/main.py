count_friends = int(input('Кол-во друзей: '))
count_receipts = int(input('Долговых расписок: '))


receipts_list = []
for i in range(count_receipts):
    temp = []
    print()
    print(str(i+1) + '-я расписка')
    print('Кому: ',  end = '')
    creditor = int(input())
    temp.append(creditor)
    print('От кого: ', end = '')
    debtor = int(input())
    temp.append(debtor)
    print('Сколько: ', end = '')
    credit = int(input())
    temp.append(credit)
    receipts_list.append(temp)
print(receipts_list)

print('Баланс друзей:')

for i_friend in range(1, count_friends + 1):
    balance = 0
    for i_receipt in range(count_receipts):
        if receipts_list[i_receipt][0] == i_friend:
            balance -= receipts_list[i_receipt][2]
        elif receipts_list[i_receipt][1] == i_friend:
            balance += receipts_list[i_receipt][2]
    print(str(i_friend) + ': ' + str(balance))