import re
import requests

URL = 'https://pastebin.com/api/api_post.php'
DEVELOPER_API_KEY = '0TUl-b2MtZSGvrSvCRszGOTrOxY1lr08'
def main():
    post_new_paste('paste', 'i dont care', '', '')
def post_new_paste(title, body_text, expiration='10M', listed=True):

    params = {
        'api_dev_key': '0TUl-b2MtZSGvrSvCRszGOTrOxY1lr08',
        'api_option'  : 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title, 
        'api_paste_expire_date': expiration,
        'api_paste_private': 0 if listed else 1 
    }
    print("Posting new paste to pastebin...", end='')
    resp_msg = requests.post(URL, data=params)


    if resp_msg.status_code ==requests.codes.ok:
        print('success.')
        return resp_msg.text
    else: 
        print("failure")
        print(f"Response code: {resp_msg.status_code} ({resp_msg.reason})")
        print(f"Error: {resp_msg.text}")
    pass


    return
if __name__ == "__main__":
    main()
 