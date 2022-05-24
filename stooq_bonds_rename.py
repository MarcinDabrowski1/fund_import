# import required module
import os

# assign directory
directory = 'stooq_bonds'
DATE = "20220523"

# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f.split(".csv")[0] + "." + DATE)
        os.rename(f, f.split(".csv")[0] + "." + DATE + ".csv")