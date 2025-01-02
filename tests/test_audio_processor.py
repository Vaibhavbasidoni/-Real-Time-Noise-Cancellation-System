import unittest
from unittest.mock import Mock
from src.audio_processor import AudioProcessor
from src.filters.single_speaker import SingleSpeakerFilter
from src.filters.multi_speaker import MultiSpeakerFilter

class TestAudioProcessor(unittest.TestCase):
    def setUp(self):
        self.audio_processor = AudioProcessor()
        self.audio_processor.output_stream = Mock()

    def test_single_speaker_filter(self):
        self.audio_processor.set_single_speaker_filter(SingleSpeakerFilter())
        # Add test cases for single speaker filter
        audio_chunk = b'\x00\x01\x02\x03'  # Example audio chunk
        processed_audio = self.audio_processor.process_audio(audio_chunk, scenario='single')
        self.assertIsNotNone(processed_audio)

    def test_multi_speaker_filter(self):
        self.audio_processor.set_multi_speaker_filter(MultiSpeakerFilter())
        # Add test cases for multi speaker filter
        audio_chunk = b'\x00\x01\x02\x03'  # Example audio chunk
        processed_audio = self.audio_processor.process_audio(audio_chunk, scenario='multi')
        self.assertIsNotNone(processed_audio)

if __name__ == '__main__':
    unittest.main()