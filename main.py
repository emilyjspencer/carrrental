from models.driver import Driver
from models.vehicle import Vehicle
from dispatcher import dispatcher



from services import billing_service
from services.assignment_service import AssignmentService

# unhappy path = the driver has 5 violations so not eligible to hire a car
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
    name="John Doe",
    date_of_birth="1985-10-25",
    driving_licence_number="ABCD1234"
)

billing_service.vehicles[vehicle.vehicle_id] = vehicle
billing_service.drivers[driver.driver_id] = driver


driver.add_violation_record("Speeding")
driver.add_violation_record("Parking ticket")
driver.add_violation_record("Reckless driving")
driver.add_violation_record("Running red light")
driver.add_violation_record("Driving without insurance")


AssignmentService.assign_vehicle_to_driver(vehicle, driver)



