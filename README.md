# Domain model components

# Entities
* Driver
* Vehicle
* RentalRequest

Explanation: each is uniquely identifiable by their respective ids driver_id, vehicle_id, rentalrequest_id

# Value objects - there are enums 
* VehicleStatus e.g. Assigned, Needs maintenance, Available
* DriverStatus e.g. Banned, Active

Explanation: the values shouldn't change, just as days of the week don't change - so enumas have been used.


# Aggregates
* Rental Request - combination of driver and vehicle information

# Services
* Billing service - calculates the cost of hiring a car
* Assignment service - assigns a driver to a car, and verifies that the user can be assigned or not - if they aren't eligible to hire a car, then they will not be assigned a vehicle.

# Bounded Contexts

* Vehicle subsystem
* Driver subsystem
* Billing subsystem

# Events

* DriverStatusChanged
* VehicleStatusChanged
* RentalRequestCreated

# Logic

* A driver is eligible to hire a car if their previous violations are less than 5
* If a driver has 5 or more previous violations - they are banned - as per as BANNED status - and cannot hire a car
* If a driver has had violations in the past - but which don't exceed 4 - then they are penalised. £100 is added to the base price to hire the car.
* If the car is nine years old or more, money is deducted when calculating the final cost to hire the car.
* The number of days required to hire the car is also taken into account.
* If the car's mileage is > 100,000, £20 is deducted


# Event-driven architecture

I decided that an event-driven system would be cleaner, enabling loose coupling because rather than components directly calling each other, they instead react to events (messages) that are published. The components therefore don't need to know about each other directly.
Additionally, the system is more extensible; it is easier to extend functionality.
The events in this system are RentalRequestCreated, DriverStatusChanged, VehicleStatusChanged

