def setup_module(module):
    print("Setup module")

def teardown_module(module):
    print("Teardown module")

def setup_function(function):

    if function == test1:
        print("\nSetting up test1!")
    elif function == test2:
        print("\nSetting up test2!")
    else:
        print("\nSetting up unknown test!")


def teardown_function(function):

    if function == test1:
        print("\nTearing down test1!")
    elif function == test2:
        print("\nTearing down test2!")
    else:
        print("\nTearing down unknown test!")


def test1():
    print("Executing test1!")
    assert True


def test2():
    print("Executing test2!")
    assert True
