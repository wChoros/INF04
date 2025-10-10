from main import cesar_encrypt
import pytest

def test_cesar_normal():
    text_to_encrypt = "abc"
    expected_text = "def"
    key = 3
    assert cesar_encrypt(text_to_encrypt, key) == expected_text

def test_cesar_roll():
    text_to_encrypt = "xyz"
    expected_text = "abc"
    key = 3
    assert cesar_encrypt(text_to_encrypt, key) == expected_text

def test_cesar_negative():
    text_to_encrypt = "def"
    expected_text = "abc"
    key = -3
    assert cesar_encrypt(text_to_encrypt, key) == expected_text

def test_cesar_big():
    text_to_encrypt = "abc"
    expected_text = "def"
    key = 29
    assert cesar_encrypt(text_to_encrypt, key) == expected_text

def test_cesar_space():
    text_to_encrypt = "ab cd"
    expected_text = "cd ef"
    key = 2
    assert cesar_encrypt(text_to_encrypt, key) == expected_text

if __name__ == "__main__":
    pytest.run