from bank import value


def test_string():
    assert value("HEllo")==0
    assert value("HEllo, what are you doing")==0
    assert value("How you doing")==20
    assert value("What are you doing")==100


