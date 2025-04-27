from models.vehicle import Vehicle
from models.driver import Driver
from models.enums import VehicleStatus
from dispatcher import dispatcher
from events import VehicleStatusChanged

class AssignmentService:

             
    @staticmethod
    def assign_vehicle_to_driver(vehicle: Vehicle, driver: Driver):
        if not driver.is_eligible_to_hire_car():
            raise Exception(f"Driver {driver.driver_id} is not eligible to hire a car (Status: {driver.status.value}, Violations: {len(driver.violations)}).")
            
        if vehicle.status != VehicleStatus.AVAILABLE:
            raise Exception(f"Vehicle {vehicle.vehicle_id} is not available for assignment.")

        vehicle.assign_driver_to_vehicle(driver.driver_id)
      
        dispatcher.publish(VehicleStatusChanged(vehicle_id=vehicle.vehicle_id, new_status=vehicle.status.value))