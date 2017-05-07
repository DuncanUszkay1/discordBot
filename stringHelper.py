import preferences as p
def strip_song_message(message):
    tokens = message.split(" ");
    i = 0
    t = len(tokens)
    while i < t and not is_a_song(tokens[i]):
        i = i + 1
    if i < t:
        return tokens[i]
    return False
def is_a_song(message):
    for a in p.stringBank.songMatchTokens:
        if(a in message):
            return True 
