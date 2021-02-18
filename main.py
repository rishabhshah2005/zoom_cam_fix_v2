from pymsgbox import *
import time
import pyautogui

delay_time = 15  # In Seconds
pop_up_time = 5  # In Seconds


def on_or_off():
    pyautogui.move(1, 1)
    pyautogui.move(-1, -1)
    video_on = pyautogui.locateCenterOnScreen('cam_images/video_on_zoom.png', confidence=0.95)
    if video_on:
        return list(video_on)
    else:
        return None


def pop_up():
    return confirm(text='Your Video is ON!! \n Do you want to keep it ON??', title='Zoom Video Alert',
                   buttons=['Yes', 'No'], timeout=pop_up_time*1000)


print('Starting bot....')

confirm(text='?', title='Zoom Video Alert', buttons=['Yes', 'No'], timeout=500)

while True:
    time.sleep(delay_time)
    condition = on_or_off()
    if condition:
        pop_ans = pop_up()
        if pop_ans == 'No':
            pyautogui.move(5, 0)
            time.sleep(0.1)
            pyautogui.click(condition[0], condition[1])
        elif pop_ans == 'Yes':
            pass
        elif pop_ans == 'Timeout':
            pyautogui.move(5, 0)
            time.sleep(0.1)
            pyautogui.click(condition[0], condition[1])
    else:
        pass



#  Made by Rishabh Shah














