import glob

all_files = glob.glob("*.csv")
df = pd.concat((pd.read_csv(f) for f in all_files), sort=False)
