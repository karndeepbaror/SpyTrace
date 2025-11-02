import os
import sys
import time

# ye colour combination h sir 
R = "\033[91m"  # red
G = "\033[92m"  # green
C = "\033[96m"  # cyan
Y = "\033[93m"  # yellow
W = "\033[0m"   # reset

print(f"{C}╔════════════════════════════════════╗")
print(f"{C}║{Y}      SpyTrace - Camera Guard 🛰️     {C}║")
print(f"{C}╚════════════════════════════════════╝{W}\n")

print(f"{Y}Scanning Your System For Active Camera...{W}")
time.sleep(2)

active = False
reason = ""

if sys.platform.startswith("linux") or "termux" in sys.executable.lower():
    try:
        for dev in os.listdir("/dev"):
            if dev.startswith("video"):
                active = True
                reason = f"Found device: /dev/{dev}"
                break
    except Exception as e:
        reason = "Permission denied while checking /dev directory."

elif sys.platform.startswith("win"):
    reason = "Windows camera detection limited (needs admin rights)."

elif sys.platform.startswith("darwin"):
    reason = "macOS system detected. Cannot check camera via Python."

print()
if active:
    print(f"{G}[✓] Camera Active{W}")
    print(f"{C}Reason:{W} {reason}\n")
else:
    print(f"{R}[✗] Camera Not Active{W}")
    if reason:
        print(f"{C}Note:{W} {reason}\n")

print(f"{Y}Scan Complete.{W}")
