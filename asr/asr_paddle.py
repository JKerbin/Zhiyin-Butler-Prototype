from paddlespeech.cli.asr import ASRExecutor
import paddle

class asr_paddlespeech:
    def __init__(self, config):
        self.asr_executor = ASRExecutor()
    def speech2text(self):
        return self.asr_executor(model='conformer_talcs',
        lang='zh_en',
        sample_rate=16000,
        config=None, 
        ckpt_path=None,
        audio_file='./tmp/sound/test.wav',
        codeswitch=True,
        force_yes=False,
        device=paddle.get_device())