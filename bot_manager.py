import subprocess
import sys
import os

bots = [
    os.path.join('sigma_bot', 'telegram_bot.py'),
    os.path.join('math_bot', 'telegram_bot.py'),
    os.path.join('fitness_bot', 'telegram_bot.py'),
    os.path.join('travel_bot', 'telegram_bot.py'),
    os.path.join('kokobot', 'telegram_bot.py'),
]

processes = []
for bot in bots:
    abs_path = os.path.abspath(bot)
    print(f"Starting {bot}...")
    p = subprocess.Popen([sys.executable, abs_path])
    processes.append(p)

print("All bots are running! Press Ctrl+C to stop.")
try:
    for p in processes:
        p.wait()
except (KeyboardInterrupt, SystemExit):
    print("Stopping all bots...")
    for p in processes:
        p.terminate()
