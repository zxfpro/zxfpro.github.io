from qet import get_llm
from IPython.core.magic import register_cell_magic

from zxftools.tknode.agentmaker import ReactAgentMaker
from zxftools import Logger
from qet import get_llm
from IPython.display import display, JSON
import time
from llama_index.llms.openai import OpenAI
from llama_index.core.llms import MessageRole
from llama_index.core.llms import ChatMessage

from llama_index.core.llms import MessageRole
from llama_index.core.llms import ChatMessage
from zxftools.tknode.tklib.tools.sheller import ShellTools
from zxftools.tknode.agentmaker import ReactAgentMaker
from zxftools import Logger
from traceloop.sdk import Traceloop
from qet import get_llm
import time

from zxftools.tknode.tklib.tools.电器控制 import ControlHome
from zxftools.tknode.tklib.tools.发布任务 import IssueAssignments
import soundfile as sf
import pyaudio
import wave
import os



from qet import get_llm
from IPython.core.magic import register_cell_magic

from zxftools.tknode.agentmaker import ReactAgentMaker
from zxftools import Logger
from qet import get_llm
from IPython.display import display, JSON

from llama_index.core.llms import MessageRole
from llama_index.core.llms import ChatMessage

from zxftools.tknode.agentmaker import ReactAgentMaker
from zxftools import Logger
from traceloop.sdk import Traceloop
from qet import get_llm
import time

from zxftools.tknode.tklib.tools.电器控制 import ControlHome
from zxftools.tknode.tklib.tools.发布任务 import IssueAssignments


# 添加声音缓存
from openai import OpenAI as opai_audio
import pygame
import azure.cognitiveservices.speech as speechsdk

import asyncio
import subprocess

import pyaudio
import wave
import os
import soundfile as sf

Traceloop.init(disable_batch=True)
logger = Logger('/Users/zhaoxuefeng/.zxf_file/log_file/llminsp.log')

class Base_Listener():
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


def check_micphone_volume(seconds = 3 ,filename = "output.wav" ,threshold=0.1):
    """
    检测n秒内的声音是否大于阈值 ,如果大于阈值返回True 否则返回False
    """
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 1
    fs = 44100  # Record at 44100 samples per second
    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    stream = p.open(format=sample_format, channels=channels,
                    rate=fs, frames_per_buffer=chunk, input=True)


    frames = []  # Initialize array to store frames
    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()
    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    data ,sample_ = sf.read('output.wav')
    decibels = max(data)

    if decibels > 0.1:
        return True
    else:
        return False


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




class Listener_v1(Base_Listener):
    result_3 = 0
    call_you = False
    fillter_prompt = """
你名叫贾维斯,是一个个人管家.你当前所处的环境中, 有你还有主人和A,B.
现在,请判断主人的输入是否是特地针对你而言,
有三种情况: 
1, 这些话是专门对你说的,与其他人无关
2, 这些话是不仅对你说,也是对在场的所有人说
3, 这些话是对别人说的,与你无关
4, 这些话有可能是对你说的,也有可能是对别人说的
---------------------------
这些是一些例子:
{few_example}
---------------------------
请根据用户的输入,判断是属于以上三种情况的哪一种,并以<result: 1>格式输出
------------------------
User: {text}
define:
    """
    fillter_example = """
'贾维斯 你在吗?' : <result: 1>
'醒醒 贾维斯,该干活了' : <result: 1>
'货架上的牛肉呢?' : <result: 4>
'你看过独行月球吗' : <result: 4>
'帮我设置日期和查看我的邮件' : <result: 4>
'朋友们 今天我们相聚在这里,大家吃的开心' : <result: 2>
'这次 我们部门干的不错' : <result: 4>
'小兰 帮我去吧花浇水' : <result: 3>
'你知道郭敬明吗？' : <result: 4>
'有多少个notebook文件' : <result: 4>
'效果还不错' : <result: 3>
'猫咪老是早上乱叫是怎么回事啊？' : <result: 4>
"""
    jar = Jarvis()
    def fillter(self, text):
        # TODO 最低3秒给回复 之后应该更快才行  速度优化

        logger.debug(f'fillter input text:{text}')
        if not text:
            return ''
        llm_openai = OpenAI()
        result = llm_openai.complete(self.fillter_prompt.format(few_example=self.fillter_example, text=text))

        logger.info(f"fillter llm result.text->:{result.text}")

        # TODO 固定格式
        if 'result: 1' in result.text:
            self.call_you = True
            return text
        elif 'result: 2' in result.text:
            return ''  # 记录

        elif 'result: 3' in result.text:
            self.result_3 += 1
            if self.result_3 > 5:
                self.call_you = False
                self.result_3 = 0
            return ''
        elif 'result: 4' in result.text:
            if self.call_you == True:
                return text
            else:
                return ''
        else:
            logger.error('error: {}'.format(result.text))
            return ''

    def recognized_handler(self, e):
        logger.debug('RECOGNIZED: {}'.format(e))
        logger.info(f"recognized: {e.result.text}")

        result = self.fillter(e.result.text)
        result = self.jar.chat_with(result)  # Deal
        logger.info(f"result end:{result}")

        if result:
            logger.debug(f'speaker: {result}')
            openai_speaker(result)

    def start_cb(self, evt):
        logger.debug('SESSION STARTED: {}'.format(evt))

    def recognizing_handler(self, evt):
        logger.debug('RECOGNIZING: {}'.format(evt))

    def stop_cb(self, evt):

        logger.debug('CLOSING on {}'.format(evt))
        self.speech_recognizer.stop_continuous_recognition()

    def cancel_cb(self, evt):
        pass



async def run_command(command):
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    # 等待命令执行完成
    stdout, stderr = await process.communicate()

async def main():
    command = "say he"  # 替换为你的命令
    await run_command(command)

asyncio.gather([])


# 运行异步任务
asyncio.run(main())



if __name__ == '__main__':

    a = Listener_v1()
    while True:
        print(1)
        if check_micphone_volume(seconds=0.4):
            print(2)
            asyncio.gather([main()])
            asyncio.run(main())
            a.start(30)


