import urllib2
import string


def execute_command(query=""):
    args = string.split(query, ".")
    url = args[0]
    command = args[1]

    url = "https://graph.api.smartthings.com{url}".format(url=url)
    print url
    request = ""
    if command == "on":
        request = urllib2.Request(url, data='{"command":"on"}')
    else:
        request = urllib2.Request(url, data='{"command":"off"}')

    tokenFile = open("token.txt")
    token = tokenFile.read()
    tokenFile.close()
    request.add_header('Authorization', "Bearer %s" % token)
    request.add_header('Content-Type', 'application/json')
    request.get_method = lambda: 'PUT'

    opener = urllib2.build_opener(urllib2.HTTPHandler)
    opener.open(request)

    return
