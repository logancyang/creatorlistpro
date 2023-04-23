import json

from utils.api_utils import setup_tweepy_client


def get_all_followings(client, username):
    resp = client.get_user(username=username, user_auth=True)
    user_id = resp.data.id
    followings = []
    pagination_token = None

    while True:
        response = client.get_users_following(
            user_id,
            max_results=1000,
            pagination_token=pagination_token,
            user_fields=['id', 'name', 'description'],
            user_auth=True
        )
        followings.extend(response.data)

        if 'next_token' in response.meta:
            pagination_token = response.meta['next_token']
        else:
            break

    return followings

api_client = setup_tweepy_client()
my_user_name = 'logancyang'
followings = get_all_followings(api_client, my_user_name)

# Save followings to a JSON file
with open('output.json', 'w') as f:
    json.dump([
        {
            'id': user.id,
            'name': user.name,
            'bio': user.description
        } for user in followings], f
    )
