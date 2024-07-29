
from ac_helper import decibel_detection, wakeword_detection, make_sounds_and_light_up, work

class WakeFunctionResult:
    def __init__(self, sound, light, status, duration):
        self.sound = sound
        self.light = light
        self.status = status
        self.duration = duration

def wake_wake_function_1tion(input_decibels, wake_word_status):
    threshold = 80
    if input_decibels >= threshold or wake_word_status == "wake_word":
        make_sounds_and_light_up()
        work()
        return WakeFunctionResult(sound="bi", light="on", status="working", duration=3600)
    else:
        return WakeFunctionResult(sound="none", light="off", status="idle", duration=0)
