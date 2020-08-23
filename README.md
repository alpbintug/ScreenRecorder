# Screen Recorder
A screen recorder that I created to record my screen, because why pay for some random applications when you create one, right?

### TO-DO

- IMPROVE PERFORMANCE (URGENT!)
    ```
    Right now program cannot handle high frame rates gets 30ish frames with my i7 8750H CPU
    How can I solve this?
    
    PROBLEMS:

    ---If I store screenshots to speed up recording process, I run out of memory quickly
    ---Taking screenshots is too slow
    ---Processing and saving screenshots is just a bit slow

    IDEAS:

    ---Reduce resolution, then upscale it in post processing?
    ---Reduce frame rate, then upscale it in post processing?
    ---Use Windows API? WHO CARES ABOUT PORTABILITY
    ---Maybe if I re-run the code enough times framerates will increase
    ---JUST GO WRITE THIS IN ASSEMBLY ALREADY
    ---Wait this makes sense
    ---Oh boy...
    ```
- Give user resolution options
- Record computer audio synched with FPS and merge this with video file
- Create a GUI element to help user name the recorded video and specify save location
- Add a timer to show user recorded video length while recording

### TO-Done
- Create a GUI to help user start and stop recording (DONE)
- Give user FPS options (DONE)


## Prerequisites

Codes are written in ***Python 3***, on to not encounter problems, use this version of Python to run the codes.
Required libraries are:
- OpenCV: ``` pip install opencv-python ```
- numpy: ``` pip install numpy ```
- pyautogui: ``` pip install PyAutoGUI ```
- tkinter: ``` pip install tk ```
- threading

## Installation and Running


- ***Clone*** the repository
- ***Run*** the ***source.py*** via Visual Studio
- ***Select*** the FPS rate you want to record in
- ***Press*** the "Start recording" button, GUI will automatically minimize
- ***Maximize*** the GUI when you need to stop recording, your captured screen will be saved as "output.avi" with the same location as your code.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Authors
Alp Bintuğ Uzun

## Contact
- [@alpbintug](https://github.com/alpbintug) on GitHub
- [Alp Bintug](www.linkedin.com/in/alpbintug) on LinkedIn
- alp.bintug@gmail.com

## License
[GNU General Public License 3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)

