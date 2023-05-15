# Now define the elevator class.

class Elevator:

    currentAccel = 0
    currentSpeed = 0 # Positive for up, negative for down, 0 for stationary
    currentHeight = 0
    currentStopTime = 0 # Time elapsed since the elevator stopped at a floor
    currentPassangerList = [] # List of passanger objects currently in the elevator

    def __init__(self, availableFloors): # Can be "all", "odd" or "even" 
        self.availableFloors = availableFloors
    
    def tick(self): # This function is called every second.

        # Add Power used by the elevator to the system energy used.
        systemEnergyUsed += abs(len(self.currentPassangerList) * self.currentSpeed * self.currentAccel)
        
        # Change the speed and move the elevator
        self.currentSpeed += self.currentAccel
        self.currentHeight += self.currentSpeed
                
        # Check if the elevator has reached a floor. If so, take appropriate action.
        if self.currentHeight % floorHeight == 0 and self.currentSpeed == 0:
            # and (self.currentStopTime <= stoppingTime or st)
            # If the elevator is at a floor, check if there are any passengers to be dropped off.
            for passenger in self.currentPassangerList:
                if passenger.destinationFloor * floorHeight == self.currentHeight:
                    self.currentPassangerList.remove(passenger)
                    passenger.allocatedElevator = None

            # Increase the stop time, if stop time is greater than stopping time, then calculate strategy.
            self.currentStopTime += 1
            if self.currentStopTime >= stoppingTime:
                self.currentStopTime = 0
                self.currentAccel = self.calculateStrategy()


        return 0
    
    # This function will be called every tick. It calculates the strategy of the elevator (such as whether or not to pick up a passenger) and sets the acceleration accordingly.
    def calculateStrategy(self):
        # Gives the acceleration of the elevator based on the strategy.
        return 0
    

