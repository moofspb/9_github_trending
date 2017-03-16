from datetime import date, timedelta
import argparse
import requests


def get_trending_repositories(top_repos_amount):
    week = date.today() - timedelta(days=7)  # for check new repos less than 1 week old
    api_url = 'https://api.github.com/search/repositories'
    parameters = {
        'q': 'created:>={}'.format(str(week)),
        'sort': 'stars',
    }
    all_repositories = requests.get(api_url, params=parameters).json()
    trending_repositories = all_repositories['items'][:top_repos_amount]
    return trending_repositories


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script find the most trending new/ '
                                                 'repositories on github.com')
    parser.add_argument('--repos_amount',
                        type=int,
                        const=20,
                        default=20,
                        nargs='?',
                        help='Amount of trending repositories')
    args = parser.parse_args()
    trending_repos = get_trending_repositories(args.repos_amount)
    print('There is {} most trending repositories on Github.com for the last week:'.format(
        args.repos_amount)
    )
    for repo in trending_repos:
        print('Repository: {}, issues: {}, link: "https://github.com/{}"'.format(
            str(repo['name']), repo['open_issues_count'],
            repo['full_name'])
        )
