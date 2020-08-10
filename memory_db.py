
import time
import lbs_pb2
import json
import utility

class MemoryDB:
    def __init__(self):
        self.location_list = dict()

        self.save_file_name = "./lbs_db.json"
        self._load_file()

    def insert(self, id, latitude, longitude):
        if id not in self.location_list:
            self.location_list[id] = dict()
            self.location_list[id]["history"] = list()
            self.location_list[id]["last_position"] = dict()
        body = dict()
        body["latitude"] = latitude
        body["longitude"] = longitude
        body["time"] = time.time()
        self.location_list[id]["history"].append(body)
        self.location_list[id]["last_position"] = body
        self._save_file()

    def get_info(self, id):
        ret_body = lbs_pb2.GetResponse()
        if id in self.location_list:
            ret_body.latitude = self.location_list[id]["last_position"]['latitude']
            ret_body.longitude = self.location_list[id]["last_position"]['longitude']
            
        return ret_body

    def get_between_history(self, id, start_time, end_time):
        if id not in self.location_list:
            print("No id", id)
            raise Exception("No id")
        
        history = self.location_list[id]["history"]
        time_history = [data["time"] for data in history]

        left_index = utility.binarySearch(time_history, utility.getTimestampFromString(start_time))
        right_index = utility.binarySearch(time_history, utility.getTimestampFromString(end_time))

        return lbs_pb2.Car(id=id, history=history[left_index:right_index])

    def get_search_result(self, latitude, longitude, radius):
        ret_body = lbs_pb2.SearchResponse()

        for id in self.location_list:
            latitude2 = self.location_list[id]["last_position"]["latitude"]
            longitude2 = self.location_list[id]["last_position"]["longitude"]
            
            dist = utility.calDistance(latitude, longitude, latitude2, longitude2)
            if dist < radius:
                last_position = lbs_pb2.Location(latitude=latitude2, longitude=longitude2)
                ret_body.cars.append(lbs_pb2.Car(id=id, last_position=last_position))

        return ret_body

    def _save_file(self):
        with open(self.save_file_name, "w") as json_file:
            json.dump(self.location_list, json_file)

    def _load_file(self):
        import os
        if os.path.exists(self.save_file_name):
            with open(self.save_file_name) as json_file:
                self.location_list = json.load(json_file)
