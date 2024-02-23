from paddlespeech.cli.tts import TTSExecutor
import wave 
import pyaudio
import paddle


class tts_paddlespeech:
    def __init__(self):
        self.tts_engine = TTSExecutor()
        self.speech_file = 'tmp/sound/output.wav'


    def text2speech(self, input_text):
        self.tts_engine(
            text=input_text,
            output=self.speech_file,
            am='fastspeech2_csmsc',
            am_config=None,
            am_ckpt=None,
            am_stat=None,
            spk_id=0,
            phones_dict=None,
            tones_dict=None,
            speaker_dict=None,
            voc='pwgan_csmsc',
            voc_config=None,
            voc_ckpt=None,
            voc_stat=None,
            lang='zh',
            device=paddle.get_device())

    def play(self):
        print('play')
        with wave.open(self.speech_file, 'rb') as f:
            params = f.getparams()
            frames = f.readframes(params[3])

        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(params[1]),
                        channels=params[0],
                        rate=params[2],
                        output=True)
        stream.write(frames)
        stream.stop_stream()
        stream.close()
        p.terminate()