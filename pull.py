from subprocess import call

repo = "git@github.com:Froogss/testman-sam2.git"

pull_path = r"~/Desktop/git_pulls"

def pull(repo, location):
  call("git pull {} {}".format(repo, pull_path))
