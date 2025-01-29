import datetime

def write_version_file():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("version.md", "w") as f:
        f.write(f"Last updated: {now}\n")

if __name__ == "__main__":
    write_version_file()
