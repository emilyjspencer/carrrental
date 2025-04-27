from models.enums import DriverStatus
from dispatcher import dispatcher
from events import RentalRequestCreated


drivers = {}
vehicles = {}
contracts = {}

def handle_rental_request(event: RentalRequestCreated):
    driver = drivers.get(event.driver_id)
    vehicle = vehicles.get(event.vehicle_id)

    if not driver or not vehicle:
        print("[BillingService] Driver or Vehicle not found!")
        return
    
    if driver.status == DriverStatus.BANNED: # if the driver is banned - they can't
        return

    base_price = vehicle.basic_cost_to_hire

    # if the driver has some violations in their violations list - but less than 5 - add a penalty
    if 0 < len(driver.violations) <= 4:
      base_price += 100

    if vehicle.year_of_production < 2016:  # if the vehicle is quite old - deduct money
        base_price -= 15
        
    if vehicle.mileage > 100000:  # if the vehicle's mileage is over 100,000, £20 is deducted
        base_price -= 20

    total_price = base_price * event.days_requested

    contracts[event.request_id] = {
        "driver_id": event.driver_id,
        "vehicle_id": event.vehicle_id,
        "total_price_to_hire": total_price,
        "created_at": event.timestamp,
    }

    print(f"[BillingService] Rental contract created: {contracts[event.request_id]}")

dispatcher.subscribe(RentalRequestCreated, handle_rental_request)