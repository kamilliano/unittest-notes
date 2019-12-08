import pytest


@pytest.fixture(scope="module", autouse=True)
def setupModule():
    print("\nSetup Module2")

@pytest.fixture(scope="class", autouse=True)
def setupFunction():
    print("\nSetup Class2")

@pytest.fixture(scope="function", autouse=True)
def setupFunction():
    print("\nSetup Function2")

class TestClass:

    def test1(self):
        print("ExecutingIt1!")
        assert True

    def test2(self):
        print("ExecutingIt2!")
        assert True