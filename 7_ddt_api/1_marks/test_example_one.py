import pytest


@pytest.mark.regress
@pytest.mark.auth
@pytest.mark.skip(reason="Becouse test is broken")
def test_one():
    assert True


@pytest.mark.sec
@pytest.mark.xfail
@pytest.mark.regress
def test_second():
    assert True
    
    
@pytest.mark.regress
@pytest.mark.sec
def test_three():
    assert 5 + 5 == 10, "5 + 5 is not equals 10"
    
    
@pytest.mark.regress
@pytest.mark.sec
def test_four():
    assert 10 + 5 == 15, "10 + 5 is not equals 15"
