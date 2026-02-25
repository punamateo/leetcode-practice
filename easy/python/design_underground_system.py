# https://leetcode.com/problems/design-underground-system/

# from dataclasses import dataclass

# @dataclass
# class StationLog:

class PassengerNotCheckedInException(Exception):
    """ Raised when a passenger wants to check out without checking in"""

class UndergroundSystem:
    def __init__(self):
        self.station_logs = dict()
        self.passenger_status = dict()
        self.passenger_logs = dict()
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passenger_status[id] = {"checkIn": {"station": stationName, "time": t}}
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:

        if "checkIn" not in self.passenger_status[id]:
            raise PassengerNotCheckedInException(f"{id} in {stationName}")

        self.passenger_status[id]["checkOut"] = {"station": stationName, "time": t}

        start_station = self.passenger_status[id]["checkIn"]["station"]
        end_station = stationName

        trip_time = t - self.passenger_status[id]["checkIn"]["time"]

        trip_name = f"{start_station}-{end_station}"

        if not trip_name in self.station_logs:
            self.station_logs[trip_name] = []

        self.station_logs[trip_name].append(trip_time)

        if id not in self.passenger_logs:
            self.passenger_logs[id] = []

        self.passenger_logs[id].append({"checkIn": self.passenger_status[id]["checkIn"] ,"checkOut": self.passenger_status[id]["checkOut"]})
        self.passenger_status[id] = None




    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = f"{startStation}-{endStation}"
        return sum(self.station_logs[key])/len(self.station_logs[key])

        


# Your UndergroundSystem object will be instantiated and called as such:
undergroundSystem = UndergroundSystem();

undergroundSystem.checkIn(10, "Leyton", 3);
undergroundSystem.checkOut(10, "Paradise", 8); # Customer 10 "Leyton" -> "Paradise" in 8-3 = 5


print(undergroundSystem.passenger_logs)
print(undergroundSystem.station_logs)

undergroundSystem.checkIn(5, "Leyton", 10);
undergroundSystem.checkOut(5, "Paradise", 16); #Customer 5 "Leyton" -> "Paradise" in 16-10 = 6
print(undergroundSystem.getAverageTime("Leyton", "Paradise")); # return 5.50000, (5 + 6) / 2 = 5.5
undergroundSystem.checkIn(2, "Leyton", 21);
undergroundSystem.checkOut(2, "Paradise", 30); # Customer 2 "Leyton" -> "Paradise" in 30-21 = 9
print(undergroundSystem.getAverageTime("Leyton", "Paradise")); #return 6.66667, (5 + 6 + 9) / 3 = 6.66667

print(undergroundSystem.passenger_logs)
print(undergroundSystem.station_logs)