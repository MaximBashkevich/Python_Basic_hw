import random

class Card:
    suit = ['Пики', 'Крести', 'Бубны', 'Черви']
    card_rank = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                 '8': 8, '9': 9, '10':10, 'Валет':10, 'Дама':10, 'Король':10,
                 'Туз': 11}


class Deck:
    desk = [(rank, suit) for rank, score in Card.card_rank.items() for suit in Card.suit]
    card_scores = []




class Player:
    # cards = []

    def __init__(self, name):
        self.name = name
        self.cards = []

    def distribution_card(self):
        randon_card = random.choice(Deck.desk)
        self.cards.append(randon_card)

    def hand(self):
        print('\nКарты на руках:')
        for card in self.cards:
            print(card[0], card[1], end='   ')

    def get_scores(self):
        total_scores = 0
        for card in self.cards:
            total_scores += Card.card_rank[card[0]]
        return total_scores


def black_jack():
    print('Игра началась!')
    player_name = input('Введите ваше имя: ')
    while True:
        player = Player(player_name)
        diller = Player('Диллер')
        loser = True
        distribution = input('\nРаздать карты?(Да/Нет) ')
        if distribution.lower() == 'да':
            for _ in range(2):
                player.distribution_card()
                diller.distribution_card()
            print('\nВ ИГРУ ВСТУПАЕТ {}'.format(player.name.upper()))
            player.hand()
            while True:
                distribution = input('\nЕщё карту?(Да/Нет) ')
                if distribution.lower() == 'да':
                    player.distribution_card()
                    player.hand()
                    if player.get_scores() > 21:
                        print('ПЕРЕБОР!\nВы проиграли.')
                        loser = False
                        break
                    elif player.get_scores() == 21:
                        print('Black Jack!\nВы выйграли.')
                        loser = False
                        break
                else:
                    break

            if loser:
                print('\nВ ИГРУ ВСТУПАЕТ ДИЛЛЕР')
                while True:
                    diller.hand()
                    if diller.get_scores() > 21:
                        print('\nВы выйграли.')
                        break
                    elif diller.get_scores() > player.get_scores():
                        print('\nВы проиграли.')
                        break
                    elif diller.get_scores() == player.get_scores():
                        print('\nНичья.')
                        break
                    elif diller.get_scores() < player.get_scores():
                        diller.distribution_card()
                        print('\nЕще карта.')
        else:
            print('\nИГРА ОКОНЧЕНА')
            break


black_jack()