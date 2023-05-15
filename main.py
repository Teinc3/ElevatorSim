# Feels good coming back to python after a long time.
# Aim: Simulate an elevator system and find the "Best" elevator algorithm.
# In terms of time or energy or both.

import random
import elevator as Elevator
import passenger as Passenger

# First define constants/variables

accel = 1
maxSpeed = 3
floors = 10 # Floors 0-9
floorHeight = 4
maxPassengers = 10
stoppingTime = 10

systemEnergyUsed = 0

elevators = []
waitingPassengers = []

# Now define the main function. This is where the simulation will be run.

def main():

    # Initially, generate passengers and add them to the waitingPassengers list.
    for i in range(0, 15):
        origin = random.randint(0, floors)
        destination = random.randint(0, floors)
        while destination == origin:
            destination = random.randint(0, floors)
        waitingPassengers.append(Passenger(origin, destination))
    
    # Now generate elevators. We will test elevators that can go to all floors first.
    elevators.append(Elevator("all"))
    elevators.append(Elevator("all"))

    # Now run the simulation until all passengers have reached their destination.
    while len(waitingPassengers) > 0 or len(elevators[0].currentPassengerList > 0) or len(elevators[1].currentPassengerList > 0):
        for elevator in elevators:
            elevator.tick()
        for passenger in waitingPassengers:
            passenger.timeElapsed += 1
        
        for passenger in waitingPassengers:
            if passenger.timeElapsed >= abs(passenger.destinationFloor - passenger.originFloor) * floorHeight:
                waitingPassengers.remove(passenger)
    