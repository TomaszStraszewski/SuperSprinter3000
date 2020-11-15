from flask import Flask, render_template, url_for, request, redirect
from in_memory_data import user_stories, get_new_id, get_story, add_story, update_story

app = Flask(__name__)


@app.route('/')
def index():
    table_headers = ["Id", "Story Title", "User Story", "Acceptance Criteria",
                     "Business Value", "Estimation", "Status"]
    user_story_keys = ["id", "title", "story", "criteria", "business", "estimation", "status"]

    return render_template("index.html", table_headers=table_headers,
                           user_stories=user_stories, user_story_keys=user_story_keys)
@app.route("/add")
def add_story_get():
    new_user_story =\
    {
        "id": None,
        "title": "",
        "story": "",
        "criteria": "",
        "business": None,
        "estimation": None
    }
    return render_template("updatestory.html", user_story=new_user_story, statuses=None )

@app.route('/update/<int:user_story_id>')
def update_story_get(user_story_id):
    user_story = get_story(user_story_id)

    if user_story is None:
        return redirect(url_for("index"))
    else:
        statuses = ["Planning", "TODO", "WIP", "QA", "DONE"]
        return render_template("updatestory.html", user_story=user_story, statuses=statuses)


@app.route('/update/post', methods=['POST'])
def add_story_post():
    new_user_story = dict(request.form)
    new_id = get_new_id()
    new_user_story['id'] = new_id
    new_user_story['status'] = "Planning"

    add_story(new_user_story)

    return redirect(url_for("index"))

@app.route('/update/post', methods=['POST'])
def update_story_post():
    updated_user_story = dict(request.form)
    updated_user_story["id"] = int(updated_user_story["id"])

    update_story(updated_user_story)

    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run()
