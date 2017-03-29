class FsharpPackage(GitHubTarballPackage):
	def __init__(self):
		GitHubTarballPackage.__init__(self,
			'fsharp', 'fsharp',
			'4.1.5',
			'24eb0bc4bfdde9b4c12b604757ea8db209bf2aa3',
			configure = './configure --prefix="%{package_prefix}"')

		self.extra_stage_files = ['lib/mono/xbuild/Microsoft/VisualStudio/v/FSharp/Microsoft.FSharp.Targets']
		self.sources.extend (['patches/fsharp-fix-mdb-support.patch'])

	def prep(self):
		Package.prep (self)

		for p in range (1, len (self.sources)):
				self.sh ('patch -p1 < "%{local_sources[' + str (p) + ']}"')

	def build(self):
		self.sh ('autoreconf')
		Package.configure (self)
		Package.make (self)

FsharpPackage()
