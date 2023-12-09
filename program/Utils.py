from datetime import time


def convert_time_str_to_time(time_str):
    hours = int(time_str.split(":")[0])
    minutes = int(time_str.split(":")[1])
    return time(hours, minutes)

def convert_time_str_to_time_extended(self):
    time_str = self.deadline.split(" ")[0]
    return convert_time_str_to_time(time_str)