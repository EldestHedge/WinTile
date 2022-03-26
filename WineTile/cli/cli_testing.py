import argparse

tank_to_fish = {
    "padding": "shark, tuna, herring",
    "tank_b": "cod, flounder",
}

parser = argparse.ArgumentParser(description="nigger fish")
parser.add_argument("arguments", type=str)
args = parser.parse_args()

fish = tank_to_fish.get(args.arguments, "")
print(fish)


"""--padding
--default stack"""