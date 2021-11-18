pyinstaller --onefile --noconsole --icon icon.ico -n OpenLChat_Client_1.0_Portable_x64 MainWindow.py
rmdir /S /Q build
rmdir /S /Q __pycache__
del OpenLChat_Client_1.0_Portable_x64.spec
copy pic.png dist\
pause