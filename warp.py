#!/usr/bin/env python3
import subprocess
import sys

def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip() or result.stderr.strip()

print("\n=== Cloudflare WARP ===")
print("1. Connect")
print("2. Disconnect")
print("3. Exit")

choice = input("\nEnter choice: ").strip()

if choice == "1":
    print(run("warp-cli connect"))
elif choice == "2":
    print(run("warp-cli disconnect"))
elif choice == "3":
    sys.exit()
else:
    print("Invalid choice")
    