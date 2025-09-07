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
