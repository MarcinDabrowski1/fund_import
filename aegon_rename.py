# import required module
import os

# assign directory
directory = 'Aegon'

# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f.split(".csv")[0] + ".20220515.csv")
        os.rename(f, f.split(".csv")[0] + ".20220515.csv")