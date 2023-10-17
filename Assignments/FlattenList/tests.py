import pytest
from flatten_list import flatten_list
from flatten_list import recurse

def test_1():
    assert flatten_list([1, 2, [3], [4,5]]) == [1, 2, 3, 4, 5]

def test_2():
    assert recurse([1, 2, [3], [4,5]]) == [1, 2, 3, 4, 5]

def test_3():
    assert recurse([1,2,3,[1,2,3,4],5,6,[7,3,2,1]]) == [1,2,3,1,2,3,4,5,6,7,3,2,1]

# def test_4():
#     assert recurse([1, [2], [3, [4, 5, [6]]], 7]) == [1, 2, 3, 4, 5, 6, 7]
