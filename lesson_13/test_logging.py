import homework_13
import pytest

@pytest.mark.parametrize('username,status', [
        ('Mykola', "success"),
        ('Kira', "failed"),
        ('Oleg', "expired")])

def test_logging(username, status):
    homework_13.log_event(username, status)

    with open('login_system.log') as f:
        last_row = f.readlines()[-1]
    assert f'Login event - Username: {username}, Status: {status}' in last_row
