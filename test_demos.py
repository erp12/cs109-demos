from hw4_solution import protected_dividsion, word_count

# First print some of these function calls

def test_protected_dividsion_standard():
    assert protected_dividsion(10, 2) == 5

def test_protected_dividsion_zero_num():
    assert protected_dividsion(0, 5) == 0

def test_protected_dividsion_zero_den():
    assert protected_dividsion(5, 0) == 0

def test_word_count_standard():
    assert word_count("Hello World") == 2

def test_word_count_empty():
    assert word_count("") == 0


# Also do some class methods
