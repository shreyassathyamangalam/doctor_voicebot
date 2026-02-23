# Doctor Voicebot

## Overview
The **Doctor Voicebot** project is designed to help provide medical advice through an interactive voice-based interface. Built using modern technologies like FastAPI, Gradio, and Eleven Labs, the voicebot aims to make healthcare more accessible by leveraging voice recognition and natural language processing.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [Dependencies](#dependencies)
- [License](#license)
- [Contributing](#contributing)

## Features
- Interactive voice conversations with patients.
- Support for voice synthesis and recognition.
- Ability to play pre-recorded audio files demonstrating bot responses.
- Easy integration with Gradio for a web-based interface.

## Getting Started

### Prerequisites
- Python >= 3.12
- Docker (optional, for containerized deployment)
- Basic knowledge of voice recognition and natural language processing

### Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/doctor_voicebot.git
   cd doctor_voicebot
   ```

2. **Install dependencies**
   You can either create a virtual environment or install the required packages globally.
   ```bash
   pip install -r requirements.txt
   ```

3. **Optional: Docker Setup**
   To run the application in a Docker container, you can build the Docker image.
   ```bash
   docker build -t doctor_voicebot .
   ```

## Usage
To start the voicebot, use the following command:
```bash
python gradio_app.py
```
This will launch a web interface for the voicebot, allowing users to interact with it via their web browsers.

## File Descriptions
- `.gitignore`: Specifies files and directories that should be ignored by Git.
- `.python-version`: Python version for the project.
- `Dockerfile`: Docker configuration file to containerize the application.
- `README.md`: Documentation for the project.
- `acne.jpg` & `skin_rash.jpg`: Sample images related to medical conditions.
- `brain_of_the_doctor.py`: Logic defining the bot's medical advice framework.
- `elevenlabs_testing.mp3`, `gtts_testing.mp3`, and `final.mp3`: Audio files for testing voice synthesis.
- `gradio_app.py`: The main application file that runs the Gradio interface.
- `patient_voice_test.mp3`: Sample input audio for testing patient responses.
- `pyproject.toml`: Project metadata and dependencies.
- `requirements.txt`: List of required Python packages for the project.
- `uv.lock`: Lock file for managing dependencies.

## Dependencies
The project requires the following Python libraries:
- `elevenlabs`
- `gradio`
- `groq`
- `gtts`
- `pyaudio`
- `pydub`
- `python-dotenv`
- `speechrecognition`

The dependencies listed above are automatically handled through `requirements.txt` and `pyproject.toml`.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! If you have suggestions for improvements or have encountered any issues, please create an issue or submit a pull request.

---

For further information, please check the documentation or open an issue in the repository. Happy coding!