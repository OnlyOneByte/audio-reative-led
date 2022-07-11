import config
import dsp
import led
import signal
import sys
import time
import numpy as np
import pyaudio
import config

from visualization import visualize_spectrum, visualize_scroll, visualize_energy, microphone_update
from led import color_wipe

def runGUI():
    # TODO: rewrite using matplotlib
    print("HI, GUI setup")

endRun = False

if __name__ == '__main__':

    if config.USE_GUI:
        runGUI()

    # Visualization effect to display on the LED strip -> function
    visualization_effect = ()
    if sys.argv[1] == "spectrum":
            visualization_effect = visualize_spectrum
    elif sys.argv[1] == "energy":
            visualization_effect = visualize_energy
    elif sys.argv[1] == "scroll":
            visualization_effect = visualize_scroll
    else:
            visualization_effect = visualize_spectrum

        
    # Initialize LEDs
    led.update()



    # Start listening to live audio stream
    p = pyaudio.PyAudio()
    frames_per_buffer = int(config.MIC_RATE / config.FPS)
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=config.MIC_RATE,
                    input=True,
                    frames_per_buffer=frames_per_buffer)
    overflows = 0
    prev_ovf_time = time.time()


    # handles exit
    def signal_handler(signal, frame):
        global endRun
        print("Exiting...")
        endRun = False
        
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        try:
            y = np.fromstring(stream.read(frames_per_buffer, exception_on_overflow=False), dtype=np.int16).astype(np.float32)
            stream.read(stream.get_read_available(), exception_on_overflow=False)
            microphone_update(y, visualization_effect) # update LEDS based on microphone
        except IOError:
            overflows += 1
            if time.time() > prev_ovf_time + 1:
                prev_ovf_time = time.time()
                print('Audio buffer has overflowed {} times'.format(overflows))

        if endRun:
            break
    
    # cleanup stuff
    stream.stop_stream()
    stream.close()
    p.terminate()
    led.color_wipe(0)

