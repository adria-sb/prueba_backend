import sys
from github import Github, Auth
import os

# Inputs from environment
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("GITHUB_REPOSITORY")
PR_NUMBER = os.getenv("PR_NUMBER")

def analyze_code_placeholder(diff_text: str) -> str:
    """Fake AI reviewer for now."""
    return "🤖 (Placeholder) I looked at the changes. Looks fine for now!"

def main():
    gh = Github(auth=Auth.Token(GITHUB_TOKEN))
    repo = gh.get_repo(REPO_NAME)
    pr = repo.get_pull(int(PR_NUMBER))

    if pr.head.repo.full_name != repo.full_name:
        print("Skipping forked PR: cannot comment with GITHUB_TOKEN")
        return

    changed_files = pr.get_files()
    diffs = []
    for f in changed_files:
        if f.patch:
            diffs.append(f"File: {f.filename}\n{f.patch}")
    diff_text = "\n\n".join(diffs)

    review_text = analyze_code_placeholder(diff_text)
    pr.create_issue_comment(review_text)

if __name__ == "__main__":
    main()
