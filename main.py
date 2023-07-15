import os
import time

root_path = "D:/Songs/"
write_path = "D:/AudioConvert"


def convert_mp4_to_mp3(path):
    try:
        audio_path = os.path.join(write_path, path.split('/')[-1])
        audio_path = audio_path.replace(".mp4", ".mp3")
        if not os.path.exists(audio_path):
            print("Converting song to " + audio_path)
            os.system('ffmpeg -i "' + path + '" "' + audio_path + '"' + ' -loglevel error')
    except Exception as e:
        print('Exception occurred for path ' + path, e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for (root, dirs, files) in os.walk(root_path):
        os.makedirs(write_path, exist_ok=True)
        for d in dirs:
            os.makedirs(os.path.join(write_path, d), exist_ok=True)
        for file in files:
            start = time.time()
            convert_mp4_to_mp3(os.path.join(root, file))
            end = time.time()
            print("Took " + str(end - start))
