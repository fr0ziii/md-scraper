import os
import requests
from bs4 import BeautifulSoup
import re
import argparse

def download_markdown(repo_url, output_dir="docs"):
    """
    Downloads all markdown files from a GitHub repository to a specified directory.

    Args:
        repo_url (str): The URL of the GitHub repository.
        output_dir (str): The directory to save the markdown files to. Defaults to "docs".
    """

    try:
        # Create the output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Find all the markdown files using GitHub API
        api_url = f"{repo_url.replace('github.com', 'api.github.com/repos')}/contents"
        response = requests.get(api_url)
        response.raise_for_status()
        contents = response.json()

        markdown_files = []
        def get_markdown_files(contents, depth=0, max_depth=3):
            if depth > max_depth:
                return
            for item in contents:
                if item["type"] == "file" and item["name"].endswith(".md"):
                    markdown_files.append(item["download_url"])
                elif item["type"] == "dir":
                    dir_url = item["url"]
                    response = requests.get(dir_url)
                    response.raise_for_status()
                    dir_contents = response.json()
                    get_markdown_files(dir_contents, depth + 1, max_depth)
        
        get_markdown_files(contents)

        # Download each markdown file
        for download_url in markdown_files:
            file_name = download_url.split("/")[-1]
            output_path = os.path.join(output_dir, file_name)

            response = requests.get(download_url)
            response.raise_for_status()

            with open(output_path, "wb") as f:
                f.write(response.content)

            print(f"Downloaded {file_name} to {output_path}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Downloads all markdown files from a GitHub repository.")
    parser.add_argument("repo_url", help="The URL of the GitHub repository.")
    parser.add_argument("-o", "--output_dir", help="The directory to save the markdown files to.", default="docs")
    args = parser.parse_args()

    try:
        download_markdown(args.repo_url, args.output_dir)
    except Exception as e:
        print(f"An error occurred: {e}")
