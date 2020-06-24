from opcional2 import *

def test_maximo123():
    assert maximo(1,2,3) == 3

def test_maximo471():
    assert maximo(4,7,1) == 7

def test_maximo360():
    assert maximo(-3,6,0) == 6

def test_maximo562055():
    assert maximo(56,20,55) == 56

def test_maximox():
    assert maximo(9,2,3) == 9

def test_maximoy():
    assert maximo(4,9,3) == 9

def test_maximoz():
    assert maximo(0,2,9) == 9

def test_maximoigual():
    assert maximo(9,9,9) == 9

def test_maximoigual():
    assert maximo(-4,-4,-4) == -4