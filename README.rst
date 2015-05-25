Subordinate
===========

Introduction
------------

Subordinate user/group ids appear in Linux kernel 3.12 in 2013. The goal of subordinate ids is to give to a user or a group an id range in addition to his own id. These additional ids can be used for various activities such as, for example, running an unpriviledged LXC_ container.

The ranges given to the users of a system are listed, by default, in */etc/subuid* (see */etc/subgid* for the groups). The format of each line is *name:id_first:id_count* and means that the user/group *name* has at his disposal a range of *id_count* ids starting at *id_first*. Note that there are some restrictions about the id ranges which can be given (see *man login.defs*).

**Subordinate** is a Python module to make easier the handling of these id files in a Python framework. The module **Subordinate** provides several tools to create and manage maps between names and ids, read id files and produce strings formatted in the good way for being directly used in a GNU/Linux environment.

Getting started
---------------

**Subordinate** comes with a *setup.py* file for taking advantage of the facilities provided by the package **Setuptools**. In a virtual environment or in your own system, you can install it with the help of the following command,

  ``$ python setup.py install``

Then, start a Python session and import *subordinate*,

>>> import subordinate

Two classes are directly available: *UserIdMap* for users' subordinate ids (by default, based on */etc/subuid*) and *GroupIdMap* for groups' subordinate ids (by default, based on */etc/subgid*). The two classes are derived from *IdMap* and behave similarly. Let's see how *UserIdMap* can be used! First, simply load an *UserIdMap* object and print its content in a proper format,

>>> user_map = subordinate.UserIdMap()
>>> print(user_map.write_string())

At this point, you should see the content of your */etc/subuid* file (at least, if such a file exists in your environment) up to some shuffle in the order of the lines.

Before giving a range to a user, this user has to be added to the map. Then, he will appear in the list of the names contained in the map but, if he was not present before, with no range,

>>> user_map.append('my_user')
>>> user_map.names()
[ ..., 'my_user', ... ]
>>> len(user_map['my_user'])
0

The class of *user_map['my_user']* is *IdRangeSet*. Objects derived from this class are set of id ranges which are not assumed to be unique in the set and which can overlap themselves. To give a range of *65536* ids starting at id *1000000* to *my_user*, use the method *append* of *IdRangeSet*,

>>> user_map['my_user'].append(1000000, 65536)
>>> len(user_map['my_user'])
1

You can check that the range has been added by printing the map's content again. You can check that a given id belongs to *my_user* and you also can do a reverse check to know who owns a given id,

>>> 1000000 in user_map['my_user']
True
>>> user_map.who_has(1000000)
['my_user']

Note that additional user names can appear in the list returned by the method *who_has*. Indeed, it is allowed to give a same range of ids to several users.

An *IdRangeSet* is a container for *IdRange* objects. Such an object has three readonly attributes *first*, *last* and *count*,

>>> r = user_map['my_user'][0]
>>> print("Range: {}-{} ({} ids)".format(r.first, r.last, r.count))
Range: 1000000-1065535 (65536 ids)

An *IdRangeSet* can contain multiple *IdRange* instances and allow to manipulate them. As we saw, ranges can be added to the set but a range can also be removed from all the ranges in the set,

>>> user_map['my_user'].append(1000100, 32)
>>> user_map['my_user'].append(1000116, 32)
>>> user_map['my_user'].append(1000116, 32)
>>> user_map['my_user'].append(1000200, 32)
>>> for r in user_map['my_user']:
...   print("Range: {}-{} ({} ids)".format(r.first, r.last, r.count))
Range: 1000000-1065535 (65536 ids)
Range: 1000100-1000131 (32 ids)
Range: 1000116-1000147 (32 ids)
Range: 1000116-1000147 (32 ids)
Range: 1000200-1000231 (32 ids)
>>>
>>> user_map['my_user'].remove(1000120, 10)
>>> for r in user_map['my_user']:
...   print("Range: {}-{} ({} ids)".format(r.first, r.last, r.count))
Range: 1000000-1000119 (120 ids)
Range: 1000130-1065535 (65406 ids)
Range: 1000100-1000119 (20 ids)
Range: 1000130-1000131 (2 ids)
Range: 1000116-1000119 (4 ids)
Range: 1000130-1000147 (18 ids)
Range: 1000116-1000119 (4 ids)
Range: 1000130-1000147 (18 ids)
Range: 1000200-1000231 (32 ids)

As you can see, a set can become a bit chaotic and it will make harder to read the associated id file (again, try to print the map's content). To tackle this problem, the class *IdRangeSet* has a method *simplify* which avoid ids to belong to multiple ranges in the set and join consecutive ranges to get a simpler a set,

>>> user_map['my_user'].simplify()
>>> for r in user_map['my_user']:
...   print("Range: {}-{} ({} ids)".format(r.first, r.last, r.count))
Range: 1000000-1000119 (120 ids)
Range: 1000130-1065535 (65406 ids)

Finally, you can remove an user and his id range set from the map with the method *remove* or remove all the users with the method *clear*,

>>> user_map.remove('my_user')
>>> user_map.clear()

Notes
-----

The module **Subordinate** has been written for Python version 3 and the compatibility with version 2 is not assured. It has been tested and works well with version 3.4.

If you encounter any problem with this module, do not hesitate to report it in a `GitHub issue`_.

.. _GitHub issue: https://github.com/Meseira/subordinate/issues
.. _LXC: https://linuxcontainers.org/
