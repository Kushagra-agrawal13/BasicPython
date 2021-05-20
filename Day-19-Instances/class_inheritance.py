# Class Inheritance

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):                     # Here Fish is inheritated from Animal
    def __init__(self):
        super().__init__()              # This super() is recommended but not strictly required.

    def breathe(self):                    # This breathe function is of Fish class, but
        super().breathe()                 # it also add an extra print statement to it .
        print("doing this underwater.")   # So, here it first prints breathe of Animal and then of Fish .

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.breathe()