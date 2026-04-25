import os
import json
import logging
from urllib import request, error

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

GITHUB_USERNAME = "duan-n2d"

def fetch_github_data():
    """Fetches public repositories for a given GitHub username."""
    api_url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos?per_page=100&type=owner"
    
    headers = {"User-Agent": "Portfolio-Data-Pipeline"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"
        
    req = request.Request(api_url, headers=headers)
    
    try:
        with request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return data
    except error.URLError as e:
        logging.error(f"Failed to fetch GitHub data: {e}")
        return []

def aggregate_metrics(repos):
    """Aggregates metrics from raw repository data."""
    total_stars = 0
    total_forks = 0
    languages = {}
    
    # Exclude forks by the user in metrics if desired, but here we include all 
    # or filter out forks the user created from others to show original work.
    original_repos = [repo for repo in repos if not repo.get('fork', False)]
    
    for repo in original_repos:
        total_stars += repo.get('stargazers_count', 0)
        total_forks += repo.get('forks_count', 0)
        
        lang = repo.get('language')
        if lang:
            languages[lang] = languages.get(lang, 0) + 1
            
    # Sort languages by count
    sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
    
    return {
        "github": {
            "total_repositories": len(repos),
            "original_repositories": len(original_repos),
            "total_stars": total_stars,
            "total_forks": total_forks,
            "top_languages": dict(sorted_languages[:5])
        }
    }

def main():
    logging.info("Starting data extraction pipeline...")
    
    repos = fetch_github_data()
    if not repos:
        logging.warning("No data retrieved from GitHub.")
        # We might still want to proceed to output an empty or default json rather than failing
        
    metrics = aggregate_metrics(repos)
    
    # Define output path
    output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'portfolio_metrics.json')
    
    # Save JSON
    with open(output_file, 'w') as f:
        json.dump(metrics, f, indent=2)
        
    logging.info(f"Successfully saved metrics to {output_file}")
    logging.info(f"Metrics summary: {json.dumps(metrics)} ")

if __name__ == "__main__":
    main()
