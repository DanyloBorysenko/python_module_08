import sys
from typing import Dict, Optional
import importlib


def dependencies_checker() -> Dict[str, Optional[str]]:
    """
    try to import required packages and return dict[package name, version]
    """
    print("Checking dependencies:")
    dependencies = {}
    required_packages = ["pandas", "numpy", "requests", "matplotlib"]
    for package in required_packages:
        try:
            module = importlib.import_module(package)
            dependencies[package] = getattr(module, "__version__", "Unknown")
        except ModuleNotFoundError as e:
            print(f"[Error] Error importing package: {e}")
            dependencies[package] = None
    return dependencies


def process_data() -> None:
    """
    1.Receive data using requests
    2.Transform data to DataFrame object and add new column 'title_len'
    3.Calculate average title length using numpy
    4.Visualize data using matplotlib
    """
    print("\nAnalyzing Matrix data...")

    # requests
    import requests
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = response.json()
    print(f"Processing {len(data)} data rows...")

    # pandas
    import pandas
    df = pandas.DataFrame(data)
    df["title_len"] = df["title"].apply(len)

    # numpy
    import numpy
    avg_title_len = numpy.mean(df["title_len"])
    print(f"Average title length is {avg_title_len}")

    # matplotlib
    import matplotlib.pyplot as plt
    print("Generating visualization..")
    plt.figure()
    plt.bar(df["id"], df["title_len"])
    plt.xlabel("ID")
    plt.ylabel("Title Length")
    plt.title("Title Length by Post ID")
    plt.show()


def main():
    print("LOADING STATUS: Loading programs...")
    dependencies_info = dependencies_checker()
    for module, version in dependencies_info.items():
        if version:
            print(f"[OK] {module} ({version}) - is ready")
        else:
            print(f"[ERROR] {module} - not installed")
    if None in list(dependencies_info.values()):
        print("\nInstall missing dependencies using:")
        print("pip install -r requirements.txt")
        sys.exit(1)
    process_data()


if __name__ == "__main__":
    # 'prefix' shows current path to the environment
    print("Virtual environment prefix:", sys.prefix)
    main()
#     [project]
# name = "ex1"
# version = "0.1.0"
# description = ""
# authors = [
#     {name = "danborys",email = "danborys@gmail.com"}
# ]
# requires-python = ">=3.13"
# dependencies = [
#     "pandas (>=3.0.0,<4.0.0)",
#     "numpy (>=2.4.2,<3.0.0)",
#     "requests (>=2.32.5,<3.0.0)",
#     "matplotlib (>=3.10.8,<4.0.0)"
# ]

# [tool.poetry]
# package-mode = false

# [build-system]
# requires = ["poetry-core>=2.0.0,<3.0.0"]
# build-backend = "poetry.core.masonry.api"
