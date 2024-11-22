from datetime import datetime
from typing import Union

class Person:
    """Class holds the details of a person such as Name, Age, etc."""

    def __init__(self, first_name: str = '', last_name: str = '', year: int = None):
        self._first_name = first_name
        self._last_name = last_name
        self._yob = year
        self._base_salary = None
        self._bonus = None

    @property
    def age(self):
        """Returns the age of the person based on their year of birth."""
        if self._yob is not None:
            return datetime.now().year - self._yob
        return None

    def set_birth_year(self, year: int):
        """Sets the year of birth for the person."""
        if not isinstance(year, int):
            raise ValueError('Year must be of type int')
        self._yob = year

    @property
    def full_name(self) -> str:
        """Returns the full name of the person."""
        return f"{self._first_name} {self._last_name}".strip()

    @full_name.setter
    def full_name(self, f_name: str = None) -> None:
        """Sets the first and last name of the person."""
        if not isinstance(f_name, str):
            raise ValueError('Full name must be of type str')
        names = f_name.split()
        if len(names) < 2:
            raise ValueError('Full name must include both first and last names')
        self._first_name = names[0]
        self._last_name = names[1]

    @property
    def first_name(self) -> str:
        """Returns the first name of the person."""
        return self._first_name

    @property
    def last_name(self) -> str:
        """Returns the last name of the person."""
        return self._last_name

    @property
    def salary(self) -> Union[float, int]:
        """Calculates and returns the total salary including the bonus."""
        if self._base_salary is not None and self._bonus is not None:
            return self._base_salary + ((self._bonus / 100) * self._base_salary)
        return 0

    @property
    def base_salary(self) -> Union[int, None]:
        """Returns the base salary of the person."""
        return self._base_salary

    def set_salary(self, base_salary: int, bonus: Union[float, int]) -> None:
        """
        Sets the base salary and bonus percentage.

        Args:
            base_salary (int): The base salary of the person.
            bonus (Union[float, int]): The bonus percentage as a float or integer.

        Raises:
            ValueError: If base_salary is not an int or if bonus is not a float or int.
        """
        if not isinstance(base_salary, int):
            raise ValueError('Base Salary must be of type int')
        if not isinstance(bonus, (int, float)):
            raise ValueError('Bonus must be of type int or float')
        if base_salary < 0:
            raise ValueError('Base Salary must be non-negative')
        if bonus < 0:
            raise ValueError('Bonus must be non-negative')
        self._base_salary = base_salary
        self._bonus = bonus
