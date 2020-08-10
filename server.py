
from concurrent import futures
import time
import datetime

import grpc

import lbs_pb2
import lbs_pb2_grpc

from memory_db import MemoryDB


class LocationService(lbs_pb2_grpc.LocationBaseServiceServicer):
    def __init__(self):
        self.memory_db = MemoryDB()

    def put(self, request, context):
        id = request.id
        latitude = request.latitude
        longitude = request.longitude
        self.memory_db.insert(id, latitude, longitude)
        
        return self.memory_db.get_info(id)
    
    def get(self, request, context):
        id = request.id
        return self.memory_db.get_info(id)
    
    def history(self, request, context):
        id = request.id
        start_time = request.start_time
        end_time = request.end_time
        return self.memory_db.get_between_history(id, start_time, end_time)

    def search(self, request, context):
        latitude = request.latitude
        longitude = request.longitude
        radius = request.radius
        return self.memory_db.get_search_result(latitude, longitude, radius)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    lbs_pb2_grpc.add_LocationBaseServiceServicer_to_server(LocationService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
