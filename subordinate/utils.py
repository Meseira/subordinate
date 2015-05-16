"""Utilities for Subordinate."""

class BadIdFile(Exception):
    """
    BadIdFile(id_filename, lineno, message) -> BadIdFile object

    Exception raised when an id file is not correctly formatted.
    """

    # Constructor
    #############

    def __init__(self, id_filename, lineno, message):
        """
        Constructor method.
        On raise, the exception contains the name id_filename of the
        incorrectly formatted id file and the line number lineno
        containing the problem. The argument message should give some
        informations about the problem.
        """

        super().__init__(
                str(message) +
                '\nfile: ' + str(id_filename) + ', line: ' + str(lineno)
                )

        self.id_filename = id_filename
        self.lineno = lineno

class Config(object):
    """
    Config() -> Config object

    Basic object containing class attributes for Subordinate's configuration.
    """

    # Default user/group subordinate id files
    user_sub_id_file = '/etc/subuid'
    group_sub_id_file = '/etc/subgid'

def subordinate_no_del(name):
    """Function raising AttributeError on del for read only attribute."""

    raise AttributeError("readonly attribute")

def subordinate_no_set(name, value):
    """Function raising AttributeError on set for read only attribute."""

    raise AttributeError("readonly attribute")
