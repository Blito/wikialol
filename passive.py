class Passive:
	def __init__(self, data_la, data_na = None, data_eu = None):
		self.description = data_la['description']

		# Fill name dicionary with other region's values
		self.name = {}
		self.name['la'] = data_la['name']
		if data_na:
			self.name['na'] = data_na['name']
		if data_eu:
			self.name['eu'] = data_na['name']

		# Remove . and spaces from image names
		self.image = self.name.replace(".", "").replace(" ", "") + '.png'

		self.sanitizedDescription = data_la['sanitizedDescription']