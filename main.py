# "Доработать класс FlatIterator в коде ниже. Должен получиться итератор, который
# принимает
# список списков и возвращает их плоское представление, т. е. последовательность, состоящую
# из вложенных элементов. Функция test в коде ниже также должна отработать без ошибок.


class FlatIterator:
    def __init__(self, list_):
        self._stopped = False
        self._list = list_
        self.a = 0
        self.b = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self._stopped:
            while self.a < len(self._list):
                if self.b < len(self._list[self.a]):
                    element = self._list[self.a][self.b]
                    # print(element)
                    self.b += 1
                    return element

                self.a += 1
                self.b = 0
                # print(element)
            self._stopped = True
        raise StopIteration



list_of_lists_1 = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f', 'h', False],
            [1, 2, None]
        ]
print(list(FlatIterator(list_of_lists_1)))

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#

if __name__ == '__main__':
    test_1()