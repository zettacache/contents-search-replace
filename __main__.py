from sys import argv
import toml


def main(base: str, map: dict):
    for key, value in map.items():
        base = str.replace(base, f"&&{key}", value)

    with open(argv[3] or "./csr-output", "w") as output_file:
        output_file.write(base)


if __name__ == "__main__":
    with open(argv[1], "r") as base_file:
        base = base_file.read()

    with open(argv[2], "r") as map_file:
        map = toml.load(map_file)

    main(base=base, map=map)
