# My Blog Project

A simple blog application where users can read, write, and share posts.

## Features
- Create, edit, and delete blog posts  
- Responsive design  
- Comment system  
- Markdown support for posts  

## Getting Started

### Prerequisites
- [Python 3.10+]
- [pip]

### Installation
```bash
# Clone the repository
git clone  https://github.com/shenzyyshen/My_Blog.git

# Move into the project folder
cd my-flask-blog


# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Server runs on `http://localhost:5000`

## Project Structure

```
My_Blog/
├── app.py           # Flask routes and logic
├── posts.json       # Blog post storage
├── templates/       # HTML templates
├── static/          # CSS styles
└── requirements.txt
```

## Key Learnings

- Building Flask routes for CRUD operations
- Reading and writing JSON as a simple data store
- Jinja2 template inheritance with `extends` and `block`
- Handling form data with `request.form`