import os

os.system("cp main.txt remaining.txt")
with open("main.txt", "r") as file:
    for line in file:
        split = line.split(" ")
        if split.__len__() != 2:
            print("Not enough arguments!")
            continue
        name = split[0]
        link = split[1]
        print(f"Started {name}")
        os.system(f"ffmpeg -i \"{link}\" -bsf:a aac_adtstoasc -vcodec copy -c copy -crf 50 {name}.mp4 > /dev/null 2>&1")
        if "audio" in name:
            original_name = name.replace("-audio", "")
            os.system(f"ffmpeg -i {original_name}.mp4 -i {name}.mp4 -c copy -map 0:0 -map 1:1 -shortest out.mp4 > /dev/null 2>&1")
            os.system(f"mv out.mp4 {original_name}.mp4 -f")
            os.system(f"rm {name}.mp4")
        print(f"Finished {name}")
        os.system("sed -i '1,1d' remaining.txt")

os.system("mv -f remaining.txt main.txt")
