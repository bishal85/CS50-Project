import pytest
from fuel import convert,gauge
def test_string1():
      assert convert("2/3")==67
      assert convert("1/100")==1
      assert convert("1/2")==50
      with pytest.raises(ValueError):
           convert("2/1")

      with pytest.raises(ZeroDivisionError):
           convert("2/0")
def test_string2():
      assert gauge(50)=="50%"
      assert gauge(1)=="E"
      assert gauge(99)=="F"
def Value():
      with pytest.raises(ZeroDivisionError):
           convert("2/0")

def Value2():
       with pytest.raises(ValueError):
           convert("2/1")


