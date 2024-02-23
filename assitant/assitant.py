from conversation.conversation_manager import conversation_manager
from configparser import ConfigParser
from asr.asr_paddle import asr_paddlespeech
from tts.tts_paddle import tts_paddlespeech
from recorder.recorder import audio_recorder



class assitant:
    def __init__(self):
        config = ConfigParser()
        config.read('config/config.ini')
        self.conversation_manager = conversation_manager(config)
        self.asr_engine = asr_paddlespeech(config)
        self.tts_engine = tts_paddlespeech()
        self.recorder = audio_recorder()

    def begin_recording(self):
        self.recorder.start()

    def end_recording(self):
        self.recorder.stop()

    def processing(self):
        text = self.asr_engine.speech2text()
        print(f'asr result {text}')
        text_response = self.conversation_manager.deal_with_input(text)
        print(f'llm response {text_response}')
        self.tts_engine.text2speech(text_response)

    def play(self):
        self.tts_engine.play()
 