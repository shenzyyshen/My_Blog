# Dev Notes

## Flask Blog
- `app.py` handles routes: home, add post, update post, delete post
- Posts are stored in `posts.json` — loaded on each request
- `post.json` is a single post template/example

## JSON Storage
- `posts.json` is read and written on each operation
- Each post has: id, author, title, content
- IDs are auto-incremented by taking max(id) + 1

## Flask Templates
- Jinja2 templating: `{{ variable }}` for output, `{% for %}` for loops
- `templates/base.html` provides the shared layout
- Child templates use `{% extends %}` and `{% block %}` to fill in content

## Routing
- `GET /` — shows all posts
- `POST /add` — creates a new post from form data
- `GET/POST /update/<id>` — shows form pre-filled with post data, saves on POST
- `POST /delete/<id>` — removes post by ID from JSON and redirects
