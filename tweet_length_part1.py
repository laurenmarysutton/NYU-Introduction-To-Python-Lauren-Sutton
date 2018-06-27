tweet = 'I am tweeting something incredibly interesting.'
print(tweet)
print('There are {} characters in this tweet.'.format(len(tweet)))
max_character_length = 240
if len(tweet) > max_character_length:
    print('This sentence is too long for a tweet!')
else:
    print('This sentence fits into a tweet.')
