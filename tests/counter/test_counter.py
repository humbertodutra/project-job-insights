import pytest 
from src.pre_built.counter import count_ocurrences

# from src.pre_built.counter import count_ocurrences

path = "tests/mocks/jobs.csv"


def test_counter():
    assert count_ocurrences(path, "developer") == 3
    assert count_ocurrences(path, "DEVELOPER") == 3

    with pytest.raises(TypeError):
        count_ocurrences(path)
        count_ocurrences("developer")

    with pytest.raises(FileNotFoundError):
        count_ocurrences("jobs_not_found.csv", "developer")
