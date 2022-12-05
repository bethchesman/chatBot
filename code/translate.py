import requests, uuid, json
def translate():
    
    # Add your key and endpoint
    key = "7b98bb936431474ebc069a334ac26494"
    endpoint = "https://api.cognitive.microsofttranslator.com"

# location, also known as region.
        # required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
    location = "westus"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['fr', 'it']
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        # location required if you're using a multi-service or regional (not global) resource.
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': "My abilities can be reduced to five features that I hope you take advantage of! If you want to know a class' prerequisites, ask me something like this, 'How can I take COSC 301'. You can get statistics on a computer science course by asking a question about a specific course. Possible job oppourtunites based on your course experice can be provided if you ask about work. I can help you make an acedmic advising appointment aswell, just ask me how! If you're unnsure what courses your experience qualifies you for, I can provide you with a list of courses you've completed the prerequisites for if you ask for help with course scheduling. I hope you found this helpful!!"
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))