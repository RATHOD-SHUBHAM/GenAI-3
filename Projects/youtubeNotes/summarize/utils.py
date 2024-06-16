'''
Youtube-Transcript-Api:
    https://pypi.org/project/youtube-transcript-api/

'''

from youtube_transcript_api import YouTubeTranscriptApi


# Todo: Extract Transcript
def extract_transcript(video_url):
    try:
        video_id = video_url.split("=")[1]  # Get the video id of the url
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        # print(transcript_text)

        transcript = ""
        for ele in transcript_text:
            transcript += " " + ele['text']
        # print(transcript)

        transcript.lstrip()
        # print(transcript)

        return transcript


    except Exception as e:
        return e
