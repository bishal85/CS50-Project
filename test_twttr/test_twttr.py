from twttr import shorten

def test_String():
    assert shorten("hello world")=="hll wrld"
    assert shorten("HELLO WORLD")=="HLL WRLD"
    assert shorten("H+L*O W.R,D")=="H+L* W.R,D"
    assert shorten("H7L1O WD")=="H7L1 WD"
    assert shorten("H7+L1O w,D")=="H7+L1 w,D"

