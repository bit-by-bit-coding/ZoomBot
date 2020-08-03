import time
"""
Classes to hold the most common types of errors
"""


class ParticipantNotFoundException(Exception):
    def __init__(self, msg):
        print(msg)


class RoomIndexNotFoundException(Exception):

    def __init__(self, msg):
        print(msg)


def send_keys_over_time(element, message, ms_per_key=50, ms_total=None):
        sec_per_key = ms_per_key if ms_total is None else ms_total/len(message)
        sec_per_key = sec_per_key/1000

        for character in message:
            element.send_keys(character)
            time.sleep(sec_per_key)
        
        return element