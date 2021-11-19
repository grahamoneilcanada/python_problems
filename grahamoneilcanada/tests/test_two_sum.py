import pytest
from grahamoneilcanada.python_problems.two_sum import TwoSum

pytest.two_sum_nums_test_one = [2, 7, 11, 15]
pytest.two_sum_target_test_one = 9
pytest.two_sum_expected_test_one = [0, 1]
pytest.two_sum_nums_test_two = [3, 2, 4]
pytest.two_sum_target_test_two = 6
pytest.two_sum_expected_test_two = [1, 2]
pytest.two_sum_nums_test_three = [3, 3]
pytest.two_sum_target_test_three = 6
pytest.two_sum_expected_test_three = [0, 1]


def test_brute_force_test_one():
    result = TwoSum().brute_force(pytest.two_sum_nums_test_one, pytest.two_sum_target_test_one)
    assert all(elem in pytest.two_sum_expected_test_one for elem in result)


def test_brute_force_test_two():
    result = TwoSum().brute_force(pytest.two_sum_nums_test_two, pytest.two_sum_target_test_two)
    assert all(elem in pytest.two_sum_expected_test_two for elem in result)


def test_brute_force_test_three():
    result = TwoSum().brute_force(pytest.two_sum_nums_test_three, pytest.two_sum_target_test_three)
    assert all(elem in pytest.two_sum_expected_test_three for elem in result)


def test_two_pass_hash_test_one():
    result = TwoSum().two_pass_hash(pytest.two_sum_nums_test_one, pytest.two_sum_target_test_one)
    assert all(elem in pytest.two_sum_expected_test_one for elem in result)


def test_two_pass_hash_test_two():
    result = TwoSum().two_pass_hash(pytest.two_sum_nums_test_two, pytest.two_sum_target_test_two)
    assert all(elem in pytest.two_sum_expected_test_two for elem in result)


def test_two_pass_hash_test_three():
    result = TwoSum().two_pass_hash(pytest.two_sum_nums_test_three, pytest.two_sum_target_test_three)
    assert all(elem in pytest.two_sum_expected_test_three for elem in result)


def test_one_pass_hash_test_one():
    result = TwoSum().one_pass_hash(pytest.two_sum_nums_test_one, pytest.two_sum_target_test_one)
    assert all(elem in pytest.two_sum_expected_test_one for elem in result)


def test_one_pass_hash_test_two():
    result = TwoSum().one_pass_hash(pytest.two_sum_nums_test_two, pytest.two_sum_target_test_two)
    assert all(elem in pytest.two_sum_expected_test_two for elem in result)


def test_one_pass_hash_test_three():
    result = TwoSum().one_pass_hash(pytest.two_sum_nums_test_three, pytest.two_sum_target_test_three)
    assert all(elem in pytest.two_sum_expected_test_three for elem in result)

