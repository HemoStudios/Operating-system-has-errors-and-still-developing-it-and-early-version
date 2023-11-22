print("welcome to NoterPad")
name = input("What is your name?: " )
print("hello "+name)
import subprocess
import time

def save_notepad():
    with open("notepad.txt", "r") as file:
        content = file.read()
    with open("saved_notepad.txt", "w") as file:
        file.write(content)
    print("Notepad content saved to 'saved_notepad.txt'.")

def open_program(program_name):
    if program_name.lower() == "notepad":
        print("Opening Notepad...")
        subprocess.Popen(["notepad.exe"])  # Opens Notepad in Windows
        save_notepad()  # Save the current content of Notepad
    elif program_name.lower() == "calculator":
        print("Opening Calculator...")
        calculator()
    elif program_name.lower() == "reversi":
        print("Starting Reversi...")
        play_reversi()  # Start the Reversi game
    elif program_name.lower() == "clock":
        print("Starting Clock...")
        show_clock()  # Show the clock
    else:
        print(f"Program '{program_name}' not found.")

# Reversi Game Functions
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def initialize_board():
    # Implement initialization of the Reversi board
    pass

def is_valid_move(board, row, col, player):
    # Implement logic to check if a move is valid
    pass

def make_move(board, row, col, player):
    # Implement logic to make a move on the board
    pass

def count_tiles(board):
    # Implement logic to count the tiles
    pass

def play_reversi():
    board = initialize_board()
    current_player = "X"
    # Implement the main game loop
    pass

# Calculator
def calculator():
    while True:
        print("\nSimple Calculator")
        print("Enter 'quit' to exit")
        expression = input("Enter an expression: ")
        if expression.lower() == "quit":
            break
        try:
            result = eval(expression)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

# Clock
def show_clock():
    while True:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print(f"Current time: {current_time}")
        time.sleep(1)
        subprocess.call("cls" if "nt" in subprocess.os.name else "clear", shell=True)

# Process user commands
def process_command(command):
    if command.lower() == "open notepad":
        print("Opening Notepad...")
        user_input = input("Enter something to add to Notepad: ")
        with open("notepad.txt", "a") as file:
            file.write(user_input + "\n")
        print(f"Added '{user_input}' to Notepad.")
    elif command.lower() == "hemo":
        print("You're the creator of mine.")
    elif command.lower() == "open start menu":
        print("Start Menu opened.")
        print("Available programs: Notepad, Calculator, Reversi, Clock")
        program = input("Enter program name to open: ")
        open_program(program)
    else:
        print("Command not recognized.")

# Start menu and user interaction
def start_menu():
    print("Commands: 'Open Start Menu', 'Hemo'")
    while True:
        user_command = input("Enter a command: ")
        process_command(user_command)

# Run the program
start_menu()
