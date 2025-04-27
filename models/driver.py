from models.enums import DriverStatus
from datetime import datetime
from constants import MAX_VIOLATIONS_ALLOWED

class Driver:
    
    MAX_VIOLATIONS_ALLOWED = MAX_VIOLATIONS_ALLOWED
     
     
    def __init__(self, driver_id, name, date_of_birth, driving_licence_number, status=DriverStatus.ACTIVE, violations=None):
        self.driver_id = driver_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.driving_licence_number = driving_licence_number
        self.status = status
        self.status_history = [(status, datetime.now())]
        self.violations = violations if violations else []
        self.time_until_no_longer_banned = 0

    def is_eligible_to_hire_car(self) -> bool:
        return self.status == DriverStatus.ACTIVE and len(self.violations) < self.MAX_VIOLATIONS_ALLOWED

    def ban(self): 
        if self.status != DriverStatus.BANNED:
            self.update_status(DriverStatus.BANNED)

    def add_violation_record(self, violation: str): 
        self.violations.append(violation)
        if len(self.violations) >= self.MAX_VIOLATIONS_ALLOWED:
            self.ban()

    def update_status(self, new_status: DriverStatus): 
        if new_status != self.status:
            self.status = new_status
            self.status_history.append((new_status, datetime.now()))

    def get_status_history(self):
        return [(status.value, timestamp) for status, timestamp in self.status_history]

    def __str__(self):
        return f"Driver {self.driver_id} - {self.name} ({self.status.value})"