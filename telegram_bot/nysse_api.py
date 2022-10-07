import json
import requests
from datetime import datetime, timezone


class NysseApi:
    def __init__(self):
        """ Class for handling calls to nysse traffic api. """
        self.base_url = "http://data.itsfactory.fi/journeys/api/1/"

    def parse_arrival_time_in_minutes(self, arrival_time):
        """ Parse arrival time in minutes from expected arrival date-time string """
        try:
            arrival_datetime = datetime.strptime(arrival_time, '%Y-%m-%dT%H:%M:%S.%f%z')
        except ValueError:
            arrival_datetime = datetime.strptime(arrival_time, '%Y-%m-%dT%H:%M:%S%z')
        new_time = arrival_datetime.strftime("%H:%M")
        return new_time

    def get_stop_info(self, stop_id):
        url = self.base_url + "stop-monitoring?stops=" + stop_id
        try:
            data = requests.get(url).json()["body"][stop_id]
        except (KeyError, requests.exceptions.JSONDecodeError):
            print("error")
            return
        stop_info = []
        for bus in data:
            if "expectedArrivalTime" in bus["call"]:
                arrival_time = bus["call"]["expectedArrivalTime"]
            else:
                arrival_time = bus["call"]["aimedArrivalTime"]
            stop_info.append([bus["lineRef"], self.parse_arrival_time_in_minutes(arrival_time)])
        return stop_info
