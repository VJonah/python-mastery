# teststock.py

import unittest
from stock import Stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)
    def test_keyword_create(self):
        s = Stock(name='GOOG',shares=100,price=490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_cost(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.cost, 100 * 490.1)

    def test_sell(self):
        s = Stock('GOOG', 100, 490.1)
        s.sell(25)
        self.assertEqual(s.shares,75)

    def test_from_row(self):
        row = ["AA",100,32.20]
        s = Stock.from_row(row)
        self.assertEqual(s.name, 'AA')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 32.20)

    def test_repr(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.__repr__(), "Stock('GOOG', 100, 490.1)")

    def test_eq(self):
        s1 = Stock('GOOG', 100, 490.1)
        s2 = Stock('GOOG', 100, 490.1)
        self.assertTrue(s1 == s2)

    def test_shares_type_error(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.shares = '50'

    def test_shares_value_error(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(ValueError):
            s.shares = -10

    def test_price_type_error(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.price = '234.3'

    def test_price_value_error(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(ValueError):
            s.price = -1234.2

    def test_non_existent_attribute_error(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(AttributeError):
            s.share = 'something'

if __name__ == '__main__':
    unittest.main()
