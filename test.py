import subprocess

list_files = subprocess.run(["dir", "-l"])
# print("The exit code was: %d" % list_files.returncode)