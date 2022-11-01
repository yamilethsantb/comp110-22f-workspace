"""Tests for dictionary functions - ex07."""

from dictionary import invert 


def test_invert() -> None:
    """Test when dictionary parameter is empty."""
    assert invert({}) == {}


def test_invert_2() -> None:
    """Test when length of dictionary is one."""
    assert invert({'Dodge': 'car'}) == {'car': 'Dodge'}


def test_invert_3() -> None:
    """Test when length of dictionary is more than one."""
    assert invert({'student': 'school', 'zookeeper': 'zoo', 'doctor': 'hospital'}) == {'school': 'student', 'zoo': 'zookeeper', 'hospital': 'doctor'}

