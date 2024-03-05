from google.cloud import speech_v1p1beta1 as speech
import os

def transcribe_audio(audio_file_path, language_code='en-US'):
    client = speech.SpeechClient()

    # Configure audio input
    audio = speech.RecognitionAudio(uri=audio_file_path)

    # Configure speech recognition settings
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code=language_code,
    )

    # Perform the transcription
    response = client.recognize(config=config, audio=audio)

    # Extract and return transcription results
    transcriptions = []
    for result in response.results:
        transcriptions.append(result.alternatives[0].transcript)
    
    return transcriptions

if __name__ == "__main__":
    # Replace 'path/to/audio/file.wav' with the path to your audio file
    audio_file_path = 'path/to/audio/file.wav'

    if not os.path.exists(audio_file_path):
        print("Audio file not found.")
    else:
        transcriptions = transcribe_audio(audio_file_path)
        print("Transcription:")
        for transcription in transcriptions:
            print(transcription)
