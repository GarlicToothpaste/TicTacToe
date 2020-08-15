@echo off 
if exist .\"TicTacToe in Python" (
    rmdir /s /q "TicTacToe in Python"
    echo. && echo Deleted original folder of TicTacToe in Python!
)
pyinstaller --onedir TicTacToe-Networking.py --name "TicTacToe in Python" && echo. && echo Successfully created the executable file for TicTacToe in Python!
move dist\"TicTacToe in Python" . && echo. && echo Moved directory successfully!
rmdir dist && echo. && echo Successfully removed dist folder...
rmdir /s /q build && echo. && echo Successfully removed build folder...
rmdir /s /q __pycache__ && echo. && echo Successfully removed __pycache__ folder...
del *.spec && echo. && echo Successfully removed the spec file...