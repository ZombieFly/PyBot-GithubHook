class Handle():

    def star(self, body: dict) -> str:
        nos_stars = body["repository"]["stargazers_count"]
        starrer_username = body["sender"]["login"]
        repo_url = body["repository"]["html_url"]
        return f"User:{starrer_username}\n"\
                "Event:Star\n"\
            f"Repo:{repo_url}\n"\
            f"The Total Stars are {nos_stars}"

    #推送
    def push(self, body: dict) -> str:
        pusher = body['pusher']['name']
        repo_url = body["repository"]["html_url"]
        repo_name = body["repository"]["name"]
        commit_url = body['commits'][0]['url']
        commit = body['commits'][0]['message']
        added = body['commits'][0]['added']
        removed = body['commits'][0]['removed']
        modified = body['commits'][0]['modified']
        return f"User:{pusher}\n"\
                "Event:push\n"\
            f"Repo:{repo_url}\n"\
            f"Commit:{commit}"