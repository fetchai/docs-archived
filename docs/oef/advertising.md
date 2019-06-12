Agents advertise their services with schemas. 

Schemas describe services in a language agnostic manner, after which they are serialised by the SDK. 


### Defining schemas

A `schema` describes an agent, service, or resource with a set of `attributes`.

To specify data models and descriptions in Python use the <a href="http://oef-sdk-docs.fetch.ai/oef.html#oef-schema" target=_blank>`oef.schema` module</a>.


### Attributes

An `attribute` is an abstract definition of a property. It is identified by a `name` that must be unique in a given schema.

Each attribute has a `type` which specifies possible values.

Currently, we support the following attribute types:

* `strings`
* `integers`
* `booleans`
* `floats`
* `locations` (latitude, longitude)

An attribute of a schema can be `optional` in the case where an attribute is inapplicable.

Attribues can also have descriptions. Let's look at a bookshop scenario.

A bookshop may like to include the following properties of its books as attributes in the SDK:

* `title`
* `author`
* `genre` (e.g. science fiction, horror)
* `year of publication`
* `average rating` (average of the ratings between 0 and 5)
* `ISBN` code
* Whether it is available as e-book. 

For example, in Python, using the `AttributeSchema` class, we instantiate `Attributes` with attribute name, type, whether it is a required attribute, and a description:

``` python
from oef.schema import AttributeSchema, Location

    attr_title    = AttributeSchema("title" ,          str,      True,  "The title of the book.")
    attr_author   = AttributeSchema("author" ,         str,      True,  "The author of the book.")
    attr_genre    = AttributeSchema("genre",           str,      True,  "The genre of the book.")
    attr_year     = AttributeSchema("year",            int,      True,  "The year of publication of the book.")
    attr_avg_rat  = AttributeSchema("average_rating",  float,    False, "The average rating of the book.")
    attr_isbn     = AttributeSchema("ISBN",            str,      True,  "The ISBN.")
    attr_ebook    = AttributeSchema("ebook_available", bool,     False, "If the book can be sold as an e-book.")
    attr_bookshop = AttributeSchema("bookshop_pos",    Location, False, "The location of the bookshop where you can find the book")
```


### Data model

A `DataModel` is a set of `attributes`. 

Let's group the book attributes into a `DataModel` called `book`. 

In Python, this looks like this:

``` python
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

```


A `DataModel` class requires a name, a list of attributes, and an optional description.



### Description

A `Description` is  an instantiated data model. Instantiated `Description` classes for the bookshop may look like this:

``` python
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
```

`Attributes` are instantiated as part of a `Description` using a dictionary where:

* `key` = the name of the attributes.
* `value` = the values associated with the attribute key.

Note that in the latter book we were able to omit the ``average_rating`` field because it was optional. 

In the `oef-sdk-python/examples/weather` folder, you will find the `weather_schema.py` file describing the data advertised by a weather service.

``` python
from oef.schema import DataModel, AttributeSchema

  WIND_SPEED_ATTR = AttributeSchema("wind_speed",
                                  bool,
                                  is_attribute_required=True,
                                  attribute_description="Provides wind speed measurements.")

  TEMPERATURE_ATTR = AttributeSchema("temperature",
                                   bool,
                                   is_attribute_required=True,
                                   attribute_description="Provides temperature measurements.")

  AIR_PRESSURE_ATTR = AttributeSchema("air_pressure",
                                    bool,
                                    is_attribute_required=True,
                                    attribute_description="Provides air pressure measurements.")

  HUMIDITY_ATTR = AttributeSchema("humidity",
                                bool,
                                is_attribute_required=True,
                                attribute_description="Provides humidity measurements.")


  WEATHER_DATA_MODEL = DataModel("weather_data",
                               [WIND_SPEED_ATTR, TEMPERATURE_ATTR, AIR_PRESSURE_ATTR, HUMIDITY_ATTR],
                               "All possible weather data.")
```
The `WeatherStation` class in the same directory, implements the behaviour of the weather station by creating a service description that mirrors the schema.

``` python
	weather_service_description = Description(
	        {
	            "wind_speed": False,
	            "temperature": True,
	            "air_pressure": True,
	            "humidity": True,
	        },
	        WEATHER_DATA_MODEL
	    )
```

### Searching for schemas

Agents searching for services do not have to match the advertised schema precisely as the OEF executes a fuzzy search algorithm/learned matching.


<br/>