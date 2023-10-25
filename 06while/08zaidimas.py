# (A - akmuo, Z - zirkles, P - popierius)
# zaidejas ir kompiuteris

import random

def game():
    moves = ['Akmuo', 'Popierius', 'Zirkles']
    zaidejas = input("Iveskite savo pasirinkima: (Akmuo, Popierius ar Zirkles)..")
    kompiuteris = random.choice(moves)
    print(f"kompiuterio pasirinkimas: {kompiuteris}")
    
    if zaidejas == kompiuteris:
        return "Lygiosios!"
    elif (kompiuteris == 'Akmuo' and kompiuteris == 'Zirkles') or \
        (kompiuteris == 'Zirkles' and kompiuteris == 'Popierius') or \
        (kompiuteris == 'Popierius' and kompiuteris == 'Akmuo'):
        return "Laimejote!"
    else:
        return "Pralaimejote!"

print(game())