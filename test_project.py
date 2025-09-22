import pytest
from project import generate_password, password_secure , validate_customize_password

def test_generate_password():
    password=generate_password(12)
    assert len(password) == 12

def test_password_valid():
    valid_ps="Mahi@1908*"
    assert password_secure (valid_ps) is True

def test_password_invalid():
    invalid_ps="weakpassword"
    assert password_secure (invalid_ps) is False

def test_validate_customize_password_valid():
    try:
        validate_customize_password("Mahesh_1718")
    except ValueError:
        pytest.fail("ValueError")


def test_validate_customize_password_invalid():
    with pytest.raises(ValueError):
        validate_customize_password("It's short.Enter valid one")

