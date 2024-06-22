import azure.cognitiveservices.speech as speechsdk
import importlib
import os
# pip install azure-cognitiveservices-speech
def recognize_from_microphone_single():
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY','3950d0d62b924e5b99b43198edd700fb'),
                                               region=os.environ.get('SPEECH_REGION','eastus'))
    speech_config.speech_recognition_language="zh-CN"

    # audio_config = speechsdk.audio.AudioConfig(filename="YourAudioFile.wav")
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()#from_mic

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")

# recognize_from_microphone()


class Speaker():
    def __init__(self):
        speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'),
                                               region=os.environ.get('SPEECH_REGION'))
        audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
        speech_config.speech_synthesis_voice_name = 'en-US-AvaMultilingualNeural'
        # speech_config.speech_synthesis_language = "en-US"
        self.speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    def get_ssml(self, ssml_string_or_file='ssml_string', types='str'):
        if types == 'input':
            ssml_string = input("ssml")
        elif types == 'read':
            ssml_string = open(ssml_string_or_file, "r").read()
        elif types == 'str':
            ssml_string = ssml_string_or_file
        return ssml_string

    def run(self, text):

        ssml_string = self.get_ssml(text)
        speech_synthesis_result = self.speech_synthesizer.speak_ssml_async(ssml_string).get()

        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized for text [{}]".format(text))
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")


class ListenSpeak():
    def __init__(self, recognition_language="zh-CN",
                 synthesis_voice_name='zh-CN-XiaoxiaoNeural'):
        '''

        :param recognition_language: "zh-CN"
        :param synthesis_voice_name: 合成声音:
        可选包括:
        zh-CN-XiaochenNeural4、5、6（女）
        zh-CN-XiaohanNeural2、4、5、6（女）
        zh-CN-XiaomengNeural1、2、4、5、6（女）
        zh-CN-XiaomoNeural2、3、4、5、6（女）
        zh-CN-XiaoqiuNeural4、5、6（女）
        zh-CN-XiaoruiNeural2、4、5、6（女）
        zh-CN-XiaoshuangNeural2、4、5、6、8（女）
        zh-CN-XiaoxiaoNeural2、4、5、6（女）
        zh-CN-XiaoxuanNeural2、3、4、5、6（女）
        zh-CN-XiaoyanNeural4、5、6（女）
        zh-CN-XiaoyiNeural1、2、4、5、6（女）
        zh-CN-XiaoyouNeural4、5、6、8（女）
        zh-CN-XiaozhenNeural1、2、4、5、6（女）
        zh-CN-YunfengNeural1、2、4、5、6（男）
        zh-CN-YunhaoNeural1、2、4、5、6（男）
        zh-CN-YunjianNeural1、2、4、5、6（男）
        zh-CN-YunxiaNeural1、2、4、5、6（男）
        zh-CN-YunxiNeural2、3、4、5、6（男）
        zh-CN-YunyangNeural2、4、5、6（男）
        zh-CN-YunyeNeural2、3、4、5、6（男）
        zh-CN-YunzeNeural1、2、3、4、5、6（男）
        zh-HK-HiuGaaiNeural4、5、6（女）
        zh-HK-HiuMaanNeural4、5、6（女）
        zh-HK-WanLungNeural1、4、5、6（男）
        zh-TW-HsiaoChenNeural4、5、6（女）
        zh-TW-HsiaoYuNeural4、5、6（女）
        zh-TW-YunJheNeural4、5、6（男）
        '''
        try:
            speechsdk = importlib.import_module("azure.cognitiveservices.speech")
        except Exception as e:
            raise Exception(f"error {e} please install 'pip install azure***'")

        # import azure.cognitiveservices.speech as speechsdk
        SPEECH_KEY = os.environ.get('SPEECH_KEY', '6736a8b2ac6a48708eb8fa55568f4046')
        SPEECH_REGION = os.environ.get('SPEECH_REGION', 'japanwest')

        speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY,
                                               region=SPEECH_REGION)

        speech_config.speech_recognition_language = recognition_language
        speech_config.speech_synthesis_voice_name = synthesis_voice_name

        audio_config0 = speechsdk.audio.AudioConfig(use_default_microphone=True)
        self.speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config,
                                                            audio_config=audio_config0)

        audio_config1 = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
        self.speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config,
                                                              audio_config=audio_config1)

    def listen(self):
        speech_recognition_result = self.speech_recognizer.recognize_once_async().get()
        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            return speech_recognition_result.text
        else:
            return None

    def speak(self, text):
        speech_synthesis_result = self.speech_synthesizer.speak_text_async(text).get()
        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            return True
        else:
            return False

