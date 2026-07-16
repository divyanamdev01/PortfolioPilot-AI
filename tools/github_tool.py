import requests

def username(github_url):
    return github_url.replace("https://github.com/", "").strip("/")

def get_profile(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code != 200:
        return None

    data = response.json()

    return {
        "name": data.get("name"),
        "username": data.get("login"),
        "followers" :data.get("follwers"),
        "public_repos": data.get("public_repos"),
        "bio": data.get("bio"),
        "location": data.get("location")
    }

def has_readme(username, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}/readme"
    response = requests.get(url)
    return response.status_code == 200

def get_repositories(username):
    repo_url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(repo_url)
    if response.status_code != 200:
        print("GitHub API Error:", response.text)
        return []
    repos=response.json()
    repo_data= []
    for repo in repos:
        repo_data.append({
            "name": repo.get("name"),
            "language":repo.get("language"),
            "stars":repo.get("stargazers_count"),
            'forks': repo.get("forks_count"),
            "has_readme": has_readme(username,repo.get("name")),
        })
    return repo_data

def language_count(repositories):
    languages={}
    for repo in repositories:   
        lang= repo.get("language")
        if lang is None:    
            continue
        languages[lang] = languages.get(lang, 0) + 1
    return languages

def total_starts(repositories):
    total = 0
    for repo in repositories:
        total += repo["stars"]
    return total

def best_repo(repositories):
    return max(repositories, key=lambda repo: repo["stars"])

def smry(github_url):
    user=username(github_url)
    repos=get_repositories(user)
    return {
        'profile':get_profile(user),
        'repositories':repos,
        'languages':language_count(repos),
        'totale_stars':total_starts(repos),
        'best_repo':best_repo(repos),
    }



print(smry("https://github.com/divyanamdev01") )
