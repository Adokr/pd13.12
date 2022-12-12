import pytest
from homework import take_from_list, calculate

@pytest.mark.parametrize("x", ["y", "lol", ([0], [1]), 1.0, None])
def test_take_from_list_type(x):
    with pytest.raises(ValueError, match= f"Indices should be integer or list of integers, not {type(x)}"):
        take_from_list([0, 1, 2], x)

@pytest.mark.parametrize("li, indices", [([0], 1), ([0, 1, 2], [2, 3])] )
def test_take_from_list_index(indices, li):
    with pytest.raises(IndexError, match=f"Index {indices} is to big for list of length {len(li)}"):
        take_from_list(li, indices)

def test_take_from_list1():
    assert take_from_list([0, 1, 2], 2) == [2]

def test_take_from_list2():
    assert take_from_list([0, 1, 2], [1, 1]) == [1, 1]

def test_calculate1(tmp_path):
    p = tmp_path / "testing-homework/output.json"
    p.parent.mkdir()
    p.touch()
    with pytest.raises(FileNotFoundError, match="No such file or directory: 'lol.txt'"):
        calculate("lol.txt", p)