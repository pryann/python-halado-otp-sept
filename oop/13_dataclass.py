from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    first_name: str
    last_name: str
    age: int = 18
    school: str = "Berklee"

    def __post_init__(self):
        object.__setattr__(self, "sort_index", self.age)


person = Person("John", "Doe", 25, "MIT")
person_2 = Person("John", "Doe", 22, "SZE")
print(person)
print(person == person_2)
# person.job = "Developer"  # FrozenInstanceError

print(person > person_2)
