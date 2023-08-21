# Method overriding is possible if one class inherits another class.
# In such case child class can override the method of the parent class

class A:
    def message(self):
        return "Hello World"
class B(A):
    def message(self):
        return "I'm Learning python"
b = B()
print(b.message())

# message() method is defined both in parent and child classes, here the child class has overridden the
# message() method that is already defined in its parent class
# both method and attributes are

