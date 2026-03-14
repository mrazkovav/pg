import os
import time
import random


TRACK_LENGTH = 70


truck1_pos = 0
truck2_pos = 0

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def draw_track(name, pos):
    track = "-" * pos + "🚚" + "-" * (TRACK_LENGTH - pos)
    return f"{name}: |{track}|"

while truck1_pos < TRACK_LENGTH and truck2_pos < TRACK_LENGTH:
    clear()

    
    truck1_pos += random.randint(1, 3)
    truck2_pos += random.randint(1, 3)

    
    truck1_pos = min(truck1_pos, TRACK_LENGTH)
    truck2_pos = min(truck2_pos, TRACK_LENGTH)

    print("🏁 ZÁVOD KAMIONŮ 🏁\n")
    print(draw_track("Kamion 1", truck1_pos))
    print(draw_track("Kamion 2", truck2_pos))

    time.sleep(0.3)

clear()
print("🏁 ZÁVOD KAMIONŮ 🏁\n")

print(draw_track("Kamion 1", truck1_pos))
print(draw_track("Kamion 2", truck2_pos))

if truck1_pos > truck2_pos:
    print("\n🥇 Vyhrál Kamion 1!")
elif truck2_pos > truck1_pos:
    print("\n🥇 Vyhrál Kamion 2!")
else:
    print("\n🤝 Remíza!")
