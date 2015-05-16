"""IdMap class definition and its derivatives."""

from subordinate.idrangeset import IdRangeSet
from subordinate.utils import BadIdFile, Config

class IdMap(object):
    """
    IdMap(id_file) -> IdMap object

    Returns a map between names and ids. This map can be loaded from
    a file such as '/etc/subuid' or '/etc/subgid' and edited to add
    or remove ids ranges.
    """

    # Constructor
    #############

    def __init__(self):
        """
        Constructor method.
        On create, the map is empty.
        """

        self.__map = {}

    # Special methods
    #################

    def __contains__(self, name):
        """Return name in self."""

        return name in self.__map

    def __getitem__(self, name):
        """Return self[name]."""

        return self.__map[name]

    def __len__(self):
        """Return len(self)."""

        return len(self.__map)

    def __str__(self):
        """Return str(self)."""

        return "{}()".format(self.__class__.__name__)

    # Miscellaneous
    ###############

    __slots__ = ['_IdMap__map']

    # Public methods
    ################

    def append(self, name):
        """If name is not in the map, append it with an empty id range set."""

        if not isinstance(name, str):
            raise TypeError(
                    "argument 'name' must be a string, not {}".format(
                        name.__class__.__name__
                        )
                    )

        if not name:
            raise ValueError("argument 'name' cannot be empty")

        if not name in self.__map:
            self.__map[name] = IdRangeSet()

    def clear(self):
        """Remove all names and id range sets from the map."""

        self.__map.clear()

    def get(self, name, default=None):
        """
        Return the IdRangeSet object associated to name if name is in the map,
        else default.
        """

        return self.__map.get(name, default)

    def names(self):
        """Return a list containing the names in the map."""

        return list(self.__map.keys())

    def read(self, id_filename):
        """
        Attempt to read and parse the file named id_filename.
        """

        with open(id_filename, 'rt') as id_file:
            self.read_file(id_file)

    def read_file(self, id_file):
        """
        Read and parse id data from id_file which must be an iterable
        yielding Unicode strings formatted as in '/etc/subuid' or
        '/etc/subgid'.
        """

        lineno = 0
        for line in id_file:
            lineno += 1
            id_data = line.split(':')

            if len(id_data) != 3:
                raise BadIdFile(
                        id_file.name, lineno,
                        'incorrect number of fields'
                        )

            name = id_data[0]
            try:
                first, count = int(id_data[1]), int(id_data[2])
            except ValueError:
                raise BadIdFile(
                        id_file.name, lineno,
                        'cannot get the id range'
                        )

            # Append the new range
            if not name in self.__map:
                self.__map[name] = IdRangeSet()
            self.__map[name].append(first, count)

    def remove(self, name):
        """
        If name is in the map, remove it and its id range set,
        else raise KeyError.
        """

        del self.__map[name]

    def write_string(self):
        """
        Return a representation of the id map as a string. This string is
        properly formatted to be written in '/etc/subuid' or '/etc/subgid'.
        """

        map_as_str = []
        for name, id_range_set in self.__map.items():
            for id_range in id_range_set:
                map_as_str.append(
                        name + ':' +
                        str(id_range.first) + ':' +
                        str(id_range.count) + '\n'
                    )

        # Remove trailing newline
        if len(map_as_str) > 0:
            map_as_str[-1] = map_as_str[-1][:-1]

        return ''.join(map_as_str)

    def who_has(self, subid):
        """Return a list of names who own subid in their id range set."""

        answer = []
        for name in self.__map:
            if subid in self.__map[name] and not name in answer:
                answer.append(name)

        return answer

class UserIdMap(IdMap):
    """
    UserIdMap(id_file) -> UserIdMap object

    Returns a map between user names and ids.
    """

    # Constructor
    #############

    def __init__(self, id_filename=Config.user_sub_id_file):
        """
        Constructor method.
        Attempt to read and parse the file named id_filename. An empty
        map is returned if id_filename is None.
        """

        super().__init__()
        if id_filename:
            self.read(id_filename)

    # Miscellaneous
    ###############

    __slots__ = []

class GroupIdMap(IdMap):
    """
    GroupIdMap(id_file) -> GroupIdMap object

    Returns a map between group names and ids.
    """

    # Constructor
    #############

    def __init__(self, id_filename=Config.group_sub_id_file):
        """
        Constructor method.
        Attempt to read and parse the file named id_filename. An empty
        map is returned if id_filename is None.
        """

        super().__init__()
        if id_filename:
            self.read(id_filename)

    # Miscellaneous
    ###############

    __slots__ = []
