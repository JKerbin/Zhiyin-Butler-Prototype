import os
import wave
import pyaudio
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
    
class audio_recorder:
    def __init__(self):
        p = pyaudio.PyAudio()
        self.thread_pool =  ThreadPoolExecutor(max_workers=1)
        self.work_end = False
        self.current_task = None

    def start(self):
        self.work_end = False
        print('submit')
        self.current_task = self.thread_pool.submit(self.work)

    def work(self):
        try:
            file_path = 'tmp\sound\\test.wav'
            print('hello')
            sample_rate=16000
            bit_depth=16
            channels=1

            p = pyaudio.PyAudio()
            format = p.get_format_from_width(bit_depth // 8)
            stream = p.open(format=format,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=1024)

            print("开始录音...")

            frames = []
            while True and not self.work_end:
                data = stream.read(1024)
                frames.append(data)

            print("录音结束.")

            # 关闭流和PyAudio
            stream.stop_stream()
            stream.close()
            p.terminate()

            # 保存录音文件
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            wf = wave.open(file_path, 'wb')
            wf.setnchannels(channels)
            wf.setsampwidth(bit_depth // 8)
            wf.setframerate(sample_rate)
            wf.writeframes(b''.join(frames))
            wf.close()
        except BaseException as e:
            print(e)

    def stop(self):
        self.work_end = True
        concurrent.futures.wait([self.current_task])

