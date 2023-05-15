# Now define the passenger class. When a passenger is created, it is assigned a random floor to go to and random destination floor.

class Passenger:

    def __init__(self, origin, destination):
        self.originFloor = origin
        self.destinationFloor = destination
    
    timeElapsed = 0 # This is the time elapsed since the passenger was created. Will stop counting once passenger arrives at destination.