import argparse
import urllib.request
import urllib.error 
import json

def get_gh_activity(username):
    url = f"https://api.github.com/users/{username}/events"

    try:
        request = urllib.request.Request(url, headers={"User-Agent": "gh-user-activity"})
        with urllib.request.urlopen(request) as response:
            data = json.loads(response.read().decode())
        return data
    except urllib.error.HTTPError as e:
        print(f"HTTP error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL error: {e.reason}")

def main():
    parser = argparse.ArgumentParser(prog="gh-activity")

    parser.add_argument("username", help="username of the github account")


    args = parser.parse_args()

    if args.username:
        events = (get_gh_activity(args.username))
        if events:
            for event in events[:5]:
                print(f"{args.username} did a {event['type'].replace('Event', '')} at {event['repo']['name']}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()