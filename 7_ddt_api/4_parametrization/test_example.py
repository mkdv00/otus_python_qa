import pytest

from test_data.test_data import auth_endpoints


@pytest.mark.parametrize("param", [1, 2, 3, 4])
def test_one(param):
    assert param % 2 == 0, f"{param} is not equal 2."
    

# Example with several parameters
@pytest.mark.parametrize("param1, param2", [
    (1, 2), (3, 4), (5, 6), (7, 8)
])
def test_two(param1, param2):
    assert (param1 + param2) % 3 == 0, f"({param1} + {param2}) % 3 is not equal 0"


# Example with nested parametrizaton
@pytest.mark.parametrize("param1", [1, 2, 3, 4, 5])
@pytest.mark.parametrize("param2", [6, 7, 8, 9, 0])
def test_tree(param1, param2):
    assert (param1 + param2) % 2 == 0, f"({param1} + {param2}) % 2 in not equal 0"
    

# Example with ids
@pytest.mark.parametrize("param", 
                         [1, 2, 3, 4, 5],
                         ids=["One", "Two", "Tree", "Four", "Five"])
def test_four(param):
    assert param is not None, f"{param} is None"


# Skip mark
@pytest.mark.parametrize("test_input, expected", [
                            ("3+5", 8),
                            ("2+4", 6),
                            pytest.param("6*9", 42, marks=pytest.mark.skip("JIRA-12312"))
                        ])
def test_five(test_input, expected):
    assert eval(test_input) == expected, f"{test_input} does no equals to {expected}"


# Example with fixture params
from test_data.test_data import get_auth_endpoints
def test_with_fixture(param_fixture):
    assert param_fixture > 0, f"{param_fixture} less or equals then 0"


# Example with csv file
@pytest.mark.parametrize("data", auth_endpoints)
def test_with_generator(data):
    print(data)
