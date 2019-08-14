from github import Github

class CCGithub:

	def __init__(self, gtoken, repo):
		self.github = Github(gtoken)
		print(gtoken)
		self.repo = self.github.get_repo(repo)

	def listFiles(self):
		contents = self.repo.get_contents("")
		file_names = []
		while contents:
			file_content = contents.pop(0)
			if file_content.type == "dir":
			     contents.extend(self.repo.get_contents(file_content.path))
			else:
				file_names.append(file_content.name)
		return file_names

	def getContent(self, filename):
		content_file = self.repo.get_contents(filename)
		return content_file.decoded_content
		

	def createOrUpdateFile(self, contents, filename):
		try:
			fcontents = self.repo.get_contents(filename)
			self.repo.update_file(filename, "update", contents, fcontents.sha, branch="master")
		except:
			self.repo.create_file(filename, "create test file", contents, branch="master")


