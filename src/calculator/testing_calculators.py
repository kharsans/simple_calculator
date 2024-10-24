import pytest
import math
from src.calculator import calculator as calc

@pytest.mark.parametrize("n, expected", [
    pytest.param(1, 1, id='n=1'),
    pytest.param(2, 4, id='n=2'),
    pytest.param(3, 9, id='n=3')
])
def test_squareNums(n, expected):
    assert calc.squareNums(n) == expected

@pytest.mark.parametrize("n, expected", [
    pytest.param(1, 1, id='n=1'),
    pytest.param(2, 3, id='n=2'),
    pytest.param(3, 6, id='n=3')
])
def test_triNums(n, expected):
    assert calc.triNums(n) == expected

@pytest.mark.parametrize("n, expected", [
    pytest.param(1, 2, id='n=1'),
    pytest.param(2, 4, id='n=2'),
    pytest.param(3, 7, id='n=3')
])
def test_lazyCaterer(n, expected):
    assert calc.lazyCaterer(n) == expected

@pytest.mark.parametrize("n, expected", [
    pytest.param(1, 1, id='n=1'),
    pytest.param(2, 5, id='n=2'),
    pytest.param(3, 15, id='n=3')
])
def test_magicSquares(n, expected):
    assert calc.magicSquares(n) == expected

@pytest.mark.parametrize("a, b, expected", [
    pytest.param(3, 4, 5, id='3-4-5 triangle'),
    pytest.param(5, 12, 13, id='5-12-13 triangle'),
    pytest.param(8, 15, 17, id='8-15-17 triangle')
])
def test_calculatehypotenuse(a, b, expected):
    assert calc.calculatehypotenuse(a, b) == expected

@pytest.mark.parametrize("radius, expected", [
    pytest.param(1, 4.1887902047863905, id='radius=1'),
    pytest.param(2, 33.510321638291124, id='radius=2'),
    pytest.param(3, 113.09733552923255, id='radius=3')
])
def test_volumeOfSphere(radius, expected):
    tolerance = 0.000001  
    result = calc.volumeOfSphere(radius)
    assert abs(result - expected) <= tolerance

@pytest.mark.parametrize("celsius, expected", [
    pytest.param(0, 32, id='freezing point'),
    pytest.param(100, 212, id='boiling point'),
    pytest.param(-40, -40, id='negative forty')
])
def test_celsiusToFahrenheit(celsius, expected):
    assert calc.celsiusToFahrenheit(celsius) == expected
