import sounddevice as sd
import time as tm

duration = 5.5  # seconds

times = list()
def callback(indata, outdata, frames, time, status):
    global times
    if status:
        print(status)
    times.append(tm.time())
    outdata[:] = indata

with sd.Stream(channels=2, callback=callback):
    sd.sleep(int(duration * 1000))

mix = indata + outdata
scale = to_which(state, mix)
transform = state**scale
constructor = transform.T @ outdata
if constructor(indata) is within target_state:
    status = call_trigger(source=frames, recursive=target_state, base=constructor)
