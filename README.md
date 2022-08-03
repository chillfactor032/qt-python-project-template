# QT Pyside6 Project Template

This repository will build a skeleton PySide6 project environment including a build script and the required dependencies to compile the project to exe using Nuitka. The dependencies of this project are in requirements.txt and are installed via pip. Nuitka has its own set of dependencies that may need to be satisfied (e.g. a compiler like clang). Check them out here:
[Nuitka User Manual](https://nuitka.net/doc/user-manual.html)

It will also compile Resource and UI files for you to use.

### Generate version.json and general build commands
To use:
 - Clone this repository
 - - `git clone https://github.com/chillfactor032/qt-python-project-template.git`
 - Run build.py to generate the version.json file.
 - `py build.py`
 - - version.json has "version", "project name", "company name" that control things about the project like file names, config file locations, and window title.
 - - The first time you run build.py it will generate this file.
- Run build.py again to compile the project to exe (optional)
- - `py build.py`

## Partial Builds (no compile)
You can also run `py build.py partial` to to only build the python part of the project but not compile it to exe. Imageio is included in the requirements because Nuitka uses it to convert png icons to ico when necessary.
You can test your partial build with `py MainWindow.py`

### UI Files
This project also contains a sample template ui file. This file is in the XML format provided by the Qt Designer. If you create the ui for your app, save the ui file to ./resources/ui. All ui files in ./resource/ui will get compiled into a single python file using the Qt tool uic.

### Resources
Qt uses a resource system that compiles files into a binary resources format. This allows you to use images and other files inside your script. The build script will compile all your resources into Resources.py and import it into MainWindow for use. All ui files in Resources.rc will get compiled into a single python file using the Qt tool rcc.

### So now what?
Edit MainWindow.py to suit your project.