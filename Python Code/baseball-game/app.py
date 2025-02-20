import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_field(bases):
    field = [
        "           H           ",  # Home plate at top
        "          /\\          ",
        "         /  \\         ",
        "        /    \\        ",
        "       /      \\       ",
        "      /        \\      ",
        "     /          \\     ",
        "    /            \\    ",
        "   1              3    ",  # First base on right, Third base on left
        "    \\            /    ",
        "     \\          /     ",
        "      \\        /      ",
        "       \\      /       ",
        "        \\    /        ",
        "         \\  /         ",
        "           2           "   # Second base
    ]

    # Replace base markers with runners
    if bases[1]: # second base
        field[15] = field[15].replace("2", "🏃")
    if bases[0]: # first base
        field[8] = field[8].replace("1", "🏃")
    if bases[2]: # third base
        field[8] = field[8].replace("3", "🏃")
    if any(bases): # if any runners have scored (reached home)
        field[0] = field[8].replace("H", "⚾")
    
    return "\n".join(field)

def play_baseball():
    print("\nWelcome to Baseball simulator!")
    score = 0
    outs = 0
    inning = 1
    bases = [0, 0, 0] # represent 1st, 2nd, and 3rd base

    while inning <- 9:
        clear_screen()
        # Randomly add base runners at the start of each bat
        if random.random() < 0.3:
            empty_bases = [i for i, base in enumerate(bases) if base == 0]
            if empty_bases:
                random_bases = random.choice(empty_bases)
                bases[random_bases] = 1
                print(f"\nA Runner has advanced to {random_bases + 1}st base")

        print(f"\nInning {inning}")
        print(f"Score: {score}")
        print(f"Outs: {'●' * outs + '○' * (3-outs)}")
        print(f"\n{draw_field(bases)}\n")

        print(f"\nChoose your pitch to hit:")
        print("1. Fastball")
        print("2. Curveball")
        print("3. Changeup")