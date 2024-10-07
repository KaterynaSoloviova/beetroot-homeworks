# Task 1
# Robots.txt
# Download and save to file robots.txt from wikipedia, twitter websites etc.

import requests


def download_robots_file(url: str, prefix: str) -> None:
    file_url = f"{url}/robots.txt"
    response = requests.get(file_url)

    file_name = f"{prefix}.robots.txt"

    with open(file_name, "w") as file:
        file.write(response.text)


download_robots_file("https://en.wikipedia.org", "wikipedia")
download_robots_file("https://x.com", "twitter")
