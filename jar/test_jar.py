from jar import Jar


def test_str():
    jar1 = Jar()
    assert str(jar1) == ""
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


