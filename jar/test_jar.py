from jar import Jar


def test_str():
    jar1 = Jar()
    assert str(jar1) == ""
    jar1.deposit(1)
    assert str(jar1) == "🍪"
    jar1.deposit(11)
    assert str(jar1) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"



