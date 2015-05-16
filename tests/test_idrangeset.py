# This file is part of Subordinate
#
# Copyright (C) 2015 Xavier Gendre
#
# Subordinate is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Subordinate is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Subordinate. If not, see <http://www.gnu.org/licenses/>.

from unittest import TestCase

from subordinate.idrange import IdRange
from subordinate.idrangeset import IdRangeSet

class TestIdRangeSet(TestCase):

    def test_array_syntax(self):

        s = IdRangeSet()
        s.append(10, 5)

        self.assertEqual(len(s), 1)

        self.assertEqual(s[0], IdRange(10, 5))
        with self.assertRaises(IndexError):
            s[1]

        self.assertEqual(s[-1], IdRange(10, 5))
        with self.assertRaises(IndexError):
            s[-2]

    def test_ids_in_set(self):

        s = IdRangeSet()
        s.append(10, 5)

        for val_id in range(10, 15):
            self.assertTrue(val_id in s)
        for val_id in range(15, 20):
            self.assertFalse(val_id in s)

    def test_iterator(self):

        s = IdRangeSet()
        s.append(10, 5)

        it = iter(s)
        r = next(it)

        self.assertEqual(r, IdRange(10, 5))
        with self.assertRaises(StopIteration):
            next(it)

    def test_modify_set(self):

        s = IdRangeSet()

        s.append(10, 5)
        s.clear()
        self.assertEqual(len(s), 0)

        s.append(10, 5)
        s.append(10, 5)
        s.remove(12, 1)
        self.assertEqual(len(s), 4)
        self.assertFalse(12 in s)

    def test_simplify(self):

        s = IdRangeSet()
        s.append(10, 5)
        s.append(10, 10)
        s.append(12, 1)
        s.append(20, 5)
        s.append(22, 8)
        s.append(40, 5)

        s.simplify()
        self.assertEqual(len(s), 2)
        self.assertEqual(s[0].first, 10)
        self.assertEqual(s[0].last, 29)
        self.assertEqual(s[1].first, 40)
        self.assertEqual(s[1].last, 44)
