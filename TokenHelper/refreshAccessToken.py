import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('SpotifyTokenDynamoDB')

# Method to refresh Spotify Access token as token expires after 3600 seconds
def get_new_access_token(oauth):
    refresh_token = load_dynamodb()
    new_token = oauth.refresh_access_token(refresh_token)
    update_dynamodb(new_token)
    access_token = new_token['access_token']
    return access_token

# Retrieve Spotify Refresh Token value
def load_dynamodb():
    response = table.scan()
    refresh_token = response['Items'][0]['refresh_token']
    return refresh_token

# Update DynamoDB entry with new Access token
def update_dynamodb(new_token):
    table.put_item(
        Item={
            'token': 'key',
            'access_token': new_token['access_token'],
            'token_type': new_token['token_type'],
            'expires_in': new_token['expires_in'],
            'scope': new_token['scope'],
            'expires_at': new_token['expires_at'],
            'refresh_token': new_token['refresh_token']
        })
