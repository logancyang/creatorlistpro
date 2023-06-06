import json
import os
import time

from utils.api_utils import setup_account

# Define the base directory
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURRENT_DIR)

# Define the path to the JSON file
file_path = os.path.join(BASE_DIR, 'data/output/output.json')

# Open and read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)



account = setup_account()
# account.tweet('test 123')
# account.like(1665954687538069504)
# account.unfollow(813286)
# account.create_list(
#     'Old Follows', 'All the people I followed before 06052023', private=True
# )
# 'Old Follows' has id 1665963043359199234
# account.add_list_member(1665963043359199234, 14647570)

"""
There's a limit how many you can add to a list per day.
'Authorization: You aren't allowed to add members to this list.'
"""
def add_list_members(user_id):
    account.add_list_member(1665963043359199234, user_id)
    print(f'Added user {user_id}, {user_name}')


for item in data:
    user_id = item['id']
    user_name = item['name']
    account.unfollow(user_id)
    print(f'Unfollowed user {user_id}, {user_name}')
    time.sleep(1)


print('Successfully added all users: ', len(data))
