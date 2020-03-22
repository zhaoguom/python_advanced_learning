import numbers


class Field:
    pass

class IntField(Field):

    def __init__(self, db_column, min_value=None, max_value=None):
        self._value = None
        self.min_value = min_value
        self.max_value = max_value
        self.db_column = db_column
        if min_value is not None:
            if isinstance(min_value, numbers.Integral):
                raise ValueError("min_value must be int")
            elif min_value < 0:
                raise ValueError("min_value must be positive int")
        if max_value is not None:
            if isinstance(max_value, numbers.Integral):
                raise ValueError("max_value must be int")
            elif max_value < 0:
                raise ValueError("max_value must be positive int")
        if min_value is not None and max_value is not None:
            if min_value > max_value:
                raise ValueError("max_value must be bigger than min_value")

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(_value, numbers.Integral):
            raise ValueError("int value required")
        if value < self.min_value or value > self.max_value:
            raise ValueError("invalid value")
        self._value = value


class CharField(Field):
    def __init__(self, db_column, value, max_length=None):
        self._value = value
        self.db_column = db_column
        if max_length is None:
            raise ValueError("you must specify max_length for CharField")
        self.max_length = max_length

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("string value needed")
        if len(value) > self.max_length:
            raise ValueError("should not exeed the max_length")
        self._value = value


class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs, **kargs):
        fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value
        attrs_meta = attrs.get("Meta":None)
        _meta = {}
        db_table = name.lower()
        if attrs_meta is not None:
            table = getattr(attrs_meta, "db_table", None)
            if table is not None:
                db_table - table
        _meta["db_table"] = db_table
        attrs["_meta"] = _meta
        attrs["fields"] = fields
        del attrs["Meta"]
        return super().__new__(cls, name, bases, attrs, **kargs)


class User(metaclass=ModelMetaClass):

    def __init__(self):
        pass

    name = CharField(db_column="", max_length=10)
    age = IntField(db_column="", min_value=0, max_value=120)

    class Meta:
        db_table = "user"


if __name__ == "__main__":
    user = User()
    user.name = "zhaoguom"
    user.age = 28
    user.save()
