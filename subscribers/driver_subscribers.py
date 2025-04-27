from dispatcher import dispatcher
from events import DriverStatusChanged

def driver_status_logger(event: DriverStatusChanged):
    print(f"[DriverSubscriber] Driver {event.driver_id} changed status to {event.new_status}")

dispatcher.subscribe(DriverStatusChanged, driver_status_logger)
