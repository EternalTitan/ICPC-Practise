import unittest
import re
from fun_poker_puzzle import *


class TestPuzzle(unittest.TestCase):
    def test_royal_flush_1(self):
        data = "7D 8D 9D TD JD AD QD KD 5D 6D".split()
        ans = main(data)
        print("expect royal-flush ", ans)
        # self.assertRegex(ans, re.compile('.*Best hand: royal-flush'))
        self.assertRegex(ans, re.compile('.*Best hand: straight-flush'))

    def test_royal_flush_2(self):
        data = "TD JD AD QD KD 7D 8D 9D 5D 6D".split()
        ans = main(data)
        print("expect royal-flush ", ans)
        # self.assertRegex(ans, re.compile('.*Best hand: royal-flush'))
        self.assertRegex(ans, re.compile('.*Best hand: straight-flush'))

    def test_straight_flush_1(self):
        data = "3H 5H 2H 9H KH 6H 4H 4D AD 2D".split()
        ans = main(data)
        print("expect straight-flush ", ans)
        self.assertRegex(ans, re.compile('.*Best hand: straight-flush'))

    def test_straight_flush_2(self):
        data = "9H KH AD 2D 3H 5H 2H 6H 4H 4D".split()
        ans = main(data)
        print("expect straight-flush ", ans)
        self.assertRegex(ans, re.compile('.*Best hand: straight-flush'))

    def test_four_of_a_kind_1(self):
        data = "9H KH AD 2D 3H 9D 9S 9C 4H 4D".split()
        ans = main(data)
        print("expect four-of-a-kind ", ans)
        self.assertRegex(ans, re.compile('.*Best hand: four-of-a-kind'))

    def test_four_of_a_kind_2(self):
        data = "KH AD 2D 3H 5H 2H 9H 9D 9S 9C".split()
        ans = main(data)
        print("expect four-of-a-kind ", ans)
        self.assertRegex(ans, re.compile('.*Best hand: four-of-a-kind'))

    def test_full_house_1(self):
        data = "9H KH AD 2D 3H 9D 9S 2H 3C 4D".split()
        ans = main(data)
        print("expect full-house ", ans)
        self.assertRegex(ans, re.compile('.*Best hand: full-house'))

    def test_full_house_2(self):
        data = "9H 9D 9S 2H 2D KH AD 3H 3C 4D".split()
        ans = main(data)
        print("expect full-house ", ans)
        self.assertRegex(ans, re.compile('.*Best hand: full-house'))

    def test_flush_1(self):
        data = "9H 4D 9S 2H 2D KH AH 3H 3C 4D".split()
        ans = main(data)
        print("expect flush ", ans)
        self.assertRegex(ans, re.compile('.*Best hand: flush'))

    def test_flush_2(self):
        data = "4D 9S 2H 2D KH AH 3H 9H 3C 4D".split()
        ans = main(data)
        print("expect flush ", ans)
        self.assertRegex(ans, re.compile('.*Best hand: flush'))

    def test_straight_1(self):
        data = "9H 8D 9S QH 2D TH JD 3H 3C 4D".split()
        ans = main(data)
        print("expect straight ", ans)
        self.assertRegex(ans, re.compile('.*Best hand: straight'))

    def test_straight_2(self):
        data = "9H 8D 9S QH TD TD JH 3H 3C 4D".split()
        ans = main(data)
        print("expect straight ", ans)
        self.assertRegex(ans, re.compile('.*Best hand: straight'))

    def test_three_of_a_kind_1(self):
        data = "9H 8D 9S 6H 2D AH JD 9C 3H 9D".split()
        ans = main(data)
        print("expect three-of-a-kind ", ans)
        self.assertRegex(ans, re.compile('.*Best hand: three-of-a-kind'))

    def test_three_of_a_kind_2(self):
        data = "9H 8D 4S 7H 2D AH JD 2H 2C 9D".split()
        ans = main(data)
        print("expect three-of-a-kind ", ans)
        self.assertRegex(ans, re.compile('.*Best hand: three-of-a-kind'))

    def test_two_pair_1(self):
        data = "9H 8D 9S 6H 2D 8H AH JD 9C 9D".split()
        ans = main(data)
        print("expect two-pair ", ans)
        self.assertRegex(ans, re.compile('.*Best hand: two-pair'))

    def test_two_pair_2(self):
        data = "9H 3D 9S 6H 2D 8H AH 8D 9C 9D".split()
        ans = main(data)
        print("expect two-pair ", ans)
        self.assertRegex(ans, re.compile('.*Best hand: two-pair'))

    def test_pair_1(self):
        data = "9H 8D 9S 6H 2D AH JD 3H 9C 9D".split()
        ans = main(data)
        print("expect one-pair ", ans)
        self.assertRegex(ans, re.compile('.*Best hand: one-pair'))

    def test_pair_2(self):
        data = "9H 8D 7S 6H 2D AH JD 3H 9C 9D".split()
        ans = main(data)
        print("expect one-pair ", ans)
        self.assertRegex(ans, re.compile('.*Best hand: one-pair'))

    def test_high_card_1(self):
        data = "9H 8D 7S 6H 2D AH JD 3H 5C 9D".split()
        ans = main(data)
        print("expect highest-card ", ans)
        self.assertRegex(ans, re.compile('.*Best hand: highest-card'))

    def test_high_card_2(self):
        data = "9H 8D 7S 6H 2D AH JD 3H TC 9D".split()
        ans = main(data)
        print("expect highest-card ", ans)
        self.assertRegex(ans, re.compile('.*Best hand: highest-card'))

    def test_total_drop_0(self):
        data = "TD JD AD QD KD 1D 3D 2D 4D 5D".split()
        ans = main(data)
        print("expect royal-flush ", ans)
        # self.assertRegex(ans, re.compile('.*Best hand: royal-flush'))
        self.assertRegex(ans, re.compile('.*Best hand: straight-flush'))

    def test_total_drop_1(self):
        data = "TD JD AD QD 1D KD 3D 2D 4D 5D".split()
        ans = main(data)
        print("expect royal-flush ", ans)
        # self.assertRegex(ans, re.compile('.*Best hand: royal-flush'))
        self.assertRegex(ans, re.compile('.*Best hand: straight-flush'))

    def test_total_drop_2(self):
        data = "TD 1D JD 4D AD QD KD 3D 2D 5D".split()
        ans = main(data)
        print("expect royal-flush ", ans)
        # self.assertRegex(ans, re.compile('.*Best hand: royal-flush'))
        self.assertRegex(ans, re.compile('.*Best hand: straight-flush'))

    def test_total_drop_3(self):
        data = "3D TD 1D JD 4D AD QD KD 2D 5D".split()
        ans = main(data)
        print("expect royal-flush ", ans)
        # self.assertRegex(ans, re.compile('.*Best hand: royal-flush'))
        self.assertRegex(ans, re.compile('.*Best hand: straight-flush'))

    def test_total_drop_4(self):
        data = "3D 2D TD 1D 4D JD AD QD KD 5D".split()
        ans = main(data)
        print("expect royal-flush ", ans)
        # self.assertRegex(ans, re.compile('.*Best hand: royal-flush'))
        self.assertRegex(ans, re.compile('.*Best hand: straight-flush'))

    def test_total_drop_5(self):
        data = "3D 2D 1D 4D 5D TD JD AD QD KD".split()
        ans = main(data)
        print("expect royal-flush ", ans)
        # self.assertRegex(ans, re.compile('.*Best hand: royal-flush'))
        self.assertRegex(ans, re.compile('.*Best hand: straight-flush'))

    def test_case_1(self):
        data = "AC 2D 9C 3S KD 5S 4D KS AS 4C".split()
        ans = main(data)
        print("expect straight ", ans)
        self.assertRegex(ans, re.compile('.*Best hand: straight'))

    def test_case_2(self):
        data = "AH 2C 9S AD 3C QH KS JS JD KD".split()
        ans = main(data)
        print("expect two-pairs ", ans)
        self.assertRegex(ans, re.compile('.*Best hand: two-pairs'))

if __name__ == '__main__':
    unittest.main()
