import cv2
import numpy as np
import base64
from typing import Optional
from openai import OpenAI
from PIL import Image
import io
import os
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

class CameraAnalyzer:
    def __init__(self, camera_id: int = 0, analysis_interval: float = 2.0):
        """Initialize the camera analyzer.
        
        Args:
            camera_id (int): The ID of the camera to use (default is 0 for the default camera)
            analysis_interval (float): Minimum time (in seconds) between frame analyses
        """
        self.camera_id = camera_id
        self.cap = None
        self.is_running = False
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.analysis_interval = analysis_interval
        self.last_analysis_time = 0
        
    def frame_to_base64(self, frame: np.ndarray) -> str:
        """Convert a frame to base64 string.
        
        Args:
            frame (np.ndarray): The frame to convert
            
        Returns:
            str: Base64 encoded image string
        """
        # Convert BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Convert to PIL Image
        pil_image = Image.fromarray(rgb_frame)
        
        # Convert to base64
        buffered = io.BytesIO()
        pil_image.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode('utf-8')
        
    def analyze_frame(self, frame: np.ndarray) -> str:
        """Analyze a single frame using OpenAI's Vision API.
        
        Args:
            frame (np.ndarray): The frame to analyze
            
        Returns:
            str: Description of what's happening in the frame
        """
        current_time = time.time()
        
        # Check if enough time has passed since the last analysis
        if current_time - self.last_analysis_time < self.analysis_interval:
            return None
            
        self.last_analysis_time = current_time
        
        try:
            # Convert frame to base64
            base64_image = self.frame_to_base64(frame)
            
            # Create the API request
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": "Describe what is happening in this camera feed. Focus on the main activities and objects visible in the scene. Be concise."
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}"
                                }
                            }
                        ]
                    }
                ],
                max_tokens=100
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            return f"Error analyzing frame: {str(e)}"
    
    def start(self):
        """Start the camera feed and analysis."""
        if not os.getenv('OPENAI_API_KEY'):
            raise RuntimeError("OpenAI API key not found. Please set it in the .env file.")
            
        self.cap = cv2.VideoCapture(self.camera_id)
        if not self.cap.isOpened():
            raise RuntimeError("Failed to open camera")
            
        self.is_running = True
        print("Camera feed started. Press 'q' to quit.")
        
        try:
            while self.is_running:
                ret, frame = self.cap.read()
                if not ret:
                    print("Failed to grab frame")
                    break
                
                # Display the frame
                cv2.imshow('Camera Feed', frame)
                
                # Analyze the frame
                analysis = self.analyze_frame(frame)
                if analysis:
                    print(f"\rAnalysis: {analysis}", flush=True)
                
                # Check for quit command
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                    
        except KeyboardInterrupt:
            print("\nStopping camera feed...")
        finally:
            self.stop()
    
    def stop(self):
        """Stop the camera feed and release resources."""
        self.is_running = False
        if self.cap is not None:
            self.cap.release()
        cv2.destroyAllWindows()

def main():
    try:
        analyzer = CameraAnalyzer(analysis_interval=2.0)  # Analyze every 2 seconds
        analyzer.start()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 