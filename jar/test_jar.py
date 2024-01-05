from jar import Jar
def test_init():

    jar1 = Jar()



def test_str():
    jar1 = Jar()
    assert str(jar1) == ""
    jar1.deposit(1)
    assert str(jar1) == "🍪"
    jar1.deposit(11)
    assert str(jar1) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar1 = Jar()
    assert str(jar1) == ""
    jar1.deposit(1)
    assert str(jar1) == "🍪"
    assert jar1.size==1
    with pytest.raises(ValueError)
         jar1.deposit(27)
def test_withdraw():
    jar1 = Jar()
    assert str(jar1) == ""
    jar1.deposit(1)
    assert str(jar1) == "🍪"
    assert jar1.size==1
    with pytest.raises(ValueError)
         jar1.withdraw(34)




