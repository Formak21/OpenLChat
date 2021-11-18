pyinstaller --onefile --icon icon.ico -n OpenLChat_Server_1.0_Portable_x64 main.py
rmdir /S /Q build
rmdir /S /Q __pycache__
del OpenLChat_Server_1.0_Portable_x64.spec
mkdir dist\Database
copy Database dist\Database\
pause