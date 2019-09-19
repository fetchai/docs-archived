.. _defining-data-model:

Defining Data Models
====================

In this section, we explain how to define `data models`, an important component of the OEF.
It allows agents to describe themselves and to discover the services/resources they are interested in.

In a sentence, a `data model` is a set of `attributes`, and a `description` of an agent/service/resource is an
assignment of those attributes.

All you need to specify data models and descriptions (that is, instances of the data model) can be found in the
:mod:`~oef.schema` module.


Attributes
~~~~~~~~~~

At the lowest level of our data model language, we have the `attribute`.
An attribute is an abstract definition of a property.

It is identified by a `name`, that must be unique in a given data model (that is, we can't have two attributes
that share the same name).

Every attribute has a `type`, that specifies the domain of the property, that is, the possible values that the attribute
can assume.
At the moment, we support four types of attributes:

* strings
* integers
* booleans
* floats
* locations, i.e. pairs of (latitude, longitude)

An attribute can be `optional`, in the sense that instantiation of the attribute is not mandatory by the instances of
the data model.

Finally, every attribute might have a `description` that explains the purpose of the attribute.

**Example**: suppose we have a bookshop, and we want to describe the books we sell. Presumably, we would like to include:
the following properties of our books:

* The `title`
* The `author`
* The `genre` (e.g. science fiction, horror)
* The `year of publication`
* The `average rating` (average of the ratings between 0 and 5)
* The `ISBN` code
* If it can be sold as an e-book.

For each of this fields, we can define an attribute in the SDK by using the :class:`~oef.schema.AttributeSchema`:

.. code-block:: python

    from oef.schema import AttributeSchema, Location
    attr_title    = AttributeSchema("title" ,          str,      True,  "The title of the book.")
    attr_author   = AttributeSchema("author" ,         str,      True,  "The author of the book.")
    attr_genre    = AttributeSchema("genre",           str,      True,  "The genre of the book.")
    attr_year     = AttributeSchema("year",            int,      True,  "The year of publication of the book.")
    attr_avg_rat  = AttributeSchema("average_rating",  float,    False, "The average rating of the book.")
    attr_isbn     = AttributeSchema("ISBN",            str,      True,  "The ISBN.")
    attr_ebook    = AttributeSchema("ebook_available", bool,     False, "If the book can be sold as an e-book.")
    attr_bookshop = AttributeSchema("bookshop_pos",    Location, False, "The location of the bookshop where you "
                                                                        "can find the book")

Let's focus on the parameters of the :class:`~oef.schema.AttributeSchema` constructor:

1. the first one is the name of the attribute. It is needed to instantiate a data model and to define queries over it.
2. the second one is the type of the attribute. It specifies the domain of the possible values the attribute can assume.
   E.g. the attribute ``year`` can only be an integer, whereas the ``average_rating`` can only be a
   floating-point number.

   The supported types are: ``str``, ``int``, ``bool``, ``float`` and :class:`~oef.schema.Location`.
3. the third one is a boolean that specifies whether the attribute is `always required` or it `can be omitted`. For
   example, we might not be able to specify the ``ebook_available`` attribute, maybe because it's not applicable
   to some kind of books.
4. the fourth parameter is the description, that is a short description of the purpose of the attribute.

Data models
~~~~~~~~~~~

A `data model` is just a set of `attributes`. The class that implements the data model is
:class:`~oef.schema.DataModel`.

**Example**: let's continue with the example of the bookshop. Once we've defined the attributes, we'd like to group them
in the same structure. We can do it in the following way:

.. code-block:: python

    from oef.schema import DataModel

    book_model = DataModel("book", [
        attr_title,
        attr_author,
        attr_genre,
        attr_year,
        attr_avg_rat,
        attr_isbn,
        attr_ebook,
        attr_bookshop
    ], "A data model to describe books.")


A :class:`~oef.schema.DataModel` requires:

1. a `name` (in the example the name is ``"book"``) used to refer to the data model.
2. a `list of attributes`, that constitutes the abstract data model.
3. an (optional) `description` about the purpose of the data model.

Description
~~~~~~~~~~~

A `description` is just an `instantiation of a data model`. That is, we specify a value to every attribute belonging
to the data model we are interested in.

In the SDK, the class that implements the description is :class:`~oef.schema.Description`.

**Example**: now we have all we need to create a little catalogue about our books:

.. code-block:: python

    from oef.schema import Description

    It = Description({
        "title" :           "It",
        "author":           "Stephen King",
        "genre":            "horror",
        "year":             1986,
        "average_rating":   4.5,
        "ISBN":             "0-670-81302-8",
        "ebook_available":  True,
        "bookshop_pos":     Location(52.2057092, 0.1183431)
    }, book_model)

    _1984 = Description({
        "title" :           "1984",
        "author":           "George Orwell",
        "genre":            "novel",
        "year":             1949,
        "ISBN":             "978-0451524935",
        "ebook_available":  False
    }, book_model)

We defined the descriptions for two books, namely ``It`` and ``1984``, that refers to a data model.

The attributes are instantiated with a dictionary that has:

* as keys, the name of the attributes.
* as values, the values associated with the attributes.

Notice that in the latter book we omitted the ``average_rating`` field. We are allowed to do that because of the
``average_rating`` attribute is not mandatory.
