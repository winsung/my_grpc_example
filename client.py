from __future__ import print_function
import time

import grpc

import lbs_pb2
import lbs_pb2_grpc

import random

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = lbs_pb2_grpc.LocationBaseServiceStub(channel)
        """
        for i in range(100):
            id = "test" + str(i)
            latitude = 37.498031428803806 + random.random()
            longitude = 127.0277740816078 + random.random()
            stub.put(lbs_pb2.PutRequest(id=id, latitude=latitude, longitude=longitude))   
            time.sleep(0.5)
        
        for i in range(10):
            id = "test1"
            latitude = 37.498031428803806 + random.random()
            longitude = 127.0277740816078 + random.random()
            stub.put(lbs_pb2.PutRequest(id=id, latitude=latitude, longitude=longitude))   
            time.sleep(1)
        """
        response = stub.get(lbs_pb2.GetRequest(id="test1"))
        print("Client received: ", response)

        response = stub.history(lbs_pb2.HistoryRequest(id="test1", start_time="2020-01-07 19:18:58", end_time="2020-01-07 23:00:00"))
        print("Client received: ", response)
        
        response = stub.search(lbs_pb2.SearchRequest(latitude=37.4908, longitude=127.02741, radius=10000))
        print("Client received: ", response)

        

if __name__ == '__main__':
    run()