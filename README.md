# Domain model components

# Entities
* Driver
* Vehicle
* RentalRequest

# Value objects
* VehicleStatus e.g. Assigned, Needs maintenance, Availabble
* DriverStatus e.g. Banned, Active

# Aggregates
* Rental Request - combination of driver and vehicle

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


