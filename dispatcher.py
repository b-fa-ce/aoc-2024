import sys
from importlib import import_module


def run_day():
    if len(sys.argv) < 2:
        print("Usage: poetry day <day_number>")
        sys.exit(1)

    day = sys.argv[1].zfill(2)
    module_name = f"aoc_2024.day_{day}.src.main"
    print(module_name)

    try:
        module = import_module(module_name)
        if hasattr(module, "main"):
            module.main()
        else:
            print(f"No 'main' function found in {module_name}")
    except ModuleNotFoundError:
        print(f"Module {module_name} not found.")
