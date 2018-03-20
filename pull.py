from subprocess import call



def pull(repo, location):
  call("git pull {} {}".format(repo, location))
