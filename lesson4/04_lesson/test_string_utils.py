from string_utils import StringUtils

utils = StringUtils()


def test_capitalize_positive():
    assert utils.capitalize("skypro") == "Skypro"


def test_capitalize_empty():
    assert utils.capitalize("") == ""


def test_trim_positive():
    assert utils.trim("   skypro") == "skypro"


def test_trim_negative():
    assert utils.trim("     ") == ""


def test_contains_true():
    assert utils.contains("SkyPro", "S") is True


def test_contains_false():
    assert utils.contains("SkyPro", "U") is False


def test_delete_symbol_positive():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_symbol_substring_bug():
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"


def test_capitalize_none_bug():
    assert utils.capitalize(None) == ""


def test_trim_none_bug():
    assert utils.trim(None) == ""
