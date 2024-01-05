from jar import Jar


def test_init():
    jar = Jar()
    assert jar == ""

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar=Jar()
    assert jar == ""
    jar.deposit(1)
    assert jar == "🍪"
    jar.deposit(11)
    assert jar == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"



def test_withdraw():
    assert jar == ""
    jar.deposit(1)
    assert jar == "🍪"
    jar.deposit(11)
    assert jar == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

