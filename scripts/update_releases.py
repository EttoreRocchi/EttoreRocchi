"""Refresh the "Latest Releases" block of the profile README from GitHub Releases."""

import json
import os
import re
import urllib.request
from pathlib import Path

OWNER = "EttoreRocchi"
REPOS = [
    "MaldiSuite",
    "MaldiAMRKit",
    "MaldiBatchKit",
    "MaldiDeepKit",
    "combatlearn",
    "ResPredAI",
    "phenocluster",
    "nestkit",
]
N_RELEASES = 5

README = Path(__file__).resolve().parent.parent / "README.md"
START = "<!-- LATEST-RELEASES:START -->"
END = "<!-- LATEST-RELEASES:END -->"


def fetch_releases(repo):
    url = f"https://api.github.com/repos/{OWNER}/{repo}/releases?per_page={N_RELEASES}"
    request = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def main():
    releases = []
    for repo in REPOS:
        for release in fetch_releases(repo):
            if release["draft"] or release["prerelease"]:
                continue
            releases.append((release["published_at"], repo, release["tag_name"], release["html_url"]))
    releases.sort(reverse=True)

    lines = [
        f"- [**{repo}** {tag}]({url}) - {published[:10]}"
        for published, repo, tag, url in releases[:N_RELEASES]
    ]
    block = "\n".join([START, *lines, END])

    text = README.read_text()
    pattern = re.compile(re.escape(START) + ".*?" + re.escape(END), flags=re.DOTALL)
    if not pattern.search(text):
        raise SystemExit(f"Markers {START} / {END} not found in {README}")
    README.write_text(pattern.sub(lambda _: block, text))


if __name__ == "__main__":
    main()
