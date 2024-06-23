# %%aigen 使用fire包将代码包装成终端可执行

import fire
from pathlib import Path
import openai

def generate_speech(text):
    response = openai.audio.speech.create(
        model="tts-1",
        voice="onyx",
        input=text
    )
    response.stream_to_file('/Users/zhaoxuefeng/Documents/Project/applescript/快捷指令/speech.mp3')

if __name__ == '__main__':
    fire.Fire(generate_speech)
