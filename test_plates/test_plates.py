from plates import is_valid
def test_string():

    assert is_valid("Cs50")==True
    assert is_valid("Cs05")==False
    assert is_valid("PI3.14")==False
    assert is_valid("50")==False
    assert is_valid("helloo1")==False
    assert is_valid("HE1H")==False





