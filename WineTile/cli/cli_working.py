import argparse


parser = argparse.ArgumentParser()

parser.add_argument(
    "--pad",
    type=str,
    help="amount of padding between windows"
)

parser.add_argument(
    "--startup",
    type=str,
    action=argparse.BooleanOptionalAction,
    help="start this application with Windows",
)

args = parser.parse_args()

if args.pad:
    print(f"padding space: {args.pad}px")

if args.startup:
    print("startup is on")
