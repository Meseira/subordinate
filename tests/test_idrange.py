from unittest import TestCase

from subordinate.idrange import IdRange

class TestIdRange(TestCase):

    def test_attributes(self):

        val_first = 10
        val_count = 5
        t = IdRange(val_first, val_count)

        self.assertEqual(t.first, val_first)
        # Attribute first is readonly
        with self.assertRaises(AttributeError):
            t.first = val_first+1
        with self.assertRaises(AttributeError):
            del t.first

        self.assertEqual(t.count, val_count)
        # Attribute count is readonly
        with self.assertRaises(AttributeError):
            t.count = t.count+1
        with self.assertRaises(AttributeError):
            del t.count

        self.assertEqual(t.last, val_first+val_count-1)
        # Attribute last is readonly
        with self.assertRaises(AttributeError):
            t.last = t.last+1
        with self.assertRaises(AttributeError):
            del t.last

    def test_comparisons(self):

        t1 = IdRange(10, 1)
        t2 = IdRange(10, 2)
        t3 = IdRange(11, 1)
        t4 = IdRange(11, 2)

        # Equality
        self.assertTrue(t1 == t1)
        self.assertFalse(t1 == t2 or t1 == t3 or t1 == t4)

        # Greater or equal
        self.assertTrue(t1 >= t1)
        self.assertFalse(t1 >= t2 or t1 >= t3 or t1 >= t4)
        self.assertTrue(t4 >= t1 and t4 >= t2 and t4 >= t3)

        # Greater than
        self.assertFalse(t1 > t1)
        self.assertFalse(t1 > t2 or t1 > t3 or t1 > t4)
        self.assertTrue(t4 > t1 and t4 > t2 and t4 > t3)

        # Lower or equal
        self.assertTrue(t1 <= t1)
        self.assertTrue(t1 <= t2 and t1 <= t3 and t1 <= t4)
        self.assertFalse(t4 <= t1 or t4 <= t2 or t4 <= t3)

        # Lower than
        self.assertFalse(t1 < t1)
        self.assertTrue(t1 < t2 and t1 < t3 and t1 < t4)
        self.assertFalse(t4 < t1 or t4 < t2 or t4 < t3)

        # Non equality
        self.assertFalse(t1 != t1)
        self.assertTrue(t1 != t2 and t1 != t3 and t1 != t4)

    def test_constructor(self):

        # Argument first must be a non-negative integer
        with self.assertRaises(ValueError):
            t = IdRange(-1, 1)

        # Argument count must be a positive integer
        with self.assertRaises(ValueError):
            t = IdRange(0, 0)

    def test_values_in_range(self):

        val_first = 10
        val_count = 5
        t = IdRange(val_first, val_count)

        for val_id in range(val_first, val_first+val_count):
            self.assertTrue(val_id in t)
