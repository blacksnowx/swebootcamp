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


def fix_same_letter_pairs(string):
    new_string = ""
    for i in range(0, len(string)):
        if i % 2 == 1 and string[i - 1] == string[i]:
            new_string += "X"
        else:
            new_string += string[i]
    return new_string


def string_to_pairs(string):
    new_string = ""
    new_string = string_to_uppercase(string)
    new_string = j_to_i(new_string)
    new_string = remove_non_chars(new_string)
    new_string = add_x_if_len_odd(new_string)
    new_string = fix_same_letter_pairs(new_string)
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


def test_fix_same_letter_pairs_changes_identical_letter_to_x():
    assert fix_same_letter_pairs("LLABCCDE") == "LXABCXDE"


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
    assert string_to_pairs("aabbcc") == "AX BX CX"


def test_string_to_pairs_performs_all_adjustments():
    assert string_to_pairs("PS. Hello, worlds jj") == "PS HE LX OW OR LD SI IX"


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


def rows_to_columns(cipher):
    flipped_cipher = []
    for row in cipher:
        flipped_cipher.append([])
    for row in cipher:
        for i in range(0, len(row)):
            flipped_cipher[i].append(row[i])
    return flipped_cipher


# PAIR CLASSIFICATION TEST SUITE:
def test_same_case_identifies_pairs_with_same_letters():
    assert same_case("LL", CIPHER)


def test_row_case_identifies_pairs_in_same_row():
    assert row_case("NR", CIPHER)


def test_column_case_identifies_pairs_in_same_column():
    assert column_case("KZ", CIPHER)


def test_rectangle_case_identifies_pairs_in_different_rows_and_columns():
    assert rectangle_case("MW", CIPHER)


def test_rows_to_columns_flips_rows_and_columns_for_cipher():
    assert rows_to_columns((("D", "A"), ("Y", "N"))) == [["D", "Y"], ["A", "N"]]


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
        if row_case(pair, cipher):
            for j in range(0, 2):
                for row in cipher:
                    for i in range(0, 5):
                        if pair[j] == row[i]:
                            if i <= 3:
                                encrypted_string += row[i + 1]
                            else:
                                encrypted_string += row[0]
        elif column_case(pair, cipher):
            rotated = rows_to_columns(cipher)
            for j in range(0, 2):
                for row in rotated:
                    for i in range(0, 5):
                        if pair[j] == row[i]:
                            if i <= 3:
                                encrypted_string += row[i + 1]
                            else:
                                encrypted_string += row[0]

        else:
            first_letter_row = -1
            first_letter_column = 0
            first_letter_found = False
            second_letter_row = -1
            second_letter_column = 0
            second_letter_found = False
            for row in cipher:
                if not first_letter_found:
                    first_letter_row += 1
                if not second_letter_found:
                    second_letter_row += 1
                for i in range(0, 5):
                    if pair[0] == row[i]:
                        first_letter_column = i
                        first_letter_found = True
                    if pair[1] == row[i]:
                        second_letter_column = i
                        second_letter_found = True

            encrypted_string += (
                f"{cipher[first_letter_row][second_letter_column]}"
                f"{cipher[second_letter_row][first_letter_column]}"
            )
    return encrypted_string


# ENCRYPTION TEST SUITE:


def test_encrypt_encrypts_row_case_pairs():
    assert encrypt("KH") == "CK"


def test_encrypt_encrypts_column_case_pairs():
    assert encrypt("IXIX") == "RIRI"


def test_encrypt_encrypts_rectangle_case_pairs():
    assert encrypt("HE") == "GR"


def test_encrypt_encrypts_multiple_rectangle_case_pairs():
    assert encrypt("IXHEHEIX") == "RIGRGRRI"


# DECRYPTION LOGIC


def decrypt(string):
    cipher = (
        ("D", "A", "V", "I", "O"),
        ("Y", "N", "E", "R", "B"),
        ("C", "F", "G", "H", "K"),
        ("L", "M", "P", "Q", "S"),
        ("T", "U", "W", "X", "Z"),
    )
    pairs_list = final_string_to_list(string_to_pairs(string))
    decrypted_string = ""
    for pair in pairs_list:
        if row_case(pair, cipher):
            for j in range(0, 2):
                for row in cipher:
                    for i in range(0, 5):
                        if pair[j] == row[i]:
                            if i >= 1:
                                decrypted_string += row[i - 1]
                            else:
                                decrypted_string += row[4]
        elif column_case(pair, cipher):
            rotated = rows_to_columns(cipher)
            for j in range(0, 2):
                for row in rotated:
                    for i in range(0, 5):
                        if pair[j] == row[i]:
                            if i >= 1:
                                decrypted_string += row[i - 1]
                            else:
                                decrypted_string += row[4]
        else:
            first_letter_row = -1
            first_letter_column = 0
            first_letter_found = False
            second_letter_row = -1
            second_letter_column = 0
            second_letter_found = False
            for row in cipher:
                if not first_letter_found:
                    first_letter_row += 1
                if not second_letter_found:
                    second_letter_row += 1
                for i in range(0, 5):
                    if pair[0] == row[i]:
                        first_letter_column = i
                        first_letter_found = True
                    if pair[1] == row[i]:
                        second_letter_column = i
                        second_letter_found = True
            decrypted_string += (
                f"{cipher[first_letter_row][second_letter_column]}"
                f"{cipher[second_letter_row][first_letter_column]}"
            )
    return decrypted_string


# DECRYPTION TEST SUITE:


def test_decrypt_decrypts_row_case_pairs():
    assert decrypt("KH") == "HG"


def test_decrypt_decrypts_column_case_pairs():
    assert decrypt("RI") == "IX"


def test_decrypt_decrypts_rectangle_case_pairs():
    assert decrypt("ZAZAAZAZ") == "UOUOOUOU"


def test_decrypt_decrypts_long_string():
    assert decrypt("QLGRQTVZIBTYQZ") == "PSHELXOWORLDSX"
