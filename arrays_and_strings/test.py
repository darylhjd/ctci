import unittest

import is_unique
import check_permutation
import urlify
import palindrome_permutation
import one_away
import string_compression
import rotate_matrix
import zero_matrix
import string_rotation


class TestArraysAndStrings(unittest.TestCase):
    def test_is_unique(self):
        self.assertTrue(is_unique.using_set("some"))
        self.assertFalse(is_unique.using_set("test"))

        self.assertTrue(is_unique.no_ds_brute_force("some"))
        self.assertFalse(is_unique.no_ds_brute_force("test"))

        self.assertTrue(is_unique.no_ds_bit_vector("thelazydogjumps"))

    def test_check_permutation(self):
        self.assertTrue(check_permutation.counter_solution("this", "hsit"))
        self.assertTrue(check_permutation.counter_solution("rhgfiugh", "fiugghhr"))
        self.assertFalse(check_permutation.counter_solution("nope", "yes"))

        self.assertTrue(check_permutation.sort_solution("rhgfiugh", "fiugghhr"))
        self.assertFalse(check_permutation.sort_solution("nope", "yes"))

    def test_urlify(self):
        self.assertEqual(urlify.urlify(list("Mr John Smith    "), 13), "Mr%20John%20Smith")
        self.assertEqual(urlify.urlify(list(" Mr John    "), 8), "%20Mr%20John")

    def test_palindrome_permutation(self):
        self.assertTrue(palindrome_permutation.palindrome_permutation("tact coa"))
        self.assertTrue(palindrome_permutation.palindrome_permutation("cacaerr"))
        self.assertFalse(palindrome_permutation.palindrome_permutation("not a palindrome"))

    def test_one_away(self):
        self.assertTrue(one_away.one_away("pale", "ple"))
        self.assertTrue(one_away.one_away("pales", "pale"))
        self.assertTrue(one_away.one_away("pale", "bale"))
        self.assertFalse(one_away.one_away("pale", "bake"))

        self.assertTrue(one_away.one_away("something", "somthing"))
        self.assertTrue(one_away.one_away("palindrome", "palindrom"))
        self.assertFalse(one_away.one_away("wrong", "woomg"))

    def test_string_compression(self):
        self.assertEqual(string_compression.string_compression("aabcccccaaa"), "a2b1c5a3")
        self.assertEqual(string_compression.string_compression("abcdefg"), "abcdefg")

    def test_rotate_matrix(self):
        a = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
        rotate_matrix.rotate_matrix(a)
        self.assertEqual(a, [[7, 4, 1],
                             [8, 5, 2],
                             [9, 6, 3]])

        a = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
        rotate_matrix.rotate_matrix(a)
        self.assertEqual(a, [[13, 9, 5, 1],
                             [14, 10, 6, 2],
                             [15, 11, 7, 3],
                             [16, 12, 8, 4]])

    def test_zero_matrix(self):
        a = [[1, 2, 3],
             [4, 0, 6],
             [7, 8, 9]]
        zero_matrix.zero_matrix_hash_set(a)
        self.assertEqual(a, [[1, 0, 3],
                             [0, 0, 0],
                             [7, 0, 9]])

        a = [[1, 2, 3, 4],
             [0, 4, 0, 9],
             [8, 5, 3, 0],
             [1, 1, 1, 1]]
        zero_matrix.zero_matrix_hash_set(a)
        self.assertEqual(a, [[0, 2, 0, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0],
                             [0, 1, 0, 0]])

        a = [[1, 2, 3],
             [4, 0, 6],
             [7, 8, 9]]
        zero_matrix.zero_matrix_no_space(a)
        self.assertEqual(a, [[1, 0, 3],
                             [0, 0, 0],
                             [7, 0, 9]])

        a = [[1, 2, 3, 4],
             [0, 4, 0, 9],
             [8, 5, 3, 0],
             [1, 1, 1, 1]]
        zero_matrix.zero_matrix_no_space(a)
        self.assertEqual(a, [[0, 2, 0, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0],
                             [0, 1, 0, 0]])

    def test_string_rotation(self):
        self.assertTrue(string_rotation.string_rotation("oooot", "oooto"))
        self.assertTrue(string_rotation.string_rotation("waterbottle", "erbottlewat"))
        self.assertFalse(string_rotation.string_rotation("botbo", "abobo"))
        self.assertTrue(string_rotation.string_rotation("botbo", "tbobo"))
        self.assertTrue(string_rotation.string_rotation("1", "1"))


if __name__ == '__main__':
    unittest.main()
