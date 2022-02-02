README BodyTracking

The program was created by Jan Kaminski (https://github.com/jkaminski677) as part of a PBL project in college. The purpose of the program is to analyze human movements during speeches in front of the camera. The program examines and records the movement of specific parts of the human body. Currently, only the hands, the center of the shoulders, the center of the hips, and the center of the body (around the heart) are set. If you want to change the body parts you have to do it from the source code.

To install the program, unzip the parent folder from the .zip format and open the executable file in .exe format.

If after running the program there is a problem with the vcruntime140.dll library then you should follow the steps below.
Unzip the vcruntime140__.zip file (either the 32-bit or 64-bit version depending on your system architecture).
Copy the file to the appropriate folders:
32 - bit windows:
   32 - bit file to C:/Windows/System32
64 - bit windows:
   32 - bit file to C:/Windows/System32
   and (if folder exists)
   64 - bit file to C:/Windows/System64 or SysWOW64


After running the program, wait until a welcome message appears on the black screen. If nothing happens for a while, you can press some letters on the keyboard, sometimes this helps. When the welcome message appears, you should choose the source of the image to be analyzed - either a movie from a webcam or a camera connected via USB or a movie saved in the computer's memory, which is recommended because the program analyzes live video and saves only the image, without sound. After choosing the source and location of the video in the computer's memory, choose the folder where all data and graphs will be saved. Next, choose one frame from the analysed movie, which will be the background in the graphs with the analysis of movement in x and y axis. Choose a moment in which the presenter is clearly visible. The videos are analyzed at about 26 frames per second, so it is easy to count the selected moment. Next, you have to choose whether you want to extract relevant fragments from the whole data set, e.g. selected moments that interest you most. You can choose an unlimited number of such fragments, but be careful that the start time is earlier than the end time, because the program may crash. For each cut fragment you should choose the density of the data given on the x-axis (i.e. time), because if the movie lasts for example 5 minutes you will not see anything on the x-axis due to the amount of data. Examples of density values: 80 - 19pom/min, 60 - 25pom/min, 40 - 37pom/min, 35 - 42pom/min, 80 - 5pom/15sec, 60 - 7pom/15sec, 40 - 10pom/15sec, 20 - 19pom/15sec . After selecting the density of the fragments, you need to select the density of the data file of the whole movie. Here large values are recommended. At the end you can choose to analyze another movie, or close the program.


The program license includes:
 - the use of the program only for the development and implementation of the project pbl "Development of a position for raising communication competence with the use of modern audiovisual solutions".

The project is under development, it is possible that a new version will appear in the near future.

Translated with www.DeepL.com/Translator (free version)