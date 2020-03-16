from necklace_matching.necklace_matcher import same_necklace, repeats, get_4_words_same_necklace


def test_same_necklace():
    assert same_necklace("nicole", "icolen") is True
    assert same_necklace("nicole", "lenico") is True
    assert same_necklace("nicole", "coneli") is False
    assert same_necklace("aabaaaaabaab", "aabaabaabaaa") is True
    assert same_necklace("abc", "cba") is False
    assert same_necklace("xxyyy", "xxxyy") is False
    assert same_necklace("xyxxz", "xxyxz") is False
    assert same_necklace("x", "x") is True
    assert same_necklace("x", "xx") is False
    assert same_necklace("x", "") is False
    assert same_necklace("", "") is True


def test_repeats():
    assert repeats("abc") == 1
    assert repeats("abcabcabc") == 3
    assert repeats("abcabcabcx") == 1
    assert repeats("aaaaaa") == 6
    assert repeats("a") == 1
    assert repeats("") == 1


def test_get_4_words_same_necklace():
    words = get_4_words_same_necklace()
    assert len(words) == 4
    for word_a in words:
        for word_b in words:
            assert same_necklace(word_a, word_b) is True
    print(words)
