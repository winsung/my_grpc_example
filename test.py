
import time

from proto.lbs_pb2 import Location, Car
from proto.lbs_pb2_grpc import LocationBaseService

loca = Location()
loca.latitude = 36.1235
loca.longitude = 127.24124
loca.time = time.time()

my_car = Car()
my_car.id = 1
my_car.history.append(loca)
my_car.last_position.CopyFrom(loca)

print(my_car)


loca2 = Location()
loca2.latitude = 11.1235
loca2.longitude = 100.24124
loca2.time = time.time()
my_car.history.append(loca2)
my_car.last_position.CopyFrom(loca2)

print(my_car)

class LocationService(LocationBaseService):
    def put(self, request, context):
        
        return my_car