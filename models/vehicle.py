from models.enums import VehicleStatus
from datetime import datetime

class Vehicle:
    
    def __init__(self, vehicle_id, manufacturer, model, basic_cost_to_hire, year_of_production, mileage, status=VehicleStatus.AVAILABLE):
        self.vehicle_id = vehicle_id
        self.manufacturer = manufacturer
        self.model = model
        self.basic_cost_to_hire = basic_cost_to_hire
        self.year_of_production = year_of_production
        self.mileage = mileage
        self.status = status
        self.status_history = [(status, datetime.now())]
        self.assigned_driver_id = None

    def mark_as_needs_maintenance(self):
        self.status = VehicleStatus.NEEDS_MAINTENANCE
        self.track_status("Vehicle marked for maintenance.")

    def mark_as_available(self):
        self.status = VehicleStatus.AVAILABLE
        self.assigned_driver_id = None
        self.track_status("Vehicle is now available.")

    def assign_driver_to_vehicle(self, driver_id): 
        if self.status != VehicleStatus.AVAILABLE:
            raise Exception(f"Vehicle {self.vehicle_id} is not available.")
        self.assigned_driver_id = driver_id
        self.status = VehicleStatus.ASSIGNED
        self.track_status(f"Assigned to driver {driver_id}.")

    def track_status(self, note=""):
        self.status_history.append((self.status, datetime.now(), note))

    def get_status_history(self):
        return [(status.value, timestamp, note) for status, timestamp, note in self.status_history]

    def print_status(self):
        return f"Vehicle {self.vehicle_id} is currently '{self.status.value}'."