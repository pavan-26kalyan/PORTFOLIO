from fastapi import FastAPI, Request, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime
from sqlalchemy.orm import Session
from database import engine, Base, get_db, initialize_database
from models import Skill, Project, Certification, ContactMessage


app = FastAPI()

# Configure static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# Configure Jinja2 templates
templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(
    request: Request,
    status: str = None,
    tech: str = None,
    db: Session = Depends(get_db)
):
    skills = db.query(Skill).order_by(Skill.id).all()
    projects = db.query(Project).order_by(Project.id).all()
    certifications = db.query(Certification).order_by(Certification.id).all()

    if tech:
        filtered_projects = []

        for project in projects:
            if tech.lower() in [technology.lower() for technology in project.technologies]:
                filtered_projects.append(project)

        projects = filtered_projects

    theme = request.cookies.get("theme", "light")

    context = {
        "request": request,
        "theme": theme,
        "skills": skills,
        "projects": projects,
        "certifications": certifications,
        "current_year": datetime.now().year,
        "status": status,
        "selected_tech": tech
    }

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context=context
    )


# Skills Data
# Projects Data
# Certifications Data
Base.metadata.create_all(bind=engine)
initialize_database()


@app.post("/contact")
async def contact(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    subject: str = Form(...),
    message: str = Form(...),
    db: Session = Depends(get_db)
):

    if not name.strip() or not email.strip() or not subject.strip() or not message.strip():
        return RedirectResponse(
            url="/?status=error#contact",
            status_code=303
        )

    contact_message = ContactMessage(
        name=name.strip(),
        email=email.strip(),
        subject=subject.strip(),
        message=message.strip()
    )

    db.add(contact_message)
    db.commit()

    return RedirectResponse(
        url="/?status=success#contact",
        status_code=303
    )


# Theme toggle endpoint
@app.post("/set-theme")
async def set_theme(request: Request):

    current_theme = request.cookies.get("theme", "light")

    if current_theme == "light":
        new_theme = "dark"
    else:
        new_theme = "light"

    referer = request.headers.get("referer")

    redirect_url = "/"

    if referer and referer.startswith("/") and not referer.startswith("//"):
        redirect_url = referer

    response = RedirectResponse(
        url=redirect_url,
        status_code=303
    )

    response.set_cookie(
        key="theme",
        value=new_theme,
        max_age=2592000,
        httponly=True,
        samesite="lax"
    )

    return response
