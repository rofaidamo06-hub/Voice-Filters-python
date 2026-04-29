
import numpy as np
import scipy.io.wavfile as wavfile


from matplotlib import pyplot as plt
from scipy.signal import kaiserord, lfilter, firwin
from scipy.fft import rfft, rfftfreq, irfft


from tkinter import *

input_file = "321.wav"
output_fname = "filtered-voice.wav"
INPUT_FILE = "321.wav"
SAMPLES_RATE = None
AUDIO_DATA = None



def read_my_wav():
    try:
        sample_rate, data = wavfile.read(input_file)
    except FileNotFoundError:
        print("ERROR! file not found! please try again!")
        return None

    if data.ndim > 1:
        data = data[:, 0]

    duration = len(data) / sample_rate

    print(f"Sample Rate: {sample_rate}")

    print(f"Duration: {duration:.2f} seconds")

    wavfile.write("321_test.wav", sample_rate, data)

    print("Saved Successfully")

    return sample_rate, data


def FIR_filter(sample_rate, data):
    nyq_rate = sample_rate / 2.0

    cutoff_hz = 3000.0
    taps = firwin(101, cutoff_hz/nyq_rate)
    filtered_data = lfilter(taps, 1.0, data)

    wavfile.write(output_fname, sample_rate, np.int16(filtered_data))

    print(f"Saved Successfully as:{output_fname}")

    print("Original Voice:")

    print("Filtered Voice:")



def FFT_noise_reduction(fs, data):
    output_file = "noise_reduced_fft.wav"

    print(f"Sample Rate: {fs} Hz")
    print(f"Number of Samples: {len(data)}")

    n = len(data)
    yf = rfft(data)
    xf = rfftfreq(n, 1 / fs)

    cutoff_freq = 4000,
    idx = np.where(xf > cutoff_freq)
    yf[idx] = 0
    clean_signal = irfft(yf)

    wavfile.write(output_file, fs, clean_signal.astype(np.int16))
    print(f"Saved Successfully as: {output_file}")

    print("Noise Reduced (FFT Method):")



def pitch_shift_and_time_stretch(data, fs, factor):
    new_fs = int(fs * factor)
    return new_fs, data


def save_wav(path, fs, data):
    wavfile.write(path, fs, np.int16(data))


def effects():
    fs, data = read_my_wav()

    fs_chip, chip_data = pitch_shift_and_time_stretch(data, fs, 1.5)
    save_wav("chipmunk.wav", fs_chip, chip_data)

    fs_mon, mon_data = pitch_shift_and_time_stretch(data, fs, 0.7)
    save_wav("monster.wav", fs_mon, mon_data)

    print("monster voice:")


    print("Chipmunk voice:")





original_fname = "321.wav"
modified_fname = "monster.wav"

def visualize_comparison():
    print("Loading files for visualization...")
    try:
        fs1, data1 = wavfile.read(original_fname)
    except FileNotFoundError:
        print(f"ERROR! file {original_fname} not found!")
        return

    if data1.ndim > 1:
        data1 = data1[:, 0]

    try:
        fs2, data2 = wavfile.read(modified_fname)
    except FileNotFoundError:
        print(f"ERROR! file {modified_fname} not found!")
        return

    if data2.ndim > 1:
        data2 = data2[:, 0]

    print(f"Plotting: {original_fname} vs {modified_fname}")

    time1 = np.arange(len(data1)) / fs1
    time2 = np.arange(len(data2)) / fs2

    plt.figure(figsize=(10, 8))

    plt.subplot(2, 1, 1)
    plt.plot(time1, data1, color='blue')
    plt.title(f"Original Voice: {original_fname}")
    plt.ylabel("Amplitude")
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.plot(time2, data2, color='red')
    plt.title(f"Modified Voice: {modified_fname}")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

    print("Graph Displayed Successfully")

visualize_comparison()
def apply_lowpass():
    fs,data = read_my_wav()
    FIR_filter(fs,data)
def apply_fft_denoise():
    fs, data = read_my_wav()
    FFT_noise_reduction(fs, data)
def apply_monster():
    fs,data = read_my_wav()
    fs_mon,mon_data = pitch_shift_and_time_stretch(data,fs,0.7)
    save_wav("monster.wav",fs_mon,mon_data)
    print("Monster voice saved")




window = Tk()
window.title("Voice Filter")
window.geometry("400x550")
icon = PhotoImage(file='img.png')
window.iconphoto(True,icon)
bg_image = PhotoImage(file='Screenshot_1.png')
bg_label = Label(window,image=bg_image).place(x=0,y=0,relwidth=1,relheight=1)
def load_audio():
    global AUDIO_DATA,SAMPLES_RATE
    fs,data = read_my_wav()
    if fs is None:
        return

    SAMPLES_RATE = fs
    AUDIO_DATA=data
    print("Audio loaded")
l1= Label(window, text="Audio Filter & Effects", font=("Arial", 14, "bold")).pack(pady=10)
btn1 =Button(window, text="1. Load WAV File",command=load_audio, bg="#ddd", width=30).pack(pady=5)
l2=Label(window, text="--- Filters ---").pack(pady=5)
btn2=Button(window, text="2. Apply Low Pass Filter",command=apply_lowpass, width=30).pack(pady=2)
l3=Label(window, text="--- Effects ---").pack(pady=5)
btn3=Button(window, text="3. Monster Voice",command=apply_monster, width=30).pack(pady=2)
l4=Label(window, text="--- FFT Denoise ---").pack(pady=5)
btn4=Button(window, text="4. Remove Noise (FFT)",command=apply_fft_denoise, width=30).pack(pady=2)
l5 =Label(window, text="--- Visuals ---").pack(pady=5)
btn5=Button(window, text="5. Plot Signals", bg="lightblue",command=visualize_comparison, width=30).pack(pady=10)

window.mainloop()