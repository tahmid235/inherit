class Parent:
    def __init__(self, Eye, Hair):
        self.Eyes = Eye
        self.Hair = Hair

class Child(Parent):
    def __init__(self, Eye, Hair):
        super().__init__(Eye, Hair)

Father = Parent("Brown", "Black")
Son = Child(Father.Eyes, Father.Hair)

print(Son.Eyes)
