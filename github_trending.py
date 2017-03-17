from datetime import date, timedelta
import argparse
import requests


def get_script_args():
    parser = argparse.ArgumentParser(description='Script find the most trending new/ '
                                                 'repositories on github.com')
    parser.add_argument('--repos_amount',
                        type=int,
                        const=20,
                        default=20,
                        nargs='?',
                        help='Amount of trending repositories')
    args = parser.parse_args()
    return args.repos_amount


def get_trending_repositories(top_repos_amount, repo_creation_period=7):
    days_ago = date.today() - timedelta(days=repo_creation_period)
    api_url = 'https://api.github.com/search/repositories'
    parameters = {
        'q': 'created:>={}'.format(str(days_ago)),
        'sort': 'stars',
        'per_page': top_repos_amount
    }
    trending_repositories = requests.get(api_url, params=parameters).json()['items']
    return trending_repositories


def print_trending_repositories(trending_repositories):
    for repo in trending_repositories:
        print('Repository: {}, issues: {}, link: "https://github.com/{}"'.format(
            str(repo['name']), repo['open_issues_count'],
            repo['full_name'])
        )


if __name__ == '__main__':
    repos_amount = get_script_args()
    trending_repos = get_trending_repositories(repos_amount)
    print('There is {} most trending repositories on Github.com for the last week:'.format(
        repos_amount)
    )
    print_trending_repositories(trending_repos)
