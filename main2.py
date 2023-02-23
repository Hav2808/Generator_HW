
import types

list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
def flat_generator(list_of_lists_1):
    list_1 = list_of_lists_1
    a = 0
    b = 0
    # if a < len(list_1):
    while a < len(list_1):
        while b < len(list_1[a]) :
            element = list_1[a][b]
            yield element
            # print(element)
            b +=1
        a += 1
        b = 0


start = flat_generator(list_of_lists_1)
print(list(start))
for item in start:
    print(item)


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()