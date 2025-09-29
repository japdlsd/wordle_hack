import pytest

from src.wordle_hack import wordle_hack

pattern_testscases = [
    ("a", "a", "g"),
    ("a", "b", "w"),
    ("aa", "aa", "gg"),
    ("aa", "ab", "gw"),
    ("ca", "ab", "wy"),
    ("caa", "aab", "wgy"),
    ("cqaa", "dazb", "wwyw"),
]


@pytest.mark.parametrize("guess,truth,pattern", pattern_testscases)
def test_eval_pattern(guess, truth, pattern):
    expected = pattern
    result = optimal_player.eval_pattern(guess, truth)
    assert result == expected
