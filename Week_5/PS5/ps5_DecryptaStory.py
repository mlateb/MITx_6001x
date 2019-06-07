def decrypt_story():
    
    strory = get_story_string()
    storyCipher = CiphertextMessage(strory)
    storyDecr = storyCipher.decrypt_message()
    return storyDecr
