# Live Camera Feed Analyzer

This application captures live camera feed and analyzes it using a Vision Language Model (VLM). Currently, it has a placeholder for the VLM integration that can be replaced with your preferred VLM API.

## Requirements

- Python 3.8 or higher
- OpenCV
- NumPy

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application from the terminal:
```bash
python camera_analyzer.py
```

- The application will start capturing video from your default camera
- Press 'q' to quit the application
- The analysis will be printed to the terminal in real-time

## Customization

To integrate your preferred VLM:
1. Open `camera_analyzer.py`
2. Locate the `analyze_frame` method in the `CameraAnalyzer` class
3. Replace the placeholder return statement with your VLM API call
4. Modify the prompt as needed for your use case

## Note

The current version includes a placeholder for the VLM integration. You'll need to add your preferred VLM API and configure it according to your needs. 