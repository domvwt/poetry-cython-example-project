from adders.addition import add, sum_list


def test_add():
    assert add(1, 2) == 3


def test_sum_list():
    assert sum_list([1, 2, 3]) == 6
