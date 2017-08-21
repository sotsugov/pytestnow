# -*- coding: utf-8 -*-
import pytest
from hello import hello_name


def test_hello_first():
    assert hello_name("john") == "hello john"


def test_hello_full_name():
    assert hello_name("john doe") == "hello john doe"


def test_hello_none():
    assert hello_name("") == "hello "


def test_hello_numbers():
    assert hello_name(123) == "hello 123"


def test_hello_unicode():
    assert hello_name("🍩") == "hello 🍩"


if __name__ == '__main__':
    pytest.main([__file__])
