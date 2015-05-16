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

from subordinate.idmap import IdMap

class TestIdMap(TestCase):

    def test_basic_usage(self):

        m = IdMap()

        # On create, map is empty
        self.assertEqual(len(m), 0)

        # Appending an user/group
        m.append('test')
        self.assertEqual(len(m), 1)
        self.assertTrue('test' in m)
        self.assertIsNotNone(m.get('test'))
        self.assertEqual(m.names(), ['test'])

        # Only string type is allowed for user/group name
        with self.assertRaises(TypeError):
            m.append(0)

        # Adding an id range
        m['test'].append(10, 5)
        self.assertEqual(m.who_has(12), ['test'])
        self.assertEqual(m.write_string(), 'test:10:5')

        # Behavior with an unknown user/group
        self.assertFalse('unknown' in m)
        self.assertIsNone(m.get('unknown'))
        with self.assertRaises(KeyError):
            m['unknown']

        # Clear the map
        m.remove('test')
        self.assertEqual(len(m), 0)
        m.append('test')
        m.clear()
        self.assertEqual(len(m), 0)

    def test_content_of_empty_map(self):

        m = IdMap()
        self.assertEqual(m.write_string(), '')
