import queue
import sounddevice

class MicrophoneStream:
    def __init__(self, rate, blocksize, queue_live, queue, callback):
        self.queue = queue
        self.queue_live = queue_live
        self._audio_stream = sounddevice.RawInputStream(samplerate=rate, dtype='int24',callback=callback, blocksize=blocksize, channel=2)

    def __enter__(self):
        self._audio_stream.start()
        return self

    def stop(self):
        self._audio_stream.stop()

    def __exit__(self, type, value, traceback):
        self._audio_stream.stop()
        self._audio_stream.close()
