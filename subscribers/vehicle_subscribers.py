from dispatcher import dispatcher
from events import VehicleStatusChanged

def vehicle_status_logger(event: VehicleStatusChanged):
    print(f"[VehicleSubscriber] Vehicle {event.vehicle_id} changed status to {event.new_status}")

dispatcher.subscribe(VehicleStatusChanged, vehicle_status_logger)
