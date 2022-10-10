# Runs this script if you want to make a new .exe file
# Need python and pyinstaller installed

pyinstaller app.spec
mv dist/Mine_Sweeper.exe Mine_Sweeper.exe
rm -r __pycache__/ build/ dist/
