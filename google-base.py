def google_search(query):
    res = service.cse().list(q=query, cx='65621b84ec2384292').execute()
    return res['items']
