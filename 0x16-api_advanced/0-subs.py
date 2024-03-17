import requests

def number_of_subscribers(subreddit):
  """
  Queries the Reddit API to get the number of subscribers for a subreddit.

  Args:
      subreddit (str): The name of the subreddit to query.

  Returns:
      int: The number of subscribers for the subreddit, or 0 if invalid.
  """

  url = f"https://www.reddit.com/r/{subreddit}/about.json"
  headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}

  try:
    response = requests.get(url, headers=headers, allow_redirects=False)
    response.raise_for_status()  # Raise exception for non-200 status codes

    results = response.json()
    subscribers = results.get("data", {}).get("subscribers", 0)
  except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    return 0

  return subscribers

