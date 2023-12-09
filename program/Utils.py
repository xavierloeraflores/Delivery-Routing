from datetime import time


# converts a time string to a time object
def convert_time_str_to_time(time_str):
    hours = int(time_str.split(":")[0])
    minutes = int(time_str.split(":")[1])
    return time(hours, minutes)

# converts a time string to a time object with am or pm
def convert_time_str_to_time_extended(self):
    time_str = self.deadline.split(" ")[0]
    return convert_time_str_to_time(time_str)

# Prints to the terminal in red
def print_red(text):
    print("\033[91m {}\033[00m" .format(text))

# Prints to the terminal in green
def print_green(text):
    print("\033[92m {}\033[00m" .format(text))


# Prints to the terminal in blue
def print_blue(text):
    print("\033[96m {}\033[00m" .format(text))


# Prints to the terminal in yellow
def print_yellow(text):
    print("\033[93m {}\033[00m" .format(text))