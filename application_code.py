from datetime import datetime
from typing import Union
import math

class Person:
    """
    A class representing a person with attributes such as name, age, year of birth, and salary details.

    Attributes:
        _first_name (str): The first name of the person.
        _last_name (str): The last name of the person.
        _yob (int): The year of birth of the person.
        _base_salary (int): The base salary of the person.
        _bonus (float): The bonus percentage of the salary.
    """

    def __init__(self, first_name: str = '', last_name: str = '', year: int = None):
        """
        Initializes the Person instance.

        Args:
            first_name (str): The first name of the person (default: '').
            last_name (str): The last name of the person (default: '').
            year (int): The year of birth of the person (default: None).
        """
        self._first_name = first_name
        self._last_name = last_name
        self._yob = year
        self._base_salary = None
        self._bonus = None

    @property
    def age(self):
        """
        Returns:
            int: The age of the person based on their year of birth.
        """
        if self._yob is not None:
            return datetime.now().year - self._yob
        return None

    def set_birth_year(self, year: int):
        """
        Sets the year of birth.

        Args:
            year (int): The year of birth.

        Raises:
            ValueError: If the year is not an integer.
        """
        if not isinstance(year, int):
            raise ValueError('Year must be of type int')
        self._yob = year

    @property
    def full_name(self) -> str:
        """
        Returns:
            str: The full name of the person.
        """
        return f"{self._first_name} {self._last_name}".strip()

    @full_name.setter
    def full_name(self, f_name: str = None) -> None:
        """
        Sets the first and last name.

        Args:
            f_name (str): Full name string with first and last names.

        Raises:
            ValueError: If the input is not a string or does not include both first and last names.
        """
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
        """
        Returns:
            Union[float, int]: The total salary including bonus.
        """
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
            base_salary (int): The base salary.
            bonus (Union[float, int]): The bonus percentage.

        Raises:
            ValueError: If the inputs are invalid.
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


class Circle:
    """
    A class to represent a circle with attributes like radius, diameter, and area.

    Attributes:
        _radius (Union[int, float]): The radius of the circle.
        _area (Union[int, float]): The area of the circle.
    """

    def __init__(self, radius):
        """
        Initializes the Circle instance.

        Args:
            radius (Union[int, float]): The radius of the circle.
        """
        self._radius = radius
        self._area = None

    @property
    def radius(self) -> Union[int, float]:
        """Returns the radius of the circle."""
        return self._radius

    @radius.setter
    def radius(self, radius: Union[int, float]) -> None:
        """
        Sets the radius of the circle.

        Args:
            radius (Union[int, float]): The radius value.

        Raises:
            ValueError: If the radius is invalid.
        """
        if not isinstance(radius, (int, float)):
            raise ValueError('Radius must be either int or float')
        if radius < 0:
            raise ValueError('Radius must be a positive integer')
        self._radius = radius
        self._area = None

    @property
    def diameter(self) -> Union[int, float]:
        """Returns the diameter of the circle."""
        return 2 * self._radius

    @diameter.setter
    def diameter(self, diameter: Union[int, float]) -> None:
        """
        Sets the diameter of the circle.

        Args:
            diameter (Union[int, float]): The diameter value.

        Raises:
            ValueError: If the diameter is invalid.
        """
        if not isinstance(diameter, (int, float)):
            raise ValueError('Diameter must be either int or float')
        self._radius = diameter / 2
        self._area = None

    @property
    def area(self) -> Union[int, float]:
        """
        Returns the area of the circle. If the area is not already calculated, it computes and caches it.

        Returns:
            Union[int, float]: The area of the circle.
        """
        if self._area is None:
            self._area = math.pi * self._radius * self._radius
        return self._area


class Vehicle:
    """
    A class to represent a vehicle.

    Attributes:
        vehicle_count (int): Class attribute to count the number of vehicles created.
    """

    vehicle_count = 0

    def __init__(self, manufacturer, car_make, year):
        """
        Initializes the Vehicle instance.

        Args:
            manufacturer (str): The manufacturer of the vehicle.
            car_make (str): The make of the vehicle.
            year (int): The year of manufacturing.
        """
        Vehicle.vehicle_count += 1

    @classmethod
    def get_vehicle_count(cls):
        """Returns the total number of vehicles created."""
        return cls.vehicle_count

    @staticmethod
    def classify_vehicle(arg):
        """
        Classifies a vehicle.

        Args:
            arg (str): Description of the vehicle.

        Returns:
            str: A classification string.
        """
        return f"This is a {arg}"


class ElectricVehicle(Vehicle):
    """
    A subclass of Vehicle for electric vehicles.
    """

    @staticmethod
    def classify_vehicle(arg):
        """
        Classifies an electric vehicle.

        Args:
            arg (str): Description of the vehicle.

        Returns:
            str: A classification string.
        """
        return f"This is an electric {arg}"


class DynamicClass:
    """
    A class demonstrating dynamic attributes.
    """

    static_value = 0

    def __init__(self):
        pass

    def dynamic_attr(self, name, obj):
        """
        Dynamically sets an attribute.

        Args:
            name (str): The name of the attribute.
            obj: The value to assign.
        """
        setattr(self, name, obj)


class ValidatedAttribute:
    """
    A class to manage attributes with validation for positive numeric values.

    Attributes:
        _value (Union[int, float]): The validated value.
    """

    def __init__(self, value: Union[int, float] = None) -> None:
        """Initializes the ValidatedAttribute instance."""
        self._value = None

    @property
    def value(self) -> Union[int, float]:
        """Returns the validated value."""
        return self._value

    @value.setter
    def value(self, value: Union[int, float]) -> None:
        """
        Sets the value with validation.

        Args:
            value (Union[int, float]): The new value.

        Raises:
            ValueError: If the value is invalid.
        """
        if not isinstance(value, (int, float)):
            raise ValueError('Value must be either int or float')
        if value <= 0:
            raise ValueError('Value must be positive')
        self._value = value
