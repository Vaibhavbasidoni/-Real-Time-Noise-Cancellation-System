# README.md

# Real-Time Noise Cancellation System

## Objective
The goal of this project is to develop a real-time noise cancellation system that processes audio in two distinct scenarios: single speaker and multiple speakers.

## Project Structure
```
noise-cancellation-system
├── src
│   ├── main.py                # Entry point for the application
│   ├── audio_processor.py      # Handles audio input/output and filtering
│   ├── filters
│   │   ├── __init__.py        # Initializes the filters package
│   │   ├── single_speaker.py   # Isolates and enhances primary speaker audio
│   │   └── multi_speaker.py    # Preserves multiple speaker voices
│   └── utils
│       ├── __init__.py        # Initializes the utils package
│       └── audio_utils.py      # Utility functions for audio processing
├── tests
│   ├── __init__.py            # Initializes the tests package
│   └── test_audio_processor.py  # Unit tests for the AudioProcessor class
├── output                      # Directory for processed audio files
├── requirements.txt            # Lists project dependencies
└── README.md                   # Documentation for the project
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd noise-cancellation-system
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the noise cancellation system, execute the following command:
```
python src/main.py
```

## Features
- Real-time processing of audio streams.
- Supports both single speaker and multiple speaker scenarios.
- Outputs processed audio as `.wav` files.

## License
This project is licensed under the MIT License.