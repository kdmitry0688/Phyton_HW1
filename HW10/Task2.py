class Table(object):

    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._table = [[0] * cols for _ in range(rows)]

    def get_value(self, row, col):
        return (self._table[row][col] if 0 <= row < self._rows and 0 <= col < self._cols
                else None)

    def set_value(self, row, col, value):
        self._table[row][col] = value

    def n_rows(self):
        return self._rows

    def n_cols(self):
        return self._cols

    def delete_row(self, row):
        self._table.pop(row)
        self._rows -= 1

    def delete_col(self, col):
        for row in range(self._rows):
            self._table[row].pop(col)
        self._cols -= 1

    def add_row(self, row):
        self._table.insert(row, [0] * self._cols)
        self._rows += 1

    def add_col(self, col):
        for row in range(self._rows):
            self._table[row].insert(col, 0)
        self._cols += 1

    def print_array(self):
        for i in range(self.n_rows()):
            for j in range(self.n_cols()):
                print(self.get_value(i, j), end=' ')
            print()
        print()

    def print_array_full(self):
        for i in range(-1, self.n_rows() + 1):
            for j in range(-1, self.n_cols() + 1):
                print(self.get_value(i, j), end=' ')
            print()
        print()


def run():
    test_table = Table(3, 3)
    test_table.set_value(0, 2, 5)

    test_table.print_array()

    test_table.add_row(1)

    test_table.print_array()
    test_table.print_array_full()

    test_table.add_col(0)

    test_table.print_array()
    test_table.print_array_full()

    test_table.set_value(2, 2, 100)

    test_table.print_array()
    test_table.print_array_full()


if __name__ == "__main__":
    run()
