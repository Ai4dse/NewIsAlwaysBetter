import whisper
import os, glob

model = whisper.load_model("medium")

def transcribe(untranscribed_recording_path):

        if os.path.exists(untranscribed_recording_path):
            audio = whisper.load_audio(untranscribed_recording_path)
            audio = whisper.pad_or_trim(audio)
            
            mel = whisper.log_mel_spectrogram(audio).to(model.device)

            options = whisper.DecodingOptions( fp16=False)
            result = whisper.decode(model, mel, options)
    
            if result.no_speech_prob < 0.7:
                print("Transcription:")
                print(result.text)

                # append text to transcript file
                with open('transcript.txt', 'a') as f:
                    f.write(result.text)
        return True