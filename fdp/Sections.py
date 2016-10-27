import xml.etree.ElementTree as ET

class Section(object):
	def __init__(self, xml):
		self.repeats = False
		self.has_key = False
		self.name = ""
		self.ignore = False
		self.contents = []

		root = ET.fromstring(xml)
		if "repeats" in root.attrib and root.attrib["repeats"].lower() == "true":
			self.repeats = True
		if "ignore" in root.attrib and root.attrib["ignore"].lower() == "true":
			self.ignore = True
		if "name" in root.attrib:
			self.name = root.attrib["name"]

		for element in root.findall():
			if element.tag == "section":
				self.contents.append(Section(ET.tostring(element)))
			if element.tag == "line":
				self.contents.append(Line(ET.tostring(element)))
		
		if self.repeats:
			# These Sections will be stored in either a dictionary or a list,
			# depending on whether a key field has been defined for this section.
			if self.name and len(root.findall(".//field[@key='{}']".format(self.name))):
				self.has_key = True

	


class Line(object):
	def __init__(self, xml):
		self.regex = re.compile(regex)
		self.fields = fields
		if self.regex.groups != len(self.fields):
			raise ValueError("Number of capture groups in regex ({}) doesn't match the number of fields provided ({}). Regex:\n{}".format(self.regex.groups, len(self.fields), regex))
	