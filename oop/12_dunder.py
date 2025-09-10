class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # human readable representation
    def __str__(self):
        return f"first_name: {self.first_name}, last_name: {self.last_name}"

    # machne readable representation
    def __repr__(self):
        return f"{self.__class__.__name__} ({self.first_name!r}, {self.last_name!r})"

    def __eq__(self, other):
        if self is other:
            return True
        elif not isinstance(other, Person):
            return False
        else:
            return (
                self.first_name == other.first_name
                and self.last_name == other.last_name
            )


person = Person("John", "Doe")
person_2 = Person("John", "Doe")
print(person)
print(repr(person))
print(person == person_2)
