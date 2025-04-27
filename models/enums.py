from enum import Enum

class VehicleStatus(Enum):
    AVAILABLE = "Available"
    ASSIGNED = "Assigned"
    NEEDS_MAINTENANCE = "Needs Maintenance"

class DriverStatus(Enum):
    ACTIVE = "Active"
    BANNED = "Banned"