from numb3rs import validate
def test_string1():

    assert validate("127.0.0.1")==True
    assert validate("127.0.0.1.2")==False
    assert validate("1.2.3.1000")==False
    assert validate("62.452.24.27")==False
