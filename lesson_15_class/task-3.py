# Task 3
# TV controller
# Create a simple prototype of a TV controller in Python. It’ll use the following commands:
# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name'
# exists in the list, or "No" - in the other case.

# The default channel turned on before all commands is №1.
# Your task is to create the TVController class and methods described above.


class TVController:
    channel = 1  # channel number

    def __init__(self, channels: list) -> None:
        self.channels = channels

    def current_channel(self) -> str:
        return self.channels[TVController.channel - 1]

    def first_channel(self) -> str:
        TVController.channel = 1
        return self.current_channel()

    def last_channel(self) -> str:
        TVController.channel = len(self.channels)
        return self.current_channel()

    def turn_channel(self, n: int) -> str:
        TVController.channel = n
        return self.current_channel()

    def next_channel(self) -> str:
        TVController.channel += 1
        if TVController.channel == len(self.channels):
            TVController.channel = 1
        return self.current_channel()

    def previous_channel(self) -> str:
        TVController.channel -= 1
        if TVController.channel == 0:
            TVController.channel = len(self.channels)
        return self.current_channel()

    def is_exist(self, channel: str | int) -> str:
        if type(channel) == str:
            return "Yes" if channel in self.channels else "No"
        else:
            return "Yes" if channel <= len(self.channels) else "No"


CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)

assert controller.first_channel() == "BBC"
assert controller.last_channel() == "TV1000"
assert controller.turn_channel(1) == "BBC"
assert controller.next_channel() == "Discovery"
assert controller.previous_channel() == "BBC"
assert controller.current_channel() == "BBC"
assert controller.is_exist(4) == "No"
assert controller.is_exist("BBC") == "Yes"
