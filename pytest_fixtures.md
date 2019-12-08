test fixture allows re-use of setup and teardown code across tests

```
@pytest.fixture():
def math():
    return Math()
```

```
def test_Add(math):
    assert math.add(1, 1) == 2
```

#test fixture teardown - yield

```
@pytest.fixture()
def setup():
    print("Setup")
    yield
    print("Teardown")
```

# test fixture teardown - addfinalizer

```
@pytest.fixture():
def setup(request):
   print("Setup")
   def teardown:
       print("Teardown")
   request.addfinalizer(teardown)
```

# test fixtures scope

- test fixtures can have the following 4 different scopes which specify how often the fixture will be called:

- function - run the fixture once for each test

- class - run the fixture once for each class of tests

- module - run once when the module goes in scope

- session - the fixture is run when pytest starts

# test fixture return objects and params

```
@pytest.fixture(params=[1,2])
def setupData(request):
    return request.param
```

```
def test1(setupData):
    print(setupData)
```