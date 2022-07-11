"""Settings for audio reactive LED strip"""
from __future__ import print_function
from __future__ import division
import os


LED_PIN = 18 # GPIO pin connected to the LED strip pixels (must support PWM) GPIO 18/ Pin 12 is default
LED_FREQ_HZ = 800000 # LED signal frequency in Hz (usually 800kHz)
LED_DMA = 5 # DMA channel used for generating PWM signal (try 5)
BRIGHTNESS = 255 # Max brightness of LED strip between 0 and 255
LED_INVERT = False # Set True if using an inverting logic level converter
SOFTWARE_GAMMA_CORRECTION = True # Set to True because Raspberry Pi doesn't use hardware dithering
USE_GUI = False # Whether or not to display a PyQtGraph GUI plot of visualization
DISPLAY_FPS = False # Whether to display the FPS when running (can reduce performance)
N_PIXELS = 300 # Number of pixels in the LED strip
MIC_RATE = 48000 # Sampling frequency of the microphone in Hz
FPS = 50 # target update rate.
_max_led_FPS = int(((N_PIXELS * 30e-6) + 50e-6)**-1.0)
assert FPS <= _max_led_FPS, 'FPS must be <= {}'.format(_max_led_FPS)

"""Location of the gamma correction table"""
GAMMA_TABLE_PATH = os.path.join(os.path.dirname(__file__), 'gamma_table.npy')

"""Frequencies below this value will be removed during audio processing"""
MIN_FREQUENCY = 200

"""Frequencies above this value will be removed during audio processing"""
MAX_FREQUENCY = 12000

"""Number of frequency bins to use when transforming audio to frequency domain

Fast Fourier transforms are used to transform time-domain audio data to the
frequency domain. The frequencies present in the audio signal are assigned
to their respective frequency bins. This value indicates the number of
frequency bins to use.

A small number of bins reduces the frequency resolution of the visualization
but improves amplitude resolution. The opposite is true when using a large
number of bins. More bins is not always better!

There is no point using more bins than there are pixels on the LED strip.
"""
N_FFT_BINS = 24

"""Number of past audio frames to include in the rolling window"""
N_ROLLING_HISTORY = 2

"""No music visualization displayed if recorded audio volume below threshold"""
MIN_VOLUME_THRESHOLD = 1e-7

