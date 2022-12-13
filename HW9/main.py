import os


class TicTacToeBoard:
    def __init__(self):
        self.field = [['[ ]' for _ in range(3)] for _ in range(3)]
        self.turn = -1
        self.game_status = True

    def show_field(self):
        print('  1  2  3')
        for ind in range(len(self.field)):
            print(f'{chr(ord("A") + ind)}{"".join(self.field[ind])}')

    def get_field(self):
        return self.field

    def new_game(self):
        self.field = [['[ ]' for _ in range(3)] for _ in range(3)]
        self.turn = -1

    def check_winner(self):
        f = self.field
        for i in range(3):
            if (f[i][0] == f[i][1] == f[i][2] == ('[X]' or '[O]')) or (
                    f[0][i] == f[1][i] == f[2][i] == ('[X]' or '[O]')):
                return True
        if (f[0][0] == f[1][1] == f[2][2] == ('[X]' or '[O]')) or (
                f[0][2] == f[1][1] == f[2][0] == ('[X]' or '[O]')):
            return True
        else:
            return False

    def check_field(self):
        winner = self.check_winner()
        if winner:
            return 'X' if self.turn > 0 else 'O'
        else:
            for i in self.field:
                for y in i:
                    if y == '[ ]':
                        return None
            return 'D'

    def make_move_second(self, row_: str, col: str) -> object:
        self.turn *= -1
        if ((len(row_) and row_.lower() not in 'abc') or (
                len(col)) != 1 and col not in '123'):
            print('Не корректные данные')
            return False
        if row_.lower() in 'abc':
            row = ord(row_.lower()) - ord('a')
        if (0 > row > 2) or (0 > int(col) - 1 > 2):
            print('Не корректные данные')
            return False
        col = int(col) - 1
        if self.field[row][col] != '[ ]':
            print(f'Ячейка {chr(row + ord("a")).upper()}{col + 1} уже занята')
            return False
        else:
            self.field[row][col] = '[X]' if self.turn > 0 else '[O]'
            return True

    def make_move(self, row: int, col: int) -> object:
        self.turn *= -1
        if not self.game_status:
            return 'Игра уже завершена'
        if (1 > row > 3) or (1 > col > 3):
            self.turn *= -1
            return 'Не корректные данные'
        col_ = col - 1
        row_ = row - 1
        if self.field[row_][col_] != '[ ]':
            self.turn *= -1
            return f'Ячейка {chr(row + ord("a")).upper()}{col + 1} уже занята'
        else:
            self.field[row_][col_] = '[X]' if self.turn > 0 else '[O]'
            check = self.check_field()
            if check != None: self.game_status = False
            if check == None: return 'Продолжаем играть'
            elif check == 'X': return 'Победил игрок X'
            elif check == 'O': return 'Победил игрок O'
            elif check == 'D': return 'Ничья'

            return True

    def run(self):
        while True:
            os.system('cls||clear')
            self.show_field()
            print(f'Ход {"первого" if self.turn > 0 else "второго"} игрока')
            while True:
                row = input('Введите номер строки: ')
                col = input('Введите номер столбца: ')
                if self.make_move_second(row, col):
                    break
            if self.check_winner() or self.check_field() == 'D':
                if self.check_field() == 'D':
                    print('Dead heat')
                else:
                    print(f'Поздравления! {"Первый" if self.turn > 0 else "Второй"} игрок победил!')
                quest = input('Начать сначала?: y/n ')
                if quest.lower() == 'y':
                    self.new_game()
                else:
                    break
            # self.turn *= -1



game = TicTacToeBoard()
game.run()


board = TicTacToeBoard()
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(board.make_move(1, 2))
print(*board.get_field(), sep="\n")
print(board.make_move(2, 1))
print(board.make_move(2, 2))
print(board.make_move(3, 1))
print(board.make_move(2, 2))
print(*board.get_field(), sep="\n")
print(board.check_field())