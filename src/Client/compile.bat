pyinstaller --onefile --noconsole --icon icon.ico -n OpenLChat_Client_1.0_Portable_x64 MainWindow.py
rmdir build
rmdir __pycache__
del MainWindow.spec
pause