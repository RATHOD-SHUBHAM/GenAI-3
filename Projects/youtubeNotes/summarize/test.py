from summarize.utils import extract_transcript
from summarize.core import generate_notes
from summarize.download_notes import write_to_file


def main(video_url):
    transcript = extract_transcript(video_url=video_url)

    summary = generate_notes(transcript=transcript)

    print(summary)

    write_to_file(transcript=summary)




if __name__ == '__main__':
    video_url = 'https://www.youtube.com/watch?v=spamOhG7BOA&ab_channel=MLOps.community'
    # 'https://www.youtube.com/watch?v=k2P_pHQDlp0&ab_channel=KrishNaik'
    # 'https://www.youtube.com/watch?v=spamOhG7BOA&ab_channel=MLOps.community'
    # 'https://www.youtube.com/watch?v=HFfXvfFe9F8&t=14s&ab_channel=KrishNaik

    main(video_url=video_url)
