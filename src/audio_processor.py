import pyaudio
import wave
import numpy as np
from src.filters.single_speaker import SingleSpeakerFilter
from src.filters.multi_speaker import MultiSpeakerFilter

class AudioProcessor:
    def __init__(self):
        # Initialize audio input and output streams
        self.input_stream = None
        self.output_stream = None
        self.single_speaker_filter = SingleSpeakerFilter()
        self.multi_speaker_filter = MultiSpeakerFilter()
        self.p = pyaudio.PyAudio()

    def start_stream(self):
        # Start the audio input and output streams
        self.input_stream = self.p.open(format=pyaudio.paInt16,
                                        channels=1,
                                        rate=44100,
                                        input=True,
                                        frames_per_buffer=1024)
        self.output_stream = self.p.open(format=pyaudio.paInt16,
                                         channels=1,
                                         rate=44100,
                                         output=True)

    def stop_stream(self):
        # Stop the audio input and output streams
        self.input_stream.stop_stream()
        self.input_stream.close()
        self.output_stream.stop_stream()
        self.output_stream.close()
        self.p.terminate()

    def process_audio(self, audio_chunk, scenario='single'):
        # Process the incoming audio chunk
        if scenario == 'single':
            processed_audio = self.single_speaker_filter.apply_filter(audio_chunk)
        else:
            processed_audio = self.multi_speaker_filter.apply_filter(audio_chunk)
        self.output_stream.write(processed_audio)
        return processed_audio

    def save_processed_audio(self, processed_audio, filename):
        # Save the processed audio to a .wav file
        wf = wave.open(filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(self.p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(processed_audio)
        wf.close()

    def set_single_speaker_filter(self, filter):
        # Set the filter for single speaker scenario
        self.single_speaker_filter = filter

    def set_multi_speaker_filter(self, filter):
        # Set the filter for multiple speakers scenario
        self.multi_speaker_filter = filter