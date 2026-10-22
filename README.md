

Readme · MD
# Python for Web 🐍🌐
 
A small multi-page web app built with **Flask** while working through Day 26 (Python Web) of [30 Days of Python](https://github.com/Asabeneh/30-Days-Of-Python), extended with all four of the day's exercises.
 
**Live demo:** https://YOUR-APP-NAME.onrender.com
 
> Hosted on Render's free tier, so the first visit after 15 minutes of inactivity may take about a minute to wake up.
 
## Features
 
- **Home / About / Post** – the tutorial pages, sharing one layout through Jinja2 template inheritance
- **Grade Calculator** – enter a subject and score to get a grade message, with server-side validation
- **BMI Calculator** – enter weight (kg) and height (cm) to calculate BMI and a health category
- **Task Manager** – add, view and delete tasks
- **Blog** – create, edit and delete posts, each with a unique ID
 
## Tech Stack
 
- Python 3, Flask
- Jinja2 templates, HTML, CSS
- Gunicorn (production server)
- Render (deployment)
 
## Project Structure
 
```
python_for_web/
├── app.py                 # Flask app and all routes
├── requirements.txt       # Dependencies
├── static/
│   └── css/
│       └── main.css       # Styles
└── templates/
    ├── layout.html        # Shared layout (nav + CSS)
    ├── home.html
    ├── about.html
    ├── post.html
    ├── result.html
    ├── grade.html
    ├── grade_result.html
    ├── bmi.html
    ├── bmi_result.html
    ├── tasks.html
    ├── blog.html
    └── post_form.html     # Shared by "new post" and "edit post"
```
 
## Routes
 
| Route | Method | Purpose |
|---|---|---|
| `/` | GET | Home page |
| `/about` | GET | About page |
| `/post` | GET | Tutorial form page |
| `/result` | POST | Show submitted tutorial form data |
| `/grade` | GET | Grade calculator form |
| `/grade/result` | POST | Calculate and show grade |
| `/bmi` | GET | BMI calculator form |
| `/bmi/result` | POST | Calculate and show BMI |
| `/tasks` | GET | List tasks |
| `/tasks/add` | POST | Add a task |
| `/tasks/delete/<index>` | POST | Delete a task |
| `/blog` | GET | List blog posts (newest first) |
| `/blog/new` | GET, POST | Show form / create a post |
| `/blog/<id>/edit` | GET, POST | Show pre-filled form / save changes |
| `/blog/<id>/delete` | POST | Delete a post |
 
## Run Locally
 
```bash
git clone https://github.com/Kho10-16/python_for_web.git
cd python_for_web
 
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux
 
pip install -r requirements.txt
python app.py
```
 
Then open http://127.0.0.1:5000
 
## Deployment (Render)
 
- **Build command:** `pip install -r requirements.txt`
- **Start command:** `gunicorn app:app`
 
Render redeploys automatically on every push to `main`.
 
## Known Limitations
 
- Tasks and blog posts are stored **in memory** (Python lists), so all data is lost when the server restarts or Render's free instance goes to sleep.
- The task manager deletes by list position, so deleting from a stale browser tab can remove the wrong task. The blog avoids this by using unique IDs.
 
## What I Learned
 
- The HTTP request/response cycle, and when to use GET vs POST
- Flask routing, including dynamic routes like `/blog/<int:post_id>/edit`
- Jinja2 templates: variables, loops, conditionals, filters and template inheritance
- Handling form data and validating it on the server
- The Post/Redirect/Get pattern to prevent duplicate form submissions
- Why unique IDs are safer than list positions
- Virtual environments, `requirements.txt`, and deploying with Gunicorn on Render
 
## Next Steps
 
- Persist data with a database (MongoDB, Day 27)
- Use unique IDs in the task manager too
- Show post excerpts on the blog list with a "read more" page
 
Claude is responding
