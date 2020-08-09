pyinstaller --onedir TicTacToe-Computer.py --name "TicTacToe in Python"
move dist\"TicTacToe in Python" .
rmdir dist
rmdir /s /q build
rmdir /s /q __pycache__
del *.spec
exit