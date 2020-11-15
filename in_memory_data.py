user_stories = [{"id": 0,
                 "title": "Test Title 1",
                 "story": "User Story number One",
                 "criteria": "This works",
                 "business" : 1000,
                "estimation": "4",
                  "status": "TODO"},
                {"id": 1,
                 "title": "Test Title 2",
                 "story": "User Story number Two",
                 "criteria": "This works too",
                  "business": 5000,
                "estimation": 3,
                  "status": "DONE"}]

def get_new_id():
    tmp_id= 0
    for story in user_stories:
        if story['id'] > tmp_id:
            tmp_id = story['id']

    return tmp_id + 1

def add_story(user_story):
    global user_stories
    user_stories.append(user_story)

def get_story(user_story_id):
    for user_story in user_stories:
        if user_story["id"] == user_story_id:
            return user_story

    return None

def update_story(updated_user_story):
    global user_stories

    count = 0
    for user_story in user_stories:
        if user_story['id'] == updated_user_story['id']:
            user_stories.pop(count)
            user_stories.insert(count, updated_user_story)
            return
        count += 1

    add_story(updated_user_story)

