class Cell:
    def __init__(self, index):
        self.value = ' '
        self.index = index


class Board:
    board_cells = [Cell(index) for index in range(1, 10)]

    def print_board(self):
        # matrix = [[cell for cell in self.board_cells] for _ in range(3)]
        for line in range(6, -1, -3):
            print('\n-------', end='')
            print('\n|', end='')
            for index_cell in range(line, line + 3):
                print(self.board_cells[index_cell].value, end='|')

    def check_cell(self, number, char):
        if self.board_cells[number].value == ' ':
            self.board_cells[number].value = char
            return True


class Player:
    #  У игрока может быть
    #   - имя
    #   - на какую клетку ходит
    def __init__(self, name):
        self.name = name
        self.cells = []

    def write_cell(self, number):
        self.cells.append(number)

    def check_win(self):
        winer_line = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
        winer = True
        for line in winer_line:
            for number in line:
                if number in self.cells:
                    winer = True
                else:
                    winer = False
                    break
            if winer:
                return True


def play():
    player_X = input('Введите имя первого игрока: ')
    player_0 = input('Введите имя второго игрока: ')
    board = Board()
    player_X = Player(player_X)
    player_0 = Player(player_0)
    for step in range(9):
        player_X_move = int(input('\n{} введите номер клетки(от 1 до 9): '.format(player_X.name))) - 1
        while True:
            if board.check_cell(player_X_move, 'X'):
                player_X.write_cell(player_X_move)
                print(player_X.cells)
                board.print_board()
                break
            else:
                player_X_move = int(input('Клетка занята, введите заново: '))

        if step > 1:
            if player_X.check_win():
                print('\n{} победил!\nИГРА ОКОНЧЕНА'.format(player_X.name))

        player_0_move = int(input('\n{} введите номер клетки(от 1 до 9): '.format(player_0.name))) - 1
        while True:
            if board.check_cell(player_0_move, '0'):
                player_0.write_cell(player_0_move)
                board.print_board()
                break
            else:
                player_0_move = int(input('Клетка занята, введите заново: '))

        if step > 1:
            if player_X.check_win():
                print('\n{} победил!\nИГРА ОКОНЧЕНА'.format(player_0.name))


play()
