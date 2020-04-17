import argparse
import os
import pandas as pd 

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Converts csv to txt')
	parser.add_argument("--source", type = str, help = "Directory of Files containing csv files")
	parser.add_argument("--dst", type = str, help = "Directory to write the txt files")
	parser.add_argument("--content", type = str, help = "Column to write the content")

	args = parser.parse_args()

	files = os.listdir(args.source)
	
	for file in files:
		data = pd.read_csv(args.source + "/" + file)
		required_data = data[args.content].tolist()

		for idx, record in enumerate(required_data):
			with open(args.dst + "/" + file.split(".")[0] + str(idx) + ".txt", "a") as f:
				f.write(record)



