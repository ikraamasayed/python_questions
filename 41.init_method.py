#   init method is just like constructor in c++ and java . But incase of c++ and java if we don't create constructor the program creates one implicitly . Incase of python we hacae create init method explicitly


class Car:
    def __init__(self):
        self.wheels = 4
        self.driver_seat = 1

BMW = Car() # no need to provide the arguments 
print(BMW.wheels,BMW.driver_seat)