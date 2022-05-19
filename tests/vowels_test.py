from programs import vowels

def test_no_vowels():
    assert vowels.vowels("GLHGH") == 0

def test_uppercase_vowels():
    assert vowels.vowels("HELLO") == 2

def test_lowercase_vowels():
    assert vowels.vowels("banana") == 3

def test_mixedcase_vowels():
    assert vowels.vowels("SPECify") == 2
