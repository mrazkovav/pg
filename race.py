import os
import time
import random

# 👉 pro zvuk (Windows)
try:
    import winsound
    SOUND = True
except:
    SOUND = False

TRACK_LENGTH = 70

# 👉 názvy kamionů
truck1_name = input("Zadej název Kamionu 1: ")
truck2_name = input("Zadej název Kamionu 2: ")

truck1_pos = 0
truck2_pos = 0

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def beep(freq=800, duration=200):
    if SOUND:
        winsound.Beep(freq, duration)

def draw_track(name, pos):
    track = "-" * pos + "🚚" + "-" * (TRACK_LENGTH - pos)
    return f"{name}: |{track}|"

# 🔽 SEMAFOR ANIMACE
def semafor():
    frames = [
        ["🔴", "⚫", "⚫"],
        ["🔴", "⚫", "⚫"],
        ["🔴", "🟡", "⚫"],
        ["🔴", "🟡", "⚫"],
        ["⚫", "⚫", "🟢"],
        ["⚫", "⚫", "🟢"],
    ]

    for frame in frames:
        clear()
        print("🚦 STARTOVNÍ SEMAFOR\n")
        print(f"   {frame[0]}\n   {frame[1]}\n   {frame[2]}")

        if SOUND:
            winsound.Beep(500 + frames.index(frame)*150, 150)

        time.sleep(0.4)

    # 🔥 blikání zelené
    for _ in range(3):
        clear()
        print("🚦 STARTOVNÍ SEMAFOR\n")
        print("   ⚫\n   ⚫\n   ⚫")
        time.sleep(0.2)

        clear()
        print("🚦 STARTOVNÍ SEMAFOR\n")
        print("   ⚫\n   ⚫\n   🟢")
        beep(1200, 100)
        time.sleep(0.2)

    clear()
    print("🚦 START!\n")
    time.sleep(0.5)

# 🔽 SPUŠTĚNÍ SEMAFORU
semafor()

# 🔽 ZÁVOD
while truck1_pos < TRACK_LENGTH and truck2_pos < TRACK_LENGTH:
    clear()

    truck1_pos += random.randint(1, 3)
    truck2_pos += random.randint(1, 3)

    truck1_pos = min(truck1_pos, TRACK_LENGTH)
    truck2_pos = min(truck2_pos, TRACK_LENGTH)

    print("🏁 ZÁVOD KAMIONŮ 🏁\n")
    print(draw_track(truck1_name, truck1_pos))
    print(draw_track(truck2_name, truck2_pos))

    time.sleep(0.3)

clear()
print("🏁 ZÁVOD KAMIONŮ 🏁\n")

print(draw_track(truck1_name, truck1_pos))
print(draw_track(truck2_name, truck2_pos))

# 🔽 VÝSLEDEK
if truck1_pos > truck2_pos:
    winner = truck1_name
    print(f"\n🥇 Vyhrál {winner}!")
elif truck2_pos > truck1_pos:
    winner = truck2_name
    print(f"\n🥇 Vyhrál {winner}!")
else:
    winner = None
    print("\n🤝 Remíza!")

# 🎺 FANFÁRY
if SOUND:
    if winner:
        winsound.Beep(1000, 200)
        winsound.Beep(1200, 200)
        winsound.Beep(1500, 400)
    else:
        winsound.Beep(800, 300)
        winsound.Beep(800, 300)