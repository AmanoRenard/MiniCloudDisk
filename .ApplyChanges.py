# After you changed files or directions, please run this program.
# Require: Python3.6+
# Please change it to your MiniCloudDisk path (e.g. "D:/Code/GUI/test/MiniCloudDisk"):
APP_PATH = "./"

import sys
from pathlib import Path

root_path = Path(APP_PATH)
if not (init_index := root_path / ".initindex").exists():
    print("Path error! Please modify APP_PATH to the root directory of MiniCloudDisk.")
    sys.exit(0)
with open(init_index, "r", encoding="utf-8") as f:
    init_data = f.readlines()
    start_init_data = init_data[:114]
    init_data = init_data[114:]

def update_index(currpath : Path):
    if currpath.is_dir():
        currindex = currpath / "index.html"
        if not currindex.exists():
            currindex.touch()
        writing_data = ""
        for childpath in currpath.iterdir():
            if not childpath.name.startswith(".") and childpath.name != "index.html":
                if childpath.is_dir():
                    update_index(childpath)
                    writing_data += f"        {childpath.name}/\n"
                else:
                    writing_data += f"        {childpath.name}\n"
        with open(currindex, "w", encoding="utf-8") as f:
            for i in start_init_data:
                f.write(i)
            f.write(writing_data)
            for i in init_data:
                f.write(i)

update_index(root_path)
