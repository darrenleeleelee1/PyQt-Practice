# PyQt5 Practice

## Set up
1. Create a new enviroment
```
conda create -n qt_env python=3.8
```
2. Activate the new enviroment
```
activate qt_env
```
3. Install PyQt5
```
pip install pyqt5
pip install pyqt5-tools
```
4. Check
```
import PyQt5
```
## Example
1. Calculator

## Extension
[PyQt APIs](https://doc.qt.io/qtforpython/api.html)

[Python Lambda](https://www.w3schools.com/python/python_lambda.asp)

[Tutorial](https://www.tutorialspoint.com/pyqt/index.htm)

## Qt Designer to Python Code
[link](https://realpython.com/qt-designer-python/)

* Shell
```
pyuic5 -x ____.ui -o ____.py 
```

## qrc file to py file
* Shell
```
Pyrcc5 ____.qrc -o ____.py
```
