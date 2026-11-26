# Personal Portfolio Application

A personal portfolio website built using **Python, FastAPI, Jinja2, HTML, and CSS** to showcase my education, technical skills, projects, certifications, and contact information.

The application uses server-side rendering with Jinja2 templates and includes dynamic content rendering, technology-based project filtering, and cookie-based Light/Dark theme persistence.

## Features

- **Responsive Portfolio:** Personal portfolio with sections for About, Skills, Projects, Certifications, and Contact.
- **Jinja2 Template Inheritance:** Reusable templates using a base layout and individual section templates.
- **Dynamic Content Rendering:** Skills, projects, and certifications are dynamically displayed using Python data structures and Jinja2 loops.
- **Project Filtering:** Filter projects based on their technologies.
- **Light/Dark Theme:** Switch between light and dark themes.
- **Theme Persistence:** Selected theme is stored using HTTP cookies and persists across page refreshes.
- **Contact Form:** Contact form with server-side validation and submission status messages.
- **Static File Handling:** Serves CSS and profile images using FastAPI StaticFiles.

## Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend Framework | FastAPI |
| Frontend | HTML, CSS |
| Template Engine | Jinja2 |
| Server | Uvicorn |
| Version Control | Git, GitHub |

## Project Structure

```text
Personal_Portfolio_Application/
│
├── main.py
├── requirements.txt
├── .gitignore
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── images/
│       └── profile.jpg
│
├── templates/
│   ├── base.html
│   ├── index.html
│   │
│   └── sections/
│       ├── header.html
│       ├── hero.html
│       ├── about.html
│       ├── skills.html
│       ├── projects.html
│       ├── certifications.html
│       ├── contact.html
│       └── footer.html
│
└── venv/
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/MokshithRao/personal-portfolio-application.git
```

### 2. Navigate to the Project Directory

```bash
cd Personal_Portfolio_Application
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
uvicorn main:app --reload
```

### 7. Open in Browser

Visit:

```text
http://127.0.0.1:8000
```

## Application Sections

| Section | Description |
|---|---|
| Home | Introduction and profile information |
| About | Educational background and professional interests |
| Skills | Technical skills organised by categories |
| Projects | Project descriptions, technologies, and GitHub links |
| Certifications | Professional certifications and credentials |
| Contact | Contact information and contact form |

## Key Implementation Details

**Jinja2 Template Inheritance**

The application uses a shared `base.html` template to maintain a consistent layout. Individual sections are organised into reusable templates and included in the main page.

**Dynamic Project Rendering**

Project information is maintained in Python data structures and dynamically rendered using Jinja2 loops.

**Technology-Based Filtering**

Users can filter projects by technology using GET query parameters.

**Cookie-Based Theme Management**

The application uses FastAPI routes and HTTP cookies to switch between Light and Dark themes. The selected preference persists across browser refreshes without requiring JavaScript or localStorage.

## Learning Outcomes

Through this project, I practised:

- Building web applications using FastAPI.
- Integrating backend functionality with Jinja2 templates.
- Implementing server-side rendering.
- Organising reusable HTML templates.
- Handling HTTP GET and POST requests.
- Managing cookies and HTTP redirects.
- Implementing dynamic content and query-based filtering.
- Structuring and maintaining a Python web application.

## Author

**Mokshith Rao**

M.S. in Data Science – IIIT Hyderabad

**GitHub:** [Mokshith Rao](https://github.com/MokshithRao)

---

*Built as part of my Python Full Stack Development learning journey.*
