import datetime

def hotelcost(night):
    return 3*night
def activity(day):
    if "Miami"==day:
        return 200
    elif "Texas"==day:
        return 350
    elif "Seattle"==day:
        return 150
    elif "LA"==day:
        return 400
def rental(car):
    if car>7:
        return 30*car-50
    elif car==3:
        return 40*car-60
    else:
        return car
    
def all (night, day, car):
    return hotelcost(night) + activity(day) + rental(car)
print("hotel cost", hotelcost(20), "activity", activity("Miami"), "rental", rental(10))
print("trips costs", all(4, "Miami", 3))
    
    