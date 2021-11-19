from grahamoneilcanada.python_problems.two_sum import TwoSum


def test_brute_force():
    expected = [0, 1]
    result = TwoSum().brute_force([2, 7, 11, 15], 9)
    assert expected == result

