import sys
from github import Github, Auth
import os

# Inputs from environment
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("GITHUB_REPOSITORY")
PR_NUMBER = os.getenv("PR_NUMBER")

# File extensions we want to skip (non-code files)
SKIP_EXTENSIONS = {".md", ".txt", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".pdf"}

def is_relevant_file(filename: str) -> bool:
    """Return True if the file looks like code worth reviewing."""
    _, ext = os.path.splitext(filename.lower())
    return ext not in SKIP_EXTENSIONS

def parse_patch(patch: str) -> str:
    """Extract and clean the diff so it's easier for AI to analyze."""
    # For now, just return patch (could add trimming or line limits later)
    return patch.strip()

def analyze_code_placeholder(file_diffs: list) -> str:
    """
    Fake AI reviewer for now.
    file_diffs is a list of tuples: (filename, diff_text).
    """
    comments = ["🤖 (Placeholder) Code review summary:"]
    for filename, diff_text in file_diffs:
        comments.append(f"\n### File: `{filename}`\n```diff\n{diff_text}\n```")
    return "\n".join(comments)

def main():
    gh = Github(auth=Auth.Token(GITHUB_TOKEN))
    repo = gh.get_repo(REPO_NAME)
    pr = repo.get_pull(int(PR_NUMBER))

    # Skip PRs from forks
    if pr.head.repo.full_name != repo.full_name:
        print("Skipping forked PR: cannot comment with GITHUB_TOKEN")
        return
    
    # Skip PRs not targeting main
    if pr.base.ref != "main":
        print(f"Skipping PR #{PR_NUMBER}: target branch is {pr.base.ref}, not main")
        return


    changed_files = pr.get_files()
    file_diffs = []
    
    for file in changed_files:

        if not is_relevant_file(file.filename):
            print(f"Skipping non-code file: {file.filename}")
            continue

        if not file.patch:
            print(f"No patch available for file: {file.filename}")
            continue
        
        cleaned_patch = parse_patch(file.patch)
        file_diffs.append((file.filename, cleaned_patch))

    if not file_diffs:
        print("No relevant code changes to review.")
        return
    
    review_text = analyze_code_placeholder(diff_text)
    pr.create_issue_comment(review_text)
    print("Review comment posted successfully.")


if __name__ == "__main__":
    main()
