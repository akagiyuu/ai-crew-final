import pytest
from data_structure.vec_dequeue import VecDequeue


def test_vec_dequeue():
    vec = VecDequeue()
    assert vec.is_empty() is True
    assert str(vec) == "[]"

    with pytest.raises(IndexError):
        vec.pop_front()
    with pytest.raises(IndexError):
        vec.pop_back()

    for i in range(10):
        assert len(vec) == i
        vec.insert(i, i + 1)
    assert str(vec) == "[" + ", ".join(str(i) for i in range(1, 11)) + "]"

    vec.push_front(0)
    vec.push_back(11)
    assert str(vec) == "[" + ", ".join(str(i) for i in range(12)) + "]"

    assert vec.pop_front() == 0
    assert vec.remove(9) == 10
    assert vec.pop_back() == 11
    assert len(vec) == 9
    assert str(vec) == "[" + ", ".join(str(i) for i in range(1, 10)) + "]"
