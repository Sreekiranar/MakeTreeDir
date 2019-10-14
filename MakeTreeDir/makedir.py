import os

class MAKETREEDIR:
	def __init__(self):
		pass
	def makedir(self,dir_path):
		"""Short summary.

		Args:
			dir_path (type): Path of the directory to be created ( can be subfolder also).

		Returns:
			type: 0 if success

		Examples
			Examples should be written in doctest format, and
			should illustrate how to use the function/class.
			>>> from MakeTreeDir import MAKETREEDIR
			>>> MAKETREEDIR().makedir('this/is/a/testing/package/creation')

		"""
		sep='/' if '/' in dir_path else '\\'
		dirs=dir_path.split(sep)

		for i,fol in enumerate(dirs):
			path=dirs[:i+1]
			directory=os.path.join(*path)
			if not os.path.exists(directory):
				os.makedirs(directory)
		return 0
