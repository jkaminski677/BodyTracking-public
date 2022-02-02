from cx_Freeze import setup, Executable

base = None

executables = [Executable("owesome_meine_posedet.py", base=base)]

packages = ["pose_module", "create_datas", "PIL", "idna", "re", "cv2", "time", "datetime", "csv",
            "pandas", "matplotlib", "tkinter", "numpy", "os", ]
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name="Body_move_detector",
    options=options,
    version="<any nuip imber>",
    description='<any description>',
    executables=executables
)


# To create an executable program:
# visit this pages:
# - https://stackoverflow.com/questions/41570359/how-can-i-convert-a-py-to-exe-for-python
# - https://regilanj.wordpress.com/2017/06/07/py-to-exe-in-python-3-6-1/

#  and if there's nothing there:


# Steps to convert .py to .exe in Python 3.6
#
# Install Python 3.6.
# Install cx_Freeze, (open your command prompt and type pip install cx_Freeze.
# Install idna, (open your command prompt and type pip install idna.
# Write a .py program named myfirstprog.py.
# Create a new python file named setup.py on the current directory of your script.
# In the setup.py file, copy the code below and save it.
# With shift pressed right click on the same directory, so you are able to open a command prompt window.
# In the prompt, type python setup.py build
# If your script is error free, then there will be no problem on creating application.
# Check the newly created folder build. It has another folder in it. Within that folder you can find your application. Run it. Make yourself happy.
# See the original script in my blog.
#
# setup.py:
#
# from cx_Freeze import setup, Executable
#
# base = None
#
# executables = [Executable("myfirstprog.py", base=base)]
#
# packages = ["idna"]
# options = {
#     'build_exe': {
#         'packages':packages,
#     },
# }
#
# setup(
#     name = "<any name>",
#     options = options,
#     version = "<any number>",
#     description = '<any description>',
#     executables = executables
# )

