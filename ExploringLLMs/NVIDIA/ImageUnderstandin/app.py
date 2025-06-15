from imageAnalyst import ImageAnalyst
from videoAnalyst import VideoAnalyst
from conversationalAgent import ConversationalAgent
import os

# os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/Cellar/ffmpeg/5.1/bin/ffmpeg"


def startConversation(summary):
    conversation_obj = ConversationalAgent()

    while True:
        user_query = input("ask: ")

        if user_query == 'q' or user_query == 'quit' or user_query == 'end':
            print("Stopping")
            break
        elif user_query == " ":
            print('Ask something !!!!!')
            continue
        else:
            response = conversation_obj.conversation(vision_response=summary, query=user_query)
            print(response)


def summarize(file_path, file_extension):
    # Determine if the file is an image or a video based on its extension
    image_extensions = ['.jpg', '.jpeg', '.png']
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv']

    if file_extension in image_extensions:
        # Create an object for image analyst
        imgAt_obj = ImageAnalyst()

        # Pass the image to the pipeline function
        image_analysis_result = imgAt_obj.pipe(file_path)

        print(image_analysis_result)

        return image_analysis_result

    elif file_extension in video_extensions:
        vdo_obj = VideoAnalyst(VIDEO_PATH = file_path)

        video_analysis_summary = vdo_obj.analyzeVideo()

        print(video_analysis_summary)

        return video_analysis_summary
    else:
        print("The file type is not supported. Please provide an image or video file.")


def main():
    # Todo: Step 1: Request user for a input
    file_path = '/Users/shubhamrathod/PycharmProjects/ThirdEye/input/vid_5.mp4'

    if not os.path.exists(file_path):
        print("The specified file does not exist.")
        return

    file_extension = os.path.splitext(file_path)[1].lower()

    # Todo: Preprocess the file
    summary = summarize(file_path, file_extension)

    # Todo: Start Conversation
    startConversation(summary=summary)


if __name__ == '__main__':
    main()
