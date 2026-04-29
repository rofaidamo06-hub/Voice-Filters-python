# Voice Filter Application (Python & DSP)

## Project Overview
Voice Filter is a Python-based desktop application designed for **Digital Signal Processing (DSP)** of human speech. The project focuses on applying mathematical transformations to audio signals, allowing for noise reduction, frequency filtering, and creative voice modulation through an interactive GUI.

## Technical Core & Features
*   **Low-Pass FIR Filtering**: Implements a Finite Impulse Response (FIR) filter to isolate specific frequency bands, crucial for clarifying voice signals.
*   **FFT Noise Reduction**: Uses **Fast Fourier Transform (FFT)** to analyze the audio spectrum and manually zero out high-frequency noise components.
*   **Voice Modulation Effects**: Developed algorithms for "Monster" and "Chipmunk" effects by scaling sample rates and manipulating pitch.
*   **Signal Visualization**: Integrated real-time plotting of waveforms (Original vs. Filtered) using Matplotlib for comparative analysis.
*   **User Interface**: A customized **Tkinter** GUI for seamless audio loading and filter application.

## Mathematical & Engineering Foundation
*   **Spectral Analysis**: Applying `rfft` and `irfft` for frequency-domain signal manipulation.
*   **Filter Design**: Using `firwin` to create precise windowed-sinc filters.
*   **Signal Integrity**: Handling sample rates and bit-depth (int16) to maintain audio quality during processing.

## Technical Stack
*   **Language**: Python 3.x
*   **Libraries**: NumPy, SciPy (Signal/FFT), Matplotlib, Tkinter.

