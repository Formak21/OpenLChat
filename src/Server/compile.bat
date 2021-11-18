pyinstaller --onefile --icon icon.ico -n OpenLChat_Server_1.0_Portable_x64 main.py
rmdir build
rmdir __pycache__
del main.spec
cp Database\* dist\Database\
pause