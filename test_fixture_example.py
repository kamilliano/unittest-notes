import pytest

@pytest.fixture() #autouse=True if you want to use it automatically
def setup():
    print("\nSetup")

def test1(setup):

    print("Executing test1!")
    assert True

@pytest.mark.usefixtures("setup")
def test2():
    print("Executing test2!")
    assert True