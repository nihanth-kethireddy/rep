import os
from git import Repo
from github import Github

# COMMITS_TO_PRINT = 5

# for pull in r.get_pulls('all'):

# def print_commit(commit):
#     print('----')
#     print(str(commit.hexsha))
#     print("\"{}\" by {} ({})".format(commit.summary,
#                                      commit.author.name,
#                                      commit.author.email))
#     print(str(commit.authored_datetime))
#     print(str("count: {} and size: {}".format(commit.count(),
#                                               commit.size)))


def print_repository(repo):
    print('Repos description: {}'.format(repo.description))
    print('Repo active branch is {}'.format(repo.active_branch))
    for remote in repo.remotes:
        print('Remote named "{}" with URL "{}"'.format(remote, remote.url))
    print('Last commit for repo is {}.'.format(str(repo.head.commit.hexsha)))


if __name__ == "__main__":
    repo_path = os.getenv('GIT_REPO_PATH')
    # Repo object used to programmatically interact with Git repositories
    repo = Repo(repo_path)
    g = Github("f927a6147c4ddcb6027c2ba15a06d1f2b4883755")
    for eachrepo in g.get_user().get_repos():
        print(eachrepo.name)
    # g = Github(login_or_token=$YOUR_TOKEN, per_page=100)
    # r = g.get_repo($REPO_NUMBER)
    # check that the repository loaded correctly
    if not repo.bare:
        print('Repo at {} successfully loaded.'.format(repo_path))
        print_repository(repo)
        # head = repo.lookup_reference('HEAD').resolve()
        # head = repo.head

        # branch_name = head.name
        # print branch_name
        # create list of commits then print some of them to stdout
        # commits = list(repo.iter_commits('master'))[:COMMITS_TO_PRINT]
        # for commit in commits:
        #     print_commit(commit)
        #     pass
        # branch_name = head.name
        # print branch_name
        # create list of commits then print some of them to stdout
        # commits = list(repo.iter_commits('master'))[:COMMITS_TO_PRINT]
        # for commit in commits:
        #     print_commit(commit)
        #     pass
    else:
        print('Could not load repository at {} :('.format(repo_path))