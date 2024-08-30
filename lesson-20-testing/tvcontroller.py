
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
        if len(self.channels) - 1 < n:
            raise ValueError(f'Channel {n} is not in {self.channels}')

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


