# Abstract base class defining programming language interface
from abc import ABCMeta, abstractmethod
from platform import java_ver

# Base class for programming languages
class programing(metaclass=ABCMeta):
     @abstractmethod
     def has_oop(self):
          # Abstract method to check if language has OOP support
          pass

# Python implementation
class python(programing):
     def has_oop(self):
          # Python has OOP support
          return "Yes"

# Java implementation  
class python(programing):
     def has_oop(self):
          # Java has OOP support
          return "No"

# Create instance of Java
one = java_ver()
# Print whether Java has OOP
print(one.has_oop())
