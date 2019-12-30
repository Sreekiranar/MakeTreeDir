import os

class MAKETREEDIR:
	def __init__(self):
		pass
	def makedir(self,dir_path):
		"""Short summary.
		Args:
			dir_path (type): Path of the directory to be created (can be subfolder also).
		Returns:
			type: 0 if success
		Examples
			Examples should be written in doctest format, and
			should illustrate how to use the function/class.
			>>> from MakeTreeDir import MAKETREEDIR
			>>> md=MAKETREEDIR()
			>>> md.makedir('this/is/a/testing/package/creation')
			# Can also deal with inputs like
			>>> md.makedir('/media/username/New Volume/folderName')
			>>> md.makedir('../../../folderName')
		"""
		try:
			sep='/' if '/' in dir_path else '\\'
			dirs=dir_path.split(sep)
			if len(dirs[0])==0:
				dirs[1]=sep+dirs[1]
				dirs=dirs[1:]
			for i,fol in enumerate(dirs):
				path=dirs[:i+1]
				directory=os.path.join(*path)
				os.makedirs(directory,exist_ok=True)
		except Exception as e:
			return e

		return 0
