from sys import argv
from time import sleep
from platform import system
import webbrowser
import pyautogui
import subprocess
import signal
import os

def main():
    lessons = []
    OS = system().lower()
    count = 1
    with open(argv[1], "r") as file:
        for line in file:
            lessons.append({
                "url" : line,
                "length" : int(input(f"Lesson #{count} length (mins, -1 to skip) ? "))
            })
            count += 1

    shutdown = input("Do you want to shutdown the computer after recording (y/N) ? ").lower()
    sleep(int(input("How much do you want to wait before starting to record (mins) ? ")) * 60)

    print("Opening programs")

    # opening obs without terminal output
    obs = subprocess.Popen(["obs"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # waiting for obs to open
    sleep(3)
    # opening web browser
    webbrowser.open_new("google.com")
    # opening teams without terminal output
    teams = subprocess.Popen(["teams"], start_new_session=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # waiting for teams to open
    sleep(30)

    count = 1
    for lesson in lessons:
        if lesson["length"] == -1:
            continue

        # open link
        webbrowser.open_new_tab(lesson["url"])

        # waiting for the meeting to appear
        sleep(10)

        # join meeting
        join = pyautogui.locateOnScreen(os.path.join('img', 'join_call.png'))
        if join is None:
            join = pyautogui.locateOnScreen(os.path.join('img', 'join_call_active.png'))

        if join is None:
            pyautogui.press('enter')
        else:
            pyautogui.click(join)

        # waiting to join the meeting
        sleep(3)

        # mute mic
        mic = pyautogui.locateOnScreen(os.path.join('img', 'mic.png'))
        if mic is not None:
            pyautogui.click(mic)
            pyautogui.moveTo(500, 500, 2, pyautogui.easeInQuad)

        # disable video
        video = pyautogui.locateOnScreen(os.path.join('img', 'video.png'))
        if video is not None:
            pyautogui.click(video)
            pyautogui.moveTo(500, 500, 2, pyautogui.easeInQuad)

        print(f"Started recording #{count}!")
        # start recording
        pyautogui.hotkey('ctrl', 'alt', 'shift', 'r', interval=0.25)

        # wait for the lesson to end
        sleep(lesson["length"] * 60)

        # stop recording
        pyautogui.hotkey('ctrl', 'alt', 'shift', 'r', interval=0.25)
        pyautogui.moveTo(500, 500, 2, pyautogui.easeInQuad)
        close = pyautogui.locateOnScreen(os.path.join('img', 'close_call.png'))
        if close is not None:
            pyautogui.click(close)
        else:
            teamspg = os.getpgid(teams.pid)
            os.killpg(teamspg, signal.SIGINT)
            sleep(2)
            teams = subprocess.Popen(["teams"], start_new_session=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            sleep(30)
        print(f"Stopped recording #{count}!")

        # make sure the video is saved
        sleep(60)

        count += 1

    print("Closing programs")
    # close obs
    obs.kill()
    # close teams
    teamspg = os.getpgid(teams.pid)
    os.killpg(teamspg, signal.SIGINT)

    # waiting for programs to be closing
    sleep(5)

    if shutdown == "y" or shutdown == "yes":
        if OS == "linux":
            subprocess.run(["shutdown"])
        elif OS == "windows":
            subprocess.run(["shutdown", "/s"])
        else:
            print("Shutdown within this OS is not supported!")


if __name__ == "__main__":
    if len(argv) < 2:
        print("Error! Please write the file name along the program!")
    else:
        main()
