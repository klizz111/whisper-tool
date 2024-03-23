import subprocess
import os

folder_path = 'D:\\Downloads\\input'
out_dir = 'D:\\Downloads\\output'
format = 'txt'
language = 'English'
modeldir = 'D:\\whisper\\'
model = 'small'

for root, dirs, files in os.walk(folder_path):
        dirs.clear()
        for file in files:
            if file.endswith('.mp3'):
                file_path = os.path.join(root, file)
                command = [
                    "whisper.exe",
                    file_path,
                    "--model_dir",
                    modeldir,
                    "--model",
                    model,
                    "--output_dir",
                    out_dir,
                    "--verbose",
                    "False",
                    "--device",
                    "cuda",
                    "--language",
                    language,
                    "--output_format",
                    format
                ]           

                print(" ".join(command))
                subprocess.run(command)
                