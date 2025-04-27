
from dispatcher import dispatcher
from events import RentalRequestCreated
from models.driver import Driver
from models.vehicle import Vehicle
from services import billing_service
from services.assignment_service import AssignmentService

# happy path = the user has less than 5 violations
vehicle = Vehicle(
    vehicle_id="V001",
    manufacturer="Toyota",
    model="Corolla",
    basic_cost_to_hire=100,
    year_of_production=2018,
    mileage=30000
)

driver = Driver(
    driver_id="D001",
    name="Billy Thorn",
    date_of_birth="1990-10-25",
    driving_licence_number="ABCD1234"
)

billing_service.vehicles[vehicle.vehicle_id] = vehicle
billing_service.drivers[driver.driver_id] = driver

driver.add_violation_record("Speeding")
driver.add_violation_record("Parking ticket")
driver.add_violation_record("DUI")


AssignmentService.assign_vehicle_to_driver(vehicle, driver)


dispatcher.publish(RentalRequestCreated(
    request_id="R001",
    driver_id=driver.driver_id,
    vehicle_id=vehicle.vehicle_id,
    days_requested=5,
    average_miles_per_day=30
))


# happy path = the user has less than 5 violations
vehicle = Vehicle(
    vehicle_id="V003",
    manufacturer="Toyota",
    model="Corolla",
    basic_cost_to_hire=110,
    year_of_production=2013,
    mileage=110000
)

driver = Driver(
    driver_id="D003",
    name="Sally Thorn",
    date_of_birth="1993-10-24",
    driving_licence_number="ABCD1434"
)

billing_service.vehicles[vehicle.vehicle_id] = vehicle
billing_service.drivers[driver.driver_id] = driver

driver.add_violation_record("Speeding")



AssignmentService.assign_vehicle_to_driver(vehicle, driver)


dispatcher.publish(RentalRequestCreated(
    request_id="R003",
    driver_id=driver.driver_id,
    vehicle_id=vehicle.vehicle_id,
    days_requested=5,
    average_miles_per_day=30
))
