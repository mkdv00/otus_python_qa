import pytest
 

@pytest.fixture(scope='session')
def environment(request):
    print("BUILDING OF APPLICATION!")
    
    def final():
        print(" DE-BUILDING OF APPLICATION!")
    
    request.addfinalizer(final)
