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

"""IdRangeSet class definition."""

from subordinate.idrange import IdRange

class IdRangeSet(object):
    """
    IdRangeSet() -> IdRangeSet object

    Returns an empty set of ranges of consecutive ids. Such a set can
    contain IdRange object which are not necessarily unique and which
    can overlap themselves.
    """

    # Constructor
    #############

    def __init__(self):
        """
        Constructor method.
        On create, the set is empty.
        """

        self.__range = []

    # Special methods
    #################

    def __contains__(self, item):
        """Return True if item is an id in self."""

        if isinstance(item, int):
            for r in self.__range:
                if item in r:
                    return True
        return False

    def __getitem__(self, key):
        """Return self[key]."""

        if isinstance(key, int):
            return self.__range[key]
        else:
            raise TypeError(
                    "{} indices must be integers, not {}".format(
                        self.__class__.__name__,
                        key.__class__.__name__
                        )
                    )

    def __iter__(self):
        """Implement iter(self)."""

        return IdRangeSetIterator(self)

    def __len__(self):
        """Return the number of ranges in the set."""

        return len(self.__range)

    def __str__(self):
        """Return str(self)."""

        return "{}()".format(self.__class__.__name__)

    # Miscellaneous
    ###############

    __slots__ = ['_IdRangeSet__range']

    # Public methods
    ################

    def append(self, first, count):
        """
        Add to the set a range of count consecutive ids
        starting at id first.
        """

        self.__range.append(IdRange(first, count))

    def clear(self):
        """Remove all ranges of ids from the set."""

        del self.__range[:]

    def remove(self, first, count):
        """
        Remove a range of count consecutive ids starting at id first
        from all the ranges in the set.
        """

        # Avoid trivialities
        if first < 0 or count < 1:
            return

        new_range = []
        last = first + count - 1
        for r in self.__range:
            if first <= r.last and r.first <= last:
                # There is an overlap
                if r.first < first:
                    new_range.append(IdRange(r.first, first-r.first))
                if last < r.last:
                    new_range.append(IdRange(last+1, r.last-last))
            else:
                # No overlap, range is kept
                new_range.append(r)

        self.__range = new_range

    def simplify(self):
        """
        Reorganize the ranges in the set in order to ensure that each range
        is unique and that there is not overlap between to ranges.
        """

        # Sort the ranges
        self.__range.sort()

        new_range = []
        new_first = self.__range[0].first
        new_count = self.__range[0].count

        for r in self.__range:
            if r.first == new_first:
                # Longest range starting at new_first
                new_count = r.count
            elif r.first <= new_first + new_count:
                # Overlapping ranges
                if new_first + new_count - 1 < r.last:
                    # There is a part of the range to add to the new range
                    new_count = r.last - new_first + 1
            else:
                # No overlap, this is a new disjoint range
                new_range.append(IdRange(new_first, new_count))
                new_first = r.first
                new_count = r.count

        # End of the last range
        new_range.append(IdRange(new_first, new_count))

        self.__range = new_range


class IdRangeSetIterator(object):
    """
    Iterator class for IdRangeSet.
    """

    # Constructor
    #############

    def __init__(self, range_set):
        """Constructor method."""

        if not isinstance(range_set, IdRangeSet):
            raise TypeError(
                    "{}() argument must be an IdRangeSet object, "
                    "not {}".format(
                        self.__class__.__name__,
                        range_set.__class__.__name__
                        )
                    )

        self.__current = -1
        self.__set = range_set

    # Special methods
    #################

    def __iter__(self):
        """Implement iter(self)."""

        return self

    def __next__(self):
        """Implement next(self)."""

        if self.__current + 1 < len(self.__set):
            self.__current += 1
            return self.__set[self.__current]
        else:
            raise StopIteration

    # Miscellaneous
    ###############

    __slots__ = [
            '_IdRangeSetIterator__current',
            '_IdRangeSetIterator__set'
            ]
