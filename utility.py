import time
import datetime
import math

def binarySearch(nums, target):
    if len(nums) == 0:
        return -1

    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

def getTimestampFromString(date):
    try:
        timestamp = time.mktime(datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S').timetuple())
        return timestamp
    except Exception as ex:
        print(ex)
        raise Exception("Cannot convert to timestamp")

def calDistance(latitude1, longitude1, latitude2, longitude2):
    theta = longitude1 - longitude2
    dist = math.sin(degToRad(latitude1)) * math.sin(degToRad(latitude2)) + math.cos(degToRad(latitude1)) * math.cos(degToRad(latitude2)) * math.cos(degToRad(theta))
    dist = math.acos(dist)
    dist = radToDeg(dist)

    # meter convert
    dist = dist * 60 * 1.1515
    dist = dist * 1.609344
    dist = dist * 1000.0

    return dist

def degToRad(deg):
    return deg * math.pi / 180.0

def radToDeg(rad):
    return rad * 180.0 / math.pi