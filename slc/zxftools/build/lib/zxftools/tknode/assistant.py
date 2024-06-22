import azure.cognitiveservices.speech as speechsdk

class Good_Listener():
    def __init__(self):
        speech_config = speechsdk.SpeechConfig(
            subscription=os.environ.get('SPEECH_KEY', '3950d0d62b924e5b99b43198edd700fb'),
            region=os.environ.get('SPEECH_REGION', 'eastus'))
        speech_config.speech_recognition_language = "zh-CN"
        speech_config.request_word_level_timestamps()
        audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
        self.last_interaction_time = None
        self._sets(speech_config, audio_config)

    def start_cb(self, evt):
        print('SESSION STARTED: {}'.format(evt))

    def recognized_handler(self, e: speechsdk.SpeechRecognitionEventArgs):
        print('RECOGNIZED: {}'.format(e))
        print(speechsdk.ResultReason.RecognizedSpeech == e.result.reason,
              'speechsdk.ResultReason.RecognizedSpeech == e.result.reason')
        if speechsdk.ResultReason.RecognizedSpeech == e.result.reason and len(e.result.text) > 0:
            print("Recognized: {}".format(e.result.text))
            print("Offset in Ticks: {}".format(e.result.offset))
            print("Duration in Ticks: {}".format(e.result.duration))

    def recognizing_handler(self, e: speechsdk.SpeechRecognitionEventArgs):
        print('RECOGNIZING: {}'.format(e))

    def stop_cb(self, evt):

        print('11 CLOSING on {}'.format(evt))
        self.speech_recognizer.stop_continuous_recognition()

    def cancel_cb(self, evt):
        pass

    def _sets(self, speech_config, audio_config):
        self.speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
        self.speech_recognizer.session_started.connect(self.start_cb)
        self.speech_recognizer.recognizing.connect(self.recognizing_handler)
        self.speech_recognizer.recognized.connect(self.recognized_handler)
        self.speech_recognizer.session_stopped.connect(self.stop_cb)
        self.speech_recognizer.canceled.connect(self.cancel_cb)

    def start(self, second: int = 20):
        # last_interaction_time = time.time() to recognized_handler
        self.last_interaction_time = time.time()
        self.speech_recognizer.start_continuous_recognition()
        # self.speech_recognizer.start_transcribing_async()
        while True:
            time.sleep(.5)

            if time.time() - self.last_interaction_time > second:
                self.speech_recognizer.stop_continuous_recognition()
                # self.speech_recognizer.start_transcribing_async()
                break


# 添加声音缓存
from openai import OpenAI as opai_audio
from IPython.display import Audio, display
import os
import time
import pygame

def openai_speaker(text="Hello world! This is a streaming test."):
    """
    mp3 aac  | flac |  ['mp3', 'opus', 'aac', 'flac', 'wav', 'pcm']
    0.25 to 4.0. 1.0 is the default.
    alloy, echo, fable, onyx, nova, and shimmer
    """
    api_key = os.environ.get('OPENAI_API_KEY')
    client = opai_audio(api_key=api_key)
    time.sleep(0.5)
    global response
    response = client.audio.speech.create(
        model="audios-1",
        voice="onyx",
        input=text,
        response_format='wav'
    )
    final = 'tempx.wav'

    pygame.init()
    pygame.mixer.init()
    response.stream_to_file(final)
    if os.path.exists(final):
        pygame.mixer.music.load(final)
        pygame.mixer.music.play()
        # display(Audio(final, autoplay=True))
        os.remove(final)