#!/usr/bin/env python
input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "r") as f:
    lines = f.readlines()

names = []
for line in lines:
    if "user:" not in line:
        continue
    start_index = line.find("[") + 1
    end_index = line.find("]", start_index)
    name = line[start_index:end_index]
    names.append(name)

with open(output_file, "w") as f:
    for name in names:
        f.write(name + "\n")
