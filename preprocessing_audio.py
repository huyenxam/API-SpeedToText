from pydub import AudioSegment
import os

def preprocessing(folder, path):
    audios = set()
    # CONVERT MP3 -> WAV
    type_file = path.split(".")[-1]
    sound = AudioSegment.from_file(path, type_file)

    audio_path = os.path.join(folder, "new_audio1.wav")
    sound.export(audio_path, format="wav")
    audios.add(audio_path)

    # SPLIT AUDIO
    time_audio = int(sound.duration_seconds / 30) + 1
    for i in range(time_audio):
        t1 = i * 30 * 1000
        t2 = (i+1) * 30 * 1000
        newAudio = sound[t1:t2]

        newAudio.set_channels(1)   # single channel --> mono channel
        newAudio = newAudio.set_frame_rate(16000)    # convert frequency : mọi freq --> 16000kHz
        # print(newAudio.frame_rate)
        # print(newAudio.split_to_mono())

        audio_path = os.path.join(folder, 'new_audio' + str(i) + '.wav')
        newAudio.export(audio_path, format="wav") 
        audios.add(audio_path)

    return audios


