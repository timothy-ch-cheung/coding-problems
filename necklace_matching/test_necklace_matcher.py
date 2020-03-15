from necklace_matching.necklace_matcher import same_necklace

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
