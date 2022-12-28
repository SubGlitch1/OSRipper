import ngrok

#This isnt the official ngrok libary. This is merely my way to parse out the tunnel host and ip from the ngrok api
#Subglitch1

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""
def get_tunnels():
# construct the api client
    with open('creds', 'r') as credfile:
        ngrok_auth=credfile.readline()
    client = ngrok.Client(ngrok_auth)

    # list all online tunnels
    for t in client.tunnels.list():
        with open('tmp.txt', 'w+') as tmp:
            out = str(t)
            tmp.write(out)
    with open('tmp.txt', 'r') as tmp:
        anan = tmp.readline()
        return find_between(anan, "tcp://", "', 'started_at':")
