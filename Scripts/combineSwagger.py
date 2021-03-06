#! /usr/bin/env python

import yaml
import glob

info = {}
paths = {}
defin = {}
for filename in glob.iglob('./**/*.yaml', recursive=True):
	print(filename)
	with open(filename, "r") as stream:
		try:
			fileObj = yaml.load(stream)
			info.update(fileObj['info'])
			paths.update(fileObj['paths'])
			defin.update(fileObj['definitions'])
		except yaml.YAMLError as exc:
			print(exc)
out = {'swagger': '2.0', 'info': info, 'paths': paths, 'definitions' : defin}

with open('out.yaml', 'w') as outfile:
	yaml.dump(out, outfile, default_flow_style=False)
