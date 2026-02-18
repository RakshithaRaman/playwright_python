import pytest

@pytest.fixture(scope="module")
def third_check():
    print("This is third check")

