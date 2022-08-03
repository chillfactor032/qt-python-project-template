# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.2.2
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x00\xb7\
\x0d\
\x0a{\x0d\x0a    \x22version\
\x22: \x221.0\x22,\x0d\x0a    \x22\
ico\x22: \x22./resourc\
es/img/<ICON>.pn\
g\x22,\x0d\x0a    \x22compan\
y_name\x22: \x22ChillA\
spect\x22,\x0d\x0a    \x22pr\
oduct_name\x22: \x22Te\
mplateTest\x22,\x0d\x0a  \
  \x22description\x22:\
 \x22This is a test\
\x22\x0d\x0a}\x0d\x0a\
"

qt_resource_name = b"\
\x00\x0c\
\x0d\x8c.^\
\x00v\
\x00e\x00r\x00s\x00i\x00o\x00n\x00.\x00j\x00s\x00o\x00n\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x82`\x97\x04\xfa\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
