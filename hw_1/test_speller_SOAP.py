from speller_SOAP import check_text


def test_step1(good_word, bad_word):
    assert good_word in check_text(bad_word)
