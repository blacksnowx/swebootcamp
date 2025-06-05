def grade_scantron(answers, key):
    score = 0
    if len(answers) != len(key):
        return -1

    for i in range(0, len(answers)):
        if answers[i] == key[i]:
            score += 1

    return score


def test_grade_scantron_mismatched_length_returns_neg_one():
    answers = ["A", "B"]
    key = ["A", "B", "C"]
    assert grade_scantron(answers, key) == -1


def test_grade_scantron_calculates_correct_score():
    answers = ["A", "B", "B"]
    key = ["A", "B", "C"]
    assert grade_scantron(answers, key) == 2


def test_grade_scantron_calculates_perfect_score():
    answers = ["A", "B", "C"]
    key = ["A", "B", "C"]
    assert grade_scantron(answers, key) == 3


def test_grade_scantron_calculates_zero_score():
    answers = ["B", "C", "D"]
    key = ["A", "B", "C"]
    assert grade_scantron(answers, key) == 0


def test_grade_scantron_accepts_empty_lists():
    answers = []
    key = []
    assert grade_scantron(answers, key) == 0
