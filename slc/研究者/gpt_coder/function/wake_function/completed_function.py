
class WakeResult:
    def __init__(self, sound, light, status, duration):
        self.sound = sound
        self.light = light
        self.status = status
        self.duration = duration

def wake_completed_functiontion(decibels, wake_word):
    if decibels >= 80 or wake_word == "wake_word":
        return WakeResult(sound="bi", light="on", status="working", duration=3600)
    else:
        return WakeResult(sound="none", light="off", status="idle", duration=0)
