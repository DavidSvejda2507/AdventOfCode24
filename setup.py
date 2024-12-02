import argparse as AP
import os
import requests

parser = AP.ArgumentParser()

parser.add_argument("day")

args = parser.parse_args()

day = int(args.day)

assert(0<day<26)

directory = f"0{day}" if (day<10) else f"{day}"
if not os.path.isdir(directory):
    os.mkdir(directory)
    
if not os.path.isfile(f"{directory}/input.txt"):
    with open(f"{directory}/input.txt") as f:
        pass
    
if not os.path.isfile(f"{directory}/solution1.py"):
    with open(f"{directory}/solution1.py", "w") as f:
        pass
    
if not os.path.isfile(f"{directory}/solution2.py"):
    with open(f"{directory}/solution2.py", "w") as f:
        pass
