from flask import Flask, render_template, request, redirect, url_for
import json
import os
app = Flask(__name__)

POSTS_FILE= "posts.json"

def load_posts():
    """
    load blog posts from JSON file
    returns: list: A list of blog post dictionaries
    """
    if not os.path.exists(POSTS_FILE):
        #file doesnt exist, create an empty one
        with open(POSTS_FILE, "w") as f:
            json.dump([], f)
    try:
        with open(POSTS_FILE, "r") as f:
            return json.load(f)

    except json.JSONDecodeError:
        return []

def save_posts(posts):
    """
    Save the given list of blog posts back into the JSON file
    Args: posts(list): A list of blog post dictionaries
    """
    with open(POSTS_FILE, "w") as f:
        json.dump(posts, f, indent=4)

#________________________
#   Routes
@app.route("/")
def index():
    """
    Index route ("/")
    Display all blog posts by rendering index.html template.
    :return:
    """
    blog_posts = load_posts()
    return render_template("index.html", posts=blog_posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Add route ("/add")
    -GET: display a form for adding a new blog post.
    -POST: collects form data, creates a new post, saves it,
    and redirects back to the index page.
    :return:
    """
    if request.method == 'POST':
        posts = load_posts()
        new_id = max([post["id"]for post in posts],default=0) + 1
        # loads existing posts

        title = request.form.get("title")
        author = request.form.get("author")
        content = request.form.get("content")

        new_post ={
            "id": new_id,
            "title": title,
            "author": author,
            "content": content,
            "likes": 0
        }

        #append new post and save
        posts.append(new_post)
        save_posts(posts)

        #redirect to home page after adding
        return redirect(url_for("index"))

    #if GET request - show add.html form
    return render_template('add.html')


@app.route("/delete/<int:post_id>")
def delete(post_id):
    """
    Delete a blog post
    """
    posts = load_posts()

    # Filter out the post with the given ID
    posts = [post for post in posts if post["id"] != post_id]
    save_posts(posts)

    # Redirect back to home page
    return redirect(url_for("index"))


@app.route("/update/<int:post_id>", methods=["GET", "POST"])
def update(post_id):
    """
    Update route ("/update/<post_id>")
    - GET: Displays a form populated with the current post details.
    - POST: Updates the post in posts.json and redirects to index.
    """
    posts = load_posts()

    # Find the post with the given ID
    post = next((p for p in posts if p["id"] == post_id), None)

    if post is None:
        return "Post not found", 404

    if request.method == "POST":
        # Update post with form data
        post["title"] = request.form.get("title")
        post["author"] = request.form.get("author")
        post["content"] = request.form.get("content")

        # Save the updated list back to posts.json
        save_posts(posts)

        # Redirect to home page
        return redirect(url_for("index"))

    # GET request → render update form
    return render_template("update.html", post=post)

@app.route("/like/<int:post_id>")
def like(post_id):
    """
    like route ("/like/<post_id>")
    Increment the 'likes' value for the post with the given ID,
    then redirects back to the index page.
    :param post_id:
    :return:
    """

    posts = load_posts()

    #find the post and increment likes
    for post in posts:
        if post["id"] == post_id:
            post["likes"] = post.get("likes", 0) + 1
            break
    save_posts(posts)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
