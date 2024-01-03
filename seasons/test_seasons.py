import sys
from seasons import String1
def test_string1():
    a=String1.get("2023-01-02")
    assert a=="Five hundred twenty-five thousand, six hundred minutes"
    a=String1.get("2022-01-02")
    assert a=="One million, fifty-one thousand, two hundred minutes"
