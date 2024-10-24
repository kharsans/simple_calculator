import pytest
from calculator.py import squareNums, triNums, lazyCaterer, magicSquares, calculatehypotenuse, volumeOfSphere, celsiusToFahrenheit

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 4),
    (3, 9)
])
def test_squareNums(n, expected):
    assert squareNums(n) == expected

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 3),
    (3, 6)
])
def test_triNums(n, expected):
    assert triNums(n) == expected

@pytest.mark.parametrize("n, expected", [
    (1, 2),
    (2, 4),
    (3, 7)
])
def test_lazyCaterer(n, expected):
    assert lazyCaterer(n) == expected

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 5),
    (3, 15)
])
def test_magicSquares(n, expected):
    assert magicSquares(n) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17)
])
def test_calculatehypotenuse(a, b, expected):
    assert pytest.approx(calculatehypotenuse(a, b)) == expected

@pytest.mark.parametrize("radius, expected", [
    (1, 4.1887902047863905),
    (2, 33.510321638291124),
    (3, 113.09733552923255)
])
def test_volumeOfSphere(radius, expected):
    assert pytest.approx(volumeOfSphere(radius)) == expected

@pytest.mark.parametrize("celsius, expected", [
    (0, 32),
    (100, 212),
    (-40, -40)
])
def test_celsiusToFahrenheit(celsius, expected):
    assert celsiusToFahrenheit(celsius) == expected
