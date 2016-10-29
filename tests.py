import fdp

parsemap = r"C:\Users\jwinsley\Downloads\nonstockreqs.xml"
inputfile = r"C:\Users\jwinsley\Downloads\Detail_LIVE.txt"


parser = fdp.FileParser(parsemap)

#print parser.root.debug()

result = parser.parse(inputfile)

print result
