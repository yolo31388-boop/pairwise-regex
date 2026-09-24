import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from regex import RegexError, compile, findall, match, search  # noqa: E402


def test_literal():
    assert match("abc", "abc") is True
    assert match("abc", "abx") is False
    assert search("bc", "abc") == (1, 3)
    assert search("abc", "abc") == (0, 3)


def test_any_and_char_class():
    assert match("[abc]", "b") is True
    assert match("[a-z]", "m") is True
    assert match("[^abc]", "x") is True
    assert match("[^abc]", "a") is False
    assert match(".", "x") is True
    assert match("[0-9]+", "12345") is True


def test_alternation_and_group():
    assert match("a|b", "b") is True
    assert match("(a|b)c", "bc") is True
    assert match("(ab)+c", "ababc") is True
    assert match("x|y|z", "y") is True


def test_repeats():
    assert match("a*", "")
    assert match("a*", "aaa")
    assert match("a+", "aaa")
    assert not match("a+", "")
    assert match("a?", "")
    assert match("a?", "a")


def test_nested_star():
    assert match("(ab|c)*", "ababccab")
    assert match("(a|b)*", "")


def test_escape():
    assert match(r"\d\d", "42") is True
    assert not match(r"\d", "x")
    assert match(r"a\.b", "a.b") is True
    assert match(r"a\*b", "a*b") is True


def test_anchors():
    assert match("^abc$", "abc") is True
    assert not match("^abc$", "xabc")
    assert search("^abc", "abcd") == (0, 3)
    assert search("abc$", "xxabc") == (2, 5)


def test_greedy_longest():
    assert search("a+", "aaa") == (0, 3)
    assert search("a*b", "aaab") == (0, 4)
    assert search("a*", "aaa") == (0, 3)   # 贪婪


def test_findall_non_overlapping():
    assert findall("aa", "aaaa") == [(0, 2), (2, 4)]
    assert findall("a+", "baaac") == [(1, 4)]
    assert findall(r"\d+", "a12b34c5") == [(1, 3), (4, 6), (7, 8)]


def test_no_match():
    assert search("zzz", "abc") is None
    assert findall("x", "abc") == []
    assert not match("a", "b")


def test_errors():
    for bad in ["(", "[", ")", "a{", "\\"]:
        try:
            compile(bad)
            assert False, f"应抛 RegexError: {bad!r}"
        except RegexError:
            pass


def test_empty_pattern():
    assert match("", "") is True
    assert search("", "abc") == (0, 0)
    assert findall("", "ab") == [(0, 0), (1, 1), (2, 2)]
