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

"""IdRange class definition."""

from subordinate.utils import subordinate_no_del, subordinate_no_set

class IdRange(object):
    """
    IdRange(first, count) -> IdRange object

    Returns a virtual sequence of count consecutive ids starting at start.
    """

    # Constructor
    #############

    def __init__(self, first, count):
        """
        Constructor method.
        The sequence starts at start (must be a non-negative integer)
        and contains count (must be a positive integer) consecutive ids.
        """

        if not isinstance(first, int):
            raise TypeError(
                    "{}() argument 'first' must be an integer, "
                    "not {}".format(
                        self.__class__.__name__,
                        first.__class__.__name__
                        )
                    )

        if first < 0:
            raise ValueError(
                    "{}() argument 'first' must be a non-negative integer: "
                    "{}".format(self.__class__.__name__, first)
                    )

        if not isinstance(count, int):
            raise TypeError(
                    "{}() argument 'count' must be an integer, "
                    "not {}".format(self.__class_.__name__,
                        count.__class__.__name__
                        )
                    )

        if count < 1:
            raise ValueError(
                    "{}() argument 'count' must be a positive integer: "
                    "{}".format(self.__class__.__name__, count)
                    )

        self.__count = count
        self.__first = first

    # Special methods
    #################

    def __contains__(self, item):
        """Return item in self."""

        if isinstance(item, int):
            return self.__first <= item and item < self.__first+self.__count
        else:
            return False

    def __str__(self):
        """Return str(self)."""

        return "{}({}, {})".format(
                self.__class__.__name__,
                self.__first,
                self.__count
                )

    # Comparison methods
    ####################

    def __eq__(self, other):
        """Return self == other."""

        if isinstance(other, IdRange):
            return self.__first == other.first and self.__count == other.count
        else:
            return False

    def __ge__(self, other):
        """Return self >= other."""

        if isinstance(other, IdRange):
            if self.__first > other.first:
                return True
            else:
                return (self.__first == other.first and
                        self.__count >= other.count)
        else:
            raise TypeError(
                    "unorderable types: {}() >= {}()".format(
                        self.__class__.__name__,
                        other.__class__.__name__
                        )
                    )

    def __gt__(self, other):
        """Return self > other."""

        if isinstance(other, IdRange):
            if self.__first > other.first:
                return True
            else:
                return (self.__first == other.first and
                        self.__count > other.count)
        else:
            raise TypeError(
                    "unorderable types: {}() > {}()".format(
                        self.__class__.__name__,
                        other.__class__.__name__
                        )
                    )

    def __le__(self, other):
        """Return self <= other."""

        if isinstance(other, IdRange):
            if self.__first < other.first:
                return True
            else:
                return (self.__first == other.first and
                        self.__count <= other.count)
        else:
            raise TypeError(
                    "unorderable types: {}() <= {}()".format(
                        self.__class__.__name__,
                        other.__class__.__name__
                        )
                    )

    def __lt__(self, other):
        """Return self < other."""

        if isinstance(other, IdRange):
            if self.__first < other.first:
                return True
            else:
                return (self.__first == other.first and
                        self.__count < other.count)
        else:
            raise TypeError(
                    "unorderable types: {}() < {}()".format(
                        self.__class__.__name__,
                        other.__class__.__name__
                        )
                    )

    def __ne__(self, other):
        """Return self != other"""

        if isinstance(other, IdRange):
            return self.__first != other.first or self.__count != other.count
        else:
            return True

    # Miscellaneous
    ###############

    __hash__ = object.__hash__

    __slots__ = [
            '_IdRange__count',
            '_IdRange__first'
            ]

    # Properties
    ############

    count = property(
            lambda self: self.__count,
            subordinate_no_set,
            subordinate_no_del,
            doc="Read only attribute 'count'"
            )

    first = property(
            lambda self: self.__first,
            subordinate_no_set,
            subordinate_no_del,
            doc="Read only attribute 'first'"
            )

    last = property(
            lambda self: self.__first + self.__count - 1,
            subordinate_no_set,
            subordinate_no_del,
            doc="Read only attribute 'last'"
            )
