
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--schema")

arguments = parser.parse_args()

print(arguments.schema)