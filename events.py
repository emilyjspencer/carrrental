from dataclasses import dataclass
from datetime import datetime

@dataclass
class VehicleStatusChanged:
    vehicle_id: str
    new_status: str
    timestamp: datetime = datetime.now()

@dataclass
class DriverStatusChanged:
    driver_id: str
    new_status: str
    timestamp: datetime = datetime.now()

@dataclass
class RentalRequestCreated:
    request_id: str
    #name: str
    driver_id: str
    vehicle_id: str
    days_requested: int
    average_miles_per_day: int
    timestamp: datetime = datetime.now()
