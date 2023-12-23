class RemoteControl:

    def __init__(self, sound, channel):
        self.sound = sound
        self.channel = channel

    def get_sound(self):
        return self.sound

    def set_sound(self, sound):
        self.sound = sound

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel
