.. _query-language:

The Query Language
==================

We recommend reading :ref:`defining-data-model` before reading this section.

Along with the Data Model language, the SDK offers the possibility to specify `queries` defined over data models.

The :mod:`~oef.query` module implements the API that allows you to:

* Query the OEF Node about specific kind of services
* Query other agents to ask them the desired resources.

In one sentence, a `query` is a set of `constraints`, defined over a `data model`.
The outcome is a set of `description` (that is, instances of :class:`~oef.schema.Description`)
`matching` with the query. That is, all the description whose attributes satisfy the constraints in the query.

In the next sections, we describe how to build queries with the SDK.

Constraints
-----------

A `constraint` is associated with an `attribute name` and imposes restrictions on the domain of that attribute.
That is, it imposes some limitations on the values the attribute can assume.

We have different types of constraints:

* `relation` constraints:

  * the author of the book must be `Stephen King`
  * the publication year must be greater than 1990

* `set` constraints:

  * the genre must fall into the following set of genres: `Horror`, `Science fiction`, `Non-fiction`.

* `range` constraints:

  * the average rating must be between 3.5 and 4.5

* `distance` constraints:

  * the nearest bookshop must be within a distance from a given location.

The class that implements the constraint concept is :class:`~oef.query.Constraint`
In the following, we show how to define them in the Python SDK.

Relation
~~~~~~~~

The :class:`~oef.query.Relation` is a constraint type that allows you to impose specific values for the attributes.

The types of relation constraints are:

* Equal: :class:`~oef.query.Eq`
* Not Equal: :class:`~oef.query.NotEq`
* Less than: :class:`~oef.query.Lt`
* Less than or Equal: :class:`~oef.query.LtEq`
* Greater than: :class:`~oef.query.Gt`
* Greater than or Equal: :class:`~oef.query.GtEq`

**Examples**: using the attributes we used before: :ref:`defining-data-model`

.. code-block:: python

    from oef.query import Constraint, Eq, NotEq, Lt, LtEq, Gt, GtEq

    # all the books whose author is Stephen King
    Constraint("author", Eq("Stephen King"))

    # all the books that are not of the genre Horror
    Constraint("genre", NotEq("Horror"))

    # all the books published before 1990
    Constraint("year", Lt(1990))

    # the same of before, but including 1990
    Constraint("year", LtEq(1990))

    # all the books with rating greater than 4.0
    Constraint("average_rating", Gt(4.0))

    # all the books published after 2000, included
    Constraint("year", GtEq(2000))


Set
~~~

The :class:`~oef.query.Set` is a constraint type that allows you to restrict the values of the attribute
in a specific set.

There are two kind of ``Set`` constraints:

* In (a set of values): :class:`~oef.query.In`
* Not in (a set of values): :class:`~oef.query.NotIn`


**Examples**:

.. code-block:: python

    from oef.query import Constraint, In, NotIn

    # all the books whose genre is one of `Horror`, `Science fiction`, `Non-fiction`
    Constraint("genre", In(["horror", "science fiction", "non-fiction"]))

    # all the books that have not been published neither in 1990, nor in 1995, nor in 2000
    Constraint("year", NotIn([1990, 1995, 2000]))


Range
~~~~~

The :class:`~oef.query.Range` is a constraint type that allows you to restrict the values of the attribute in a given
range.


**Examples**:

.. code-block:: python

    from oef.query import Constraint, Range

    # all the books whose title is between 'A' and 'B' (alphanumeric order)
    Constraint("title",   Range(("A", "B")))

    # all the books that have been published between 1960 and 1970
    Constraint("genre",   Range((1960, 1970))


Distance
~~~~~~~~~

The :class:`~oef.query.Distance` is a constraint type that allows you to put a limit on a :class:`~oef.schema.Location`
attribute type. More specifically, you can set a maximum distance from a given location (the `center`),
such that will be considered only the instances whose location attribute value is within a distance from the center.

**Examples**:

.. code-block:: python

    from oef.query import Constraint, Distance
    from oef.schema import Location, Description

    # define a location of interest, e.g. the Tour Eiffel
    tour_eiffel = Location(48.8581064, 2.29447)

    # find all the locations close to the Tour Eiffel within 1 km
    close_to_tour_eiffel = Constraint("position", Distance(tour_eiffel, 1.0))

    # Le Jules Verne, a famous restaurant close to the Tour Eiffel, satisfies the constraint.
    le_jules_verne_restaurant = Location(48.8579675, 2.2951849)
    close_to_tour_eiffel.check(Description({"position": le_jules_verne_restaurant}))  # gives `True`

    # The Colosseum does not satisfy the constraint (farther than 1 km from the Tour Eiffel).
    colosseum = Location(41.8902102, 12.4922309)
    close_to_tour_eiffel.check(Description({"position": colosseum}))  # gives `False`


Constraint Expressions
----------------------

The constraints above mentioned can be combined with the common logical operators (i.e. and, or and not), yielding
more complex expression.

In particular we can specify any conjunction/disjunction/negations of the previous constraints or composite constraint
expressions, e.g.:

* books that belong to `Horror` **and** has been published after 2000, but **not** published by `Stephen King`.
* books whose author is **either** `J. K. Rowling` **or** `J. R. R. Tolkien`


The classes that implement these operators are :class:`~oef.query.Not`, :class:`~oef.query.And`
and :class:`~oef.query.Or`.

Not
~~~

The :class:`~oef.query.Not` is a constraint expression that allows you to specify a negation of a constraint expression.
The :class:`~oef.query.Not` constraint is satisfied whenever its subexpression is `not` satisfied.

**Example**:

.. code-block:: python

    from oef.query import Constraint, Not, Range

    # all the books whose year of publication is not between 1990 and 2000
    Not(Constraint("year", Range((1990, 2000)))


And
~~~

The :class:`~oef.query.And` is a constraint type that allows you to specify a conjunction of constraints
over an attribute. That is, the :class:`~oef.query.And` constraint is satisfied whenever all the subexpressions
that constitute the `and` are satisfied.

Notice: the number of subexpressions must be **at least** 2.

**Example**:

.. code-block:: python

    from oef.query import Constraint, And, NotEq, Range

    # all the books whose title is between 'I' and 'J' (alphanumeric order) but not equal to 'It'
    And([Constraint("title", Range(("I", "J"))), Constraint("title", NotEq("It"))])

Or
~~

The :class:`~oef.query.Or` is a constraint type that allows you to specify a disjunction of constraints. That is, the
``Or`` constraint is satisfied whenever at least one of the constraints that constitute the ``or`` is satisfied.

Notice: the number of subexpressions must be **at least** 2.

**Example**:

.. code-block:: python

    from oef.query import Constraint, Or, Lt, Gt

    # all the books that have been published either before the year 1960 or after the year 1970
    Or([Constraint("year", Lt(1960)), Constraint("year", Gt(1970))])


Queries
-------

A `query` is simply a `list of constraint expressions`, interpreted as a conjunction
(that is, a matching description with the query must satisfy `every` constraint expression.)

**Examples**:

.. code-block:: python

    from oef.query import Query, Constraint, Eq, Gt, Eq

    # return all the books written by Stephen King published after 1990, and available as an e-book:
    Query([
        Constraint("author", Eq("Stephen King")),
        Constraint("year", Gt(1990)),
        Constraint("ebook_available", Eq(True))
    ], book_model)

Where ``book_model`` is the ``DataModel`` object defined in :ref:`defining-data-model`. However, the data model is
an optional parameter, but to avoid ambiguity is recommended to include it.

The ``check`` method
~~~~~~~~~~~~~~~~~~~~

The :class:`~oef.query.Query` class supports a way to check whether a :class:`~oef.schema.Description` matches with the
query. This method is called :func:`~oef.query.Query.check`.

Examples:

.. code-block:: python

    from oef.query import Query, Constraint, Eq, Gt, Eq
    from oef.schema import Description

    q = Query([
        Constraint("author", Eq("Stephen King")),
        Constraint("year", Gt(1990)),
        Constraint("ebook_available", Eq(True))
        ])

    # With a query, you can check that a `~oef.schema.Description` object satisfies the constraints.

    q.check(Description({"author": "Stephen King", "year": 1991, "ebook_available": True}))  # True
    q.check(Description({"author": "George Orwell", "year": 1948, "ebook_available": False})) # False


Validity
~~~~~~~~

A :class:`~oef.query.Query` object must satisfy some conditions in order to be instantiated.

- The list of constraints expressions can't be empty; must have at least one constraint expression.
- If the data model is specified:

    - For every constraint expression that constitute the query, check if they are `valid wrt the data model`.


A :class:`~oef.query.ConstraintExpr` `c` (that is, one of :class:`~oef.query.And`, :class:`~oef.query.Or`,
:class:`~oef.query.Not`, :class:`~oef.query.Constraint`) is `valid wrt a` :class:`~oef.query.DataModel` if:

- If `c` is an instance of :class:`~oef.query.And`, :class:`~oef.query.Or` or :class:`~oef.query.Not`, then
  every subexpression of `c` must be valid (wrt to the data model);
- If `c` is an instance of :class:`~oef.query.Constraint`, then:

    - if the constraint type is one of :class:`~oef.query.Lt`, :class:`~oef.query.LtEq`, :class:`~oef.query.Gt`,
      :class:`~oef.query.Gt`, the value in the constructor must be one of ``str``, ``int`` or ``float``.
    - if the constraint type is a :class:`~oef.query.Range`, then the types in the range must be one of ``int``, ``str``,
      ``float`` or :class:`~oef.schema.Location`.
    - if the constraint type is a :class:`~oef.query.Distance`, then the only valid type is :class:`~oef.schema.Location`.
    - if the constraint type is a :class:`~oef.query.Set`, then the types supported are
      ``str``, ``int``, ``float``, ``bool``, :class:`~oef.schema.Location`. Notice though that a set of ``bool`` is trivial,
      so you may find yourself more comfortable by using other alternatives.
    - for the other constraint types, i.e. :class:`~oef.query.Eq` and :class:`~oef.query.NotEq`, the value can be one of the
      allowed types for :class:`~oef.schema.AttributeSchema`, that is ``str``, ``int``, ``float``, ``bool``,
      :class:`~oef.schema.Location`.

- Moreover, when `c` is a :class:`~oef.query.Constraint`, the attribute must have a consistent type wrt the data model.
  E.g. consider a :class:`~oef.query.Constraint` like:

.. code-block:: python

  Constraint("foo", Eq(True)))

Consider a :class:`~oef.schema.DataModel` where there is an :class:`~oef.schema.AttributeSchema`
``"foo"`` of type ``str``. Then the constraint is not compatible with the mentioned data model, because
the constraint expect an equality comparison with a boolean ``True``, instead of a ``str``.


