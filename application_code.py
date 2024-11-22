from datetime import datetime
from typing import Union
import math

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


class Circle:
    """ Circle class which has manages radius, diameter and area """
    def __init__(self, radius):
        self._radius = radius
        self._area = None

    @property
    def radius(self)->Union[int, float]:
        return self._radius
    
    @radius.setter
    def radius(self, radius:Union[int, float])->None:
        if not isinstance (radius, (int, float)):
            raise ValueError ('Radius must be either int or float')

        if radius < 0:
            raise ValueError ('Radius must be a positive integer')
        
        self._radius = radius
        self._area = None

    @property
    def diameter(self)->Union[int, float]:
        return 2*self._radius
    
    @diameter.setter
    def diameter(self, diameter:Union[int, float])->None:
        if not isinstance (diameter, (int, float)):
            raise ValueError ('Diameter must be either int or float')
        
        self._radius = diameter/2
        self._area = None

    @property
    def area(self)->Union[int, float]:
        if self._area == None:
            self._area = math.pi*self._radius*self._radius
            return self._area
        else:
            return self._area
    

class Vehicle:
    vehicle_count = 0
    
    def __init__(self, manufacturer, car_make, year):
        manufacturer = manufacturer
        car_make = car_make
        year = year
        Vehicle.vehicle_count += 1

    @classmethod
    def get_vehicle_count(cls):
        return cls.vehicle_count
    
    @staticmethod
    def classify_vehicle(arg):
        return (f"This is a {arg}")


class ElectricVehicle(Vehicle):
    @staticmethod
    def classify_vehicle(arg):
        return (f"This is an electric {arg}")


class DynamicClass:
    static_value = 0

    def __init__(self):
        pass

    def dynamic_attr(self, name, obj):
        self.name = obj



class ValidatedAttribute:
    def __init__(self, value:Union[int, float]=None)->None:
        self._value = None

    @property
    def value(self)->Union[int, float]:
        return self._value
    
    @value.setter
    def value(self, value:Union[int, float])->None:
        if value <= 0:
            raise ValueError('Value must a positive')
        if not isinstance(value, (int, float)):
            raise ValueError('Value must be either int or float')
        
        self._value = value