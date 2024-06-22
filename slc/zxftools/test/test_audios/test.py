import unittest
from unittest.mock import patch, MagicMock
from azure.cognitiveservices.speech import SpeechConfig, SpeechRecognizer, AudioConfig, SpeechSynthesizer, AudioOutputConfig
import os

from zxftools.audios import du
from zxftools.audios import ListenSpeak,Speaker,recognize_from_microphone_single

class TestAudio(unittest.TestCase):

    def test_du(self):
        du()




class TestSpeechModule(unittest.TestCase):

    def setUp(self):
        # 设置环境变量
        os.environ['SPEECH_KEY'] = 'your-speech-key'
        os.environ['SPEECH_REGION'] = 'your-speech-region'

    @patch('speech_module.speechsdk.SpeechRecognizer')
    @patch('speech_module.speechsdk.AudioConfig')
    def test_recognize_from_microphone_single(self, mock_audio_config, mock_speech_recognizer):
        # 测试recognize_from_microphone_single函数
        mock_recognizer = MagicMock()
        mock_recognizer.recognize_once_async.return_value.get.return_value = MagicMock(reason='some_reason', text='test speech')
        mock_speech_recognizer.return_value = mock_recognizer
        mock_audio_config.return_value = MagicMock()

        from speech_module import recognize_from_microphone_single
        recognize_from_microphone_single()

        # 验证是否正确调用了recognize_once_async
        mock_recognizer.recognize_once_async.assert_called_once()

    @patch('speech_module.speechsdk.SpeechSynthesizer')
    @patch('speech_module.speechsdk.AudioOutputConfig')
    def test_speaker_speak(self, mock_audio_output_config, mock_speech_synthesizer):
        # 测试Speaker类的speak方法
        speaker = Speaker()
        mock_synthesizer = MagicMock()
        mock_synthesizer.speak_ssml_async.return_value.get.return_value = MagicMock(reason='SynthesizingAudioCompleted')
        mock_speech_synthesizer.return_value = mock_synthesizer
        mock_audio_output_config.return_value = MagicMock()

        ssml = "<speak>Test SSML</speak>"
        speaker.run(ssml)

        # 验证是否正确调用了speak_ssml_async
        mock_synthesizer.speak_ssml_async.assert_called_once_with(ssml)

    @patch('speech_module.speechsdk.SpeechRecognizer')
    @patch('speech_module.speechsdk.AudioConfig')
    def test_listenspeak_listen(self, mock_audio_config, mock_speech_recognizer):
        # 测试ListenSpeak类的listen方法
        listenspeak = ListenSpeak()
        mock_recognizer = MagicMock()
        mock_recognizer.recognize_once_async.return_value.get.return_value = MagicMock(reason='RecognizedSpeech', text='listen test')
        mock_speech_recognizer.return_value = mock_recognizer
        mock_audio_config.return_value = MagicMock()

        result = listenspeak.listen()

        # 验证返回值是否正确
        self.assertEqual(result, 'listen test')

    @patch('speech_module.speechsdk.SpeechSynthesizer')
    @patch('speech_module.speechsdk.AudioOutputConfig')
    def test_listenspeak_speak(self, mock_audio_output_config, mock_speech_synthesizer):
        # 测试ListenSpeak类的speak方法
        listenspeak = ListenSpeak()
        mock_synthesizer = MagicMock()
        mock_synthesizer.speak_text_async.return_value.get.return_value = MagicMock(reason='SynthesizingAudioCompleted')
        mock_speech_synthesizer.return_value = mock_synthesizer
        mock_audio_output_config.return_value = MagicMock()

        result = listenspeak.speak('test speak')

        # 验证返回值是否正确
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()