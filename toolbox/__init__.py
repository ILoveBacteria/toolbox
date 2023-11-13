from git import Repo

# Load project version
version = Repo().tags[-1]
