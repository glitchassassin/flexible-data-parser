import fdp

inputfile = r"Z:\PARSED\file_formats\nonstockreqs.xml"

with open(inputfile, "r") as inp:
	xml = inp.read()

root = fdp.Section(xml)

