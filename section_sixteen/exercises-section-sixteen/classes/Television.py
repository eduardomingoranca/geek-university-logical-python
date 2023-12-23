from classes.RemoteControl import RemoteControl


class Television(RemoteControl):

    def volume_up(self, sound):
        self.sound = sound + 1

    def volume_down(self, sound):
        self.sound = sound - 1

    def channel_up(self, channel):
        self.channel = channel + 1

    def channel_down(self, channel):
        self.channel = channel - 1
