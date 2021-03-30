import paypay
import pytest

def test_iseven():
    assert not paypay.iseven(1)
    assert not paypay.iseven(132461)
    assert not paypay.iseven(2.1)
    assert paypay.iseven(2)
    assert paypay.iseven(200)
    assert paypay.iseven(230132)

def test_sqrt():
    assert abs(paypay.sqrt(9**2, 1e-3) - 9) < 1e-3


@pytest.mark.parametrize('word, palindrome', [('holi', False),
                                              ('Python', False),
                                              ('dabalearrozalazorraelabad', True),
                                              ('dabale arroz a la zorra el abad', False),
                                              ('Bob', True)])
def test_ispalindrome(word, palindrome):
    assert paypay.ispalindrome(word) == palindrome
