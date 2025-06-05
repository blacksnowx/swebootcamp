CIPHER = (
    ("D", "A", "V", "I", "O"),
    ("Y", "N", "E", "R", "B"),
    ("C", "F", "G", "H", "K"),
    ("L", "M", "P", "Q", "S"),
    ("T", "U", "W", "X", "Z"),
)


def string_to_uppercase(string):
    return string.upper()


def j_to_i(string):
    new_string = ""
    for x in string:
        if x == "j" or x == "J":
            new_string += "I"
        else:
            new_string += x
    return new_string


def remove_non_chars(string):
    new_string = ""
    for char in string:
        if char.isalpha():
            new_string += char
    return new_string


def add_x_if_len_odd(string):
    if len(string) % 2 == 1:
        return string + "X"
    else:
        return string


def string_to_pairs(string):
    new_string = ""
    new_string = string_to_uppercase(string)
    new_string = j_to_i(new_string)
    new_string = remove_non_chars(new_string)
    new_string = add_x_if_len_odd(new_string)
    count = 0
    paired_string = ""
    for char in new_string:
        count += 1
        if count == 2:
            paired_string += char
            paired_string += " "
            count = 0
        else:
            paired_string += char
    final_string = paired_string[:-1]

    return final_string


def final_string_to_list(string):
    return string.split(" ")


# STRING CONVERSION TEST SUITE


def test_string_to_uppercase_converts_string_to_all_uppercase():
    assert string_to_uppercase("test string") == ("TEST STRING")


def test_j_to_i_converts_js_to_is():
    assert j_to_i("jif") == "Iif"


def test_j_to_i_handles_upper_and_lowercase():
    assert j_to_i("Jif") == "Iif"


def test_remove_non_chars_strips_non_chars():
    assert remove_non_chars("a1!A)2~ b3B4") == "aAbB"


def test_add_x_if_len_odd_adds_x_to_odd_length_string():
    assert add_x_if_len_odd("Cat") == "CatX"


def test_leave_string_unchanged_if_length_even():
    assert add_x_if_len_odd("Rabbit") == "Rabbit"


def test_string_to_pairs_adds_space_after_every_two_chars():
    assert string_to_pairs("aabbcc") == "AA BB CC"


def test_string_to_pairs_performs_all_adjustments():
    assert string_to_pairs("PS. Hello, worlds jj") == "PS HE LL OW OR LD SI IX"


def test_final_string_to_list_converts_string_into_list():
    assert final_string_to_list("AB CD EF") == ["AB", "CD", "EF"]


# PAIR CLASSIFICATION LOGIC:


def same_case(string, cipher):
    return True if string[0] == string[1] else False


def row_case(string, cipher):
    for row in cipher:
        if string[0] in row and string[1] in row:
            return True
    return False


def column_case(string, cipher):
    for row in cipher:
        for i in range(0, 5):
            if string[0] == row[i]:
                for row in cipher:
                    if string[1] == row[i]:
                        return True
    return False


def rectangle_case(string, cipher):
    return not (
        same_case(string, cipher)
        or row_case(string, cipher)
        or column_case(string, cipher)
    )


# PAIR CLASSIFICATION TEST SUITE:


def test_same_case_identifies_pairs_with_same_letters():
    assert same_case("LL", CIPHER)


def test_row_case_identifies_pairs_in_same_row():
    assert row_case("NR", CIPHER)


def test_column_case_identifies_pairs_in_same_column():
    assert column_case("KZ", CIPHER)


def test_rectangle_case_identifies_pairs_in_different_rows_and_columns():
    assert rectangle_case("MW", CIPHER)


# ENCRYPTION LOGIC


def encrypt(string):
    cipher = (
        ("D", "A", "V", "I", "O"),
        ("Y", "N", "E", "R", "B"),
        ("C", "F", "G", "H", "K"),
        ("L", "M", "P", "Q", "S"),
        ("T", "U", "W", "X", "Z"),
    )
    pairs_list = final_string_to_list(string_to_pairs(string))
    encrypted_string = ""
    for pair in pairs_list:
        if same_case(pair, cipher):
            encrypted_string += pair[0]
            encrypted_string += "X"
        elif row_case(pair, cipher):
            for j in range(0, 2):
                for row in cipher:
                    for i in range(0, 5):
                        if pair[j] == row[i]:
                            if i <= 3:
                                encrypted_string += row[i + 1]
                            else:
                                encrypted_string += row[0]
    return encrypted_string


# ENCRYPTION TEST SUITE:


def test_encrypt_encrypts_same_case_pairs():
    assert encrypt("eeff") == "EXFX"


def test_encrypt_encrypts_row_case_pairs():
    assert encrypt("KH") == "CK"
