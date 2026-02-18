import pytest

@pytest.fixture(scope="function")
def Initial_setup():
    print("First the setup is completed")


def test_first_method(Initial_setup):
    print("This is first check")

@pytest.fixture(scope="module")
def preWork():
    print("I setup module instance")
    return "fail"


@pytest.fixture(scope="function")
def secondWork():
    print("I setup secondWork instance")
    yield #pause
    print("tear down validation")


# @pytest.mark.smoke
def test_initialCheck(preWork, secondWork):
    print("This is first test")
    assert preWork == "fail"


# @pytest.mark.skip
def test_SecondCheck(preWork, third_check):
    print("This is Second test")


