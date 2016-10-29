from .Sections import Section, Line

class FileParser(object):
	def __init__(self, pattern):
		self.pattern = pattern
		self._rerun = True

		# load pattern into objects
		with open(pattern, "r") as inp:
			self.root = Section(inp.read())

	def parse(self, filename):
		with open(filename, "r") as inp:
			for line in inp:
				while self._rerun:
					self._rerun = False
					status, result = self.root.run(line, self._rerun_line)
					#print "{}\n\n(Status, Result, Rerun) = ({}, {}, {})".format(line, status, result, self._rerun)
				if status == "complete":
					break
				self._rerun = True
		return result

	def _rerun_line(self):
		#print "Told to rerun"
		self._rerun = True