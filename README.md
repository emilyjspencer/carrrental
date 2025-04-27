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




