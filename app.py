from __future__ import annotations

import hashlib
import os
import secrets
import sqlite3
import uuid
from datetime import datetime
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, File, Form, HTTPException, Request, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
UPLOAD_DIR = BASE_DIR / "static" / "uploads"
DB_PATH = DATA_DIR / "projectvault.db"
DATA_DIR.mkdir(exist_ok=True)
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI(title="ProjectVault", version="1.0.0")
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SESSION_SECRET", "projectvault-dev-secret-change-me"), max_age=60 * 60 * 24 * 7)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

CATEGORIES = [
    "Web Development", "Mobile Application", "Artificial Intelligence", "Machine Learning",
    "Data Science", "Blockchain", "Cybersecurity", "IoT", "Robotics", "Cloud Computing",
    "Computer Vision", "Natural Language Processing", "Embedded Systems", "Other",
]
PROJECT_TYPES = ["Mini Project", "Major Project", "Final Year Project", "Hackathon Project", "Personal Project", "Research Project"]


def db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def now() -> str:
    return datetime.utcnow().isoformat(timespec="seconds")


def slugify(value: str) -> str:
    import re
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return value or uuid.uuid4().hex[:8]


def hash_password(password: str, salt: Optional[str] = None) -> str:
    salt = salt or secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(salt), 160_000).hex()
    return f"{salt}${digest}"


def verify_password(password: str, stored: str) -> bool:
    try:
        salt, digest = stored.split("$", 1)
        return secrets.compare_digest(hash_password(password, salt).split("$", 1)[1], digest)
    except ValueError:
        return False


def current_user(request: Request):
    uid = request.session.get("user_id")
    if not uid:
        return None
    with db() as conn:
        return conn.execute("SELECT * FROM users WHERE id = ?", (uid,)).fetchone()


def flash(request: Request, message: str, kind: str = "info"):
    request.session["flash"] = {"message": message, "kind": kind}


def context(request: Request, **kwargs):
    return {
        "request": request,
        "user": current_user(request),
        "flash": request.session.pop("flash", None),
        "categories": CATEGORIES,
        "project_types": PROJECT_TYPES,
        **kwargs,
    }


def require_user(request: Request):
    user = current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Login required")
    return user


def require_admin(request: Request):
    user = require_user(request)
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return user


def init_db():
    with db() as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS users (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              email TEXT NOT NULL UNIQUE,
              password_hash TEXT NOT NULL,
              profile_image TEXT,
              bio TEXT,
              college TEXT,
              department TEXT,
              graduation_year INTEGER,
              skills TEXT,
              github_url TEXT,
              linkedin_url TEXT,
              portfolio_url TEXT,
              role TEXT NOT NULL DEFAULT 'student',
              account_status TEXT NOT NULL DEFAULT 'active',
              created_at TEXT NOT NULL,
              updated_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS projects (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
              title TEXT NOT NULL,
              slug TEXT NOT NULL UNIQUE,
              short_description TEXT NOT NULL,
              description TEXT NOT NULL,
              category TEXT NOT NULL,
              technologies TEXT NOT NULL,
              github_url TEXT,
              demo_url TEXT,
              project_type TEXT,
              academic_year INTEGER,
              screenshot TEXT,
              status TEXT NOT NULL DEFAULT 'pending',
              rejection_reason TEXT,
              view_count INTEGER NOT NULL DEFAULT 0,
              created_at TEXT NOT NULL,
              updated_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS likes (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
              project_id INTEGER NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
              created_at TEXT NOT NULL,
              UNIQUE(user_id, project_id)
            );
            CREATE TABLE IF NOT EXISTS ratings (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
              project_id INTEGER NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
              rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
              created_at TEXT NOT NULL,
              updated_at TEXT NOT NULL,
              UNIQUE(user_id, project_id)
            );
            CREATE TABLE IF NOT EXISTS reports (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
              project_id INTEGER NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
              reason TEXT NOT NULL,
              description TEXT,
              status TEXT NOT NULL DEFAULT 'open',
              created_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS notifications (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
              message TEXT NOT NULL,
              type TEXT,
              is_read INTEGER NOT NULL DEFAULT 0,
              created_at TEXT NOT NULL
            );
            """
        )

        if conn.execute("SELECT COUNT(*) FROM users").fetchone()[0] == 0:
            created = now()
            conn.execute(
                "INSERT INTO users(name,email,password_hash,bio,college,department,graduation_year,skills,github_url,role,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                ("Rahul Sharma", "student@example.com", hash_password("demo123"), "CSE student building practical AI and web products.", "ABC Institute of Technology", "Computer Science Engineering", 2027, "React, Python, Machine Learning, Flask", "https://github.com/", "student", created, created),
            )
            conn.execute(
                "INSERT INTO users(name,email,password_hash,bio,college,department,graduation_year,skills,role,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
                ("ProjectVault Admin", "admin@example.com", hash_password("admin123"), "Platform administrator", "ProjectVault", "Administration", 2026, "Moderation, Analytics", "admin", created, created),
            )
            uid = conn.execute("SELECT id FROM users WHERE email='student@example.com'").fetchone()[0]
            samples = [
                ("AI Resume Analyzer", "Analyze resumes and highlight relevant skills using NLP.", "A student-focused resume analysis tool that extracts skills, identifies missing keywords, and generates a structured summary for recruiters and applicants.", "Artificial Intelligence", "Python,NLP,FastAPI,React", "Final Year Project", 2026),
                ("Smart Attendance System", "Face-recognition attendance with real-time class reports.", "Computer vision attendance project with student registration, face matching, attendance logs, and teacher-facing reports.", "Computer Vision", "Python,OpenCV,SQLite", "Major Project", 2026),
                ("Blockchain Voting", "Transparent campus election prototype built on smart contracts.", "A decentralized voting prototype for college clubs with auditable vote records and simple wallet-based participation.", "Blockchain", "Solidity,React,Ethers.js", "Hackathon Project", 2025),
                ("IoT Smart Farming", "Soil and climate monitoring dashboard for smarter irrigation.", "An IoT project combining sensor readings with a dashboard to help students explore automated irrigation and farm monitoring.", "IoT", "Arduino,Python,IoT", "Major Project", 2026),
                ("Campus Marketplace", "A safe student-only marketplace for books and electronics.", "A responsive web marketplace allowing verified students to list, search, and contact sellers for used campus items.", "Web Development", "JavaScript,Node.js,PostgreSQL", "Mini Project", 2025),
                ("Plant Disease Detection", "CNN-powered plant leaf disease classifier.", "Upload a plant leaf image and receive a predicted disease class with confidence and basic treatment guidance.", "Machine Learning", "Python,TensorFlow,OpenCV", "Final Year Project", 2026),
            ]
            for idx, p in enumerate(samples):
                title, short, desc, cat, tech, ptype, year = p
                conn.execute(
                    "INSERT INTO projects(user_id,title,slug,short_description,description,category,technologies,github_url,demo_url,project_type,academic_year,status,view_count,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (uid, title, slugify(title), short, desc, cat, tech, "https://github.com/", "https://example.com", ptype, year, "approved" if idx < 5 else "pending", 2800 - idx * 310, created, created),
                )
            for pid in range(1, 6):
                # Seed aggregates from distinct pseudo users are represented by current counters through actual demo rows below.
                pass
        conn.commit()


init_db()


def project_query(where="", params=(), order="p.created_at DESC"):
    sql = f"""
      SELECT p.*, u.name AS creator_name, u.department AS creator_department, u.college AS creator_college,
             (SELECT COUNT(*) FROM likes l WHERE l.project_id=p.id) AS like_count,
             COALESCE((SELECT ROUND(AVG(r.rating),1) FROM ratings r WHERE r.project_id=p.id),0) AS avg_rating,
             (SELECT COUNT(*) FROM ratings r2 WHERE r2.project_id=p.id) AS rating_count
      FROM projects p JOIN users u ON u.id=p.user_id
      {where}
      ORDER BY {order}
    """
    with db() as conn:
        return conn.execute(sql, params).fetchall()


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    projects = project_query("WHERE p.status='approved'", (), "p.view_count DESC, p.created_at DESC")[:6]
    latest = project_query("WHERE p.status='approved'", (), "p.created_at DESC")[:4]
    with db() as conn:
        contributors = conn.execute("""
            SELECT u.id,u.name,u.department,COUNT(p.id) projects_count,
                   COALESCE(SUM((SELECT COUNT(*) FROM likes l WHERE l.project_id=p.id)),0) likes_count
            FROM users u LEFT JOIN projects p ON p.user_id=u.id AND p.status='approved'
            WHERE u.role='student' GROUP BY u.id ORDER BY likes_count DESC, projects_count DESC LIMIT 4
        """).fetchall()
    return templates.TemplateResponse(request, "home.html", context(request, projects=projects, latest=latest, contributors=contributors))


@app.get("/explore", response_class=HTMLResponse)
def explore(request: Request, q: str = "", technology: str = "", category: str = "", sort: str = "recent"):
    clauses = ["p.status='approved'"]
    params = []
    if q:
        clauses.append("(p.title LIKE ? OR p.short_description LIKE ? OR p.description LIKE ? OR p.technologies LIKE ?)")
        like = f"%{q}%"
        params += [like, like, like, like]
    if technology:
        clauses.append("p.technologies LIKE ?")
        params.append(f"%{technology}%")
    if category:
        clauses.append("p.category = ?")
        params.append(category)
    order_map = {
        "recent": "p.created_at DESC", "views": "p.view_count DESC",
        "liked": "like_count DESC", "rated": "avg_rating DESC, rating_count DESC",
    }
    projects = project_query("WHERE " + " AND ".join(clauses), tuple(params), order_map.get(sort, order_map["recent"]))
    return templates.TemplateResponse(request, "explore.html", context(request, projects=projects, q=q, technology=technology, category=category, sort=sort))


@app.get("/project/{slug}", response_class=HTMLResponse)
def project_detail(request: Request, slug: str):
    with db() as conn:
        p = conn.execute("""
          SELECT p.*,u.name creator_name,u.college creator_college,u.department creator_department,u.id creator_id,
                 (SELECT COUNT(*) FROM likes l WHERE l.project_id=p.id) like_count,
                 COALESCE((SELECT ROUND(AVG(r.rating),1) FROM ratings r WHERE r.project_id=p.id),0) avg_rating,
                 (SELECT COUNT(*) FROM ratings r2 WHERE r2.project_id=p.id) rating_count
          FROM projects p JOIN users u ON u.id=p.user_id WHERE p.slug=?
        """, (slug,)).fetchone()
        if not p or (p["status"] != "approved" and (not current_user(request) or current_user(request)["id"] != p["user_id"] and current_user(request)["role"] != "admin")):
            raise HTTPException(404)
        conn.execute("UPDATE projects SET view_count=view_count+1 WHERE id=?", (p["id"],))
        conn.commit()
        user = current_user(request)
        liked = False
        my_rating = 0
        if user:
            liked = bool(conn.execute("SELECT 1 FROM likes WHERE user_id=? AND project_id=?", (user["id"], p["id"])).fetchone())
            rr = conn.execute("SELECT rating FROM ratings WHERE user_id=? AND project_id=?", (user["id"], p["id"])).fetchone()
            my_rating = rr[0] if rr else 0
    return templates.TemplateResponse(request, "project.html", context(request, project=p, liked=liked, my_rating=my_rating))


@app.post("/project/{project_id}/like")
def toggle_like(request: Request, project_id: int):
    user = require_user(request)
    with db() as conn:
        p = conn.execute("SELECT slug FROM projects WHERE id=? AND status='approved'", (project_id,)).fetchone()
        if not p: raise HTTPException(404)
        exists = conn.execute("SELECT id FROM likes WHERE user_id=? AND project_id=?", (user["id"], project_id)).fetchone()
        if exists: conn.execute("DELETE FROM likes WHERE id=?", (exists["id"],))
        else: conn.execute("INSERT INTO likes(user_id,project_id,created_at) VALUES(?,?,?)", (user["id"], project_id, now()))
        conn.commit()
    return RedirectResponse(f"/project/{p['slug']}", status_code=303)


@app.post("/project/{project_id}/rating")
def rate_project(request: Request, project_id: int, rating: int = Form(...)):
    user = require_user(request)
    if rating not in range(1,6): raise HTTPException(400, "Rating must be 1-5")
    with db() as conn:
        p = conn.execute("SELECT slug FROM projects WHERE id=? AND status='approved'", (project_id,)).fetchone()
        if not p: raise HTTPException(404)
        existing = conn.execute("SELECT id FROM ratings WHERE user_id=? AND project_id=?", (user["id"], project_id)).fetchone()
        if existing:
            conn.execute("UPDATE ratings SET rating=?,updated_at=? WHERE id=?", (rating, now(), existing["id"]))
        else:
            conn.execute("INSERT INTO ratings(user_id,project_id,rating,created_at,updated_at) VALUES(?,?,?,?,?)", (user["id"], project_id, rating, now(), now()))
        conn.commit()
    flash(request, "Rating saved.", "success")
    return RedirectResponse(f"/project/{p['slug']}", status_code=303)


@app.post("/project/{project_id}/report")
def report_project(request: Request, project_id: int, reason: str = Form(...), description: str = Form("")):
    user = require_user(request)
    with db() as conn:
        p = conn.execute("SELECT slug FROM projects WHERE id=?", (project_id,)).fetchone()
        if not p: raise HTTPException(404)
        conn.execute("INSERT INTO reports(user_id,project_id,reason,description,created_at) VALUES(?,?,?,?,?)", (user["id"], project_id, reason, description[:500], now()))
        conn.commit()
    flash(request, "Report submitted for admin review.", "success")
    return RedirectResponse(f"/project/{p['slug']}", status_code=303)


@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(request, "login.html", context(request))


@app.post("/login")
def login(request: Request, email: str = Form(...), password: str = Form(...)):
    with db() as conn:
        user = conn.execute("SELECT * FROM users WHERE lower(email)=lower(?)", (email.strip(),)).fetchone()
    if not user or not verify_password(password, user["password_hash"]) or user["account_status"] != "active":
        flash(request, "Invalid email/password or inactive account.", "error")
        return RedirectResponse("/login", status_code=303)
    request.session["user_id"] = user["id"]
    flash(request, f"Welcome back, {user['name']}!", "success")
    return RedirectResponse("/admin" if user["role"] == "admin" else "/dashboard", status_code=303)


@app.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse(request, "register.html", context(request))


@app.post("/register")
def register(request: Request, name: str = Form(...), email: str = Form(...), password: str = Form(...), college: str = Form(...), department: str = Form(...), graduation_year: int = Form(...)):
    if len(password) < 6:
        flash(request, "Password must be at least 6 characters.", "error")
        return RedirectResponse("/register", status_code=303)
    try:
        with db() as conn:
            cur = conn.execute("INSERT INTO users(name,email,password_hash,college,department,graduation_year,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?)", (name.strip(), email.strip().lower(), hash_password(password), college.strip(), department.strip(), graduation_year, now(), now()))
            conn.commit()
            request.session["user_id"] = cur.lastrowid
    except sqlite3.IntegrityError:
        flash(request, "An account with that email already exists.", "error")
        return RedirectResponse("/register", status_code=303)
    flash(request, "Account created successfully.", "success")
    return RedirectResponse("/dashboard", status_code=303)


@app.post("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/", status_code=303)


@app.get("/profile/{user_id}", response_class=HTMLResponse)
def profile(request: Request, user_id: int):
    with db() as conn:
        profile_user = conn.execute("SELECT * FROM users WHERE id=?", (user_id,)).fetchone()
        if not profile_user: raise HTTPException(404)
        stats = conn.execute("""
          SELECT COUNT(p.id) projects_count,
                 COALESCE(SUM((SELECT COUNT(*) FROM likes l WHERE l.project_id=p.id)),0) total_likes,
                 COALESCE(ROUND(AVG((SELECT AVG(r.rating) FROM ratings r WHERE r.project_id=p.id)),1),0) avg_rating
          FROM projects p WHERE p.user_id=? AND p.status='approved'
        """, (user_id,)).fetchone()
    projects = project_query("WHERE p.status='approved' AND p.user_id=?", (user_id,))
    return templates.TemplateResponse(request, "profile.html", context(request, profile_user=profile_user, stats=stats, projects=projects))


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    user = require_user(request)
    if user["role"] == "admin": return RedirectResponse("/admin", status_code=303)
    with db() as conn:
        projects = conn.execute("""
          SELECT p.*,
                 (SELECT COUNT(*) FROM likes l WHERE l.project_id=p.id) like_count,
                 COALESCE((SELECT ROUND(AVG(r.rating),1) FROM ratings r WHERE r.project_id=p.id),0) avg_rating
          FROM projects p WHERE p.user_id=? ORDER BY p.created_at DESC
        """, (user["id"],)).fetchall()
        stats = conn.execute("""
          SELECT COUNT(*) total_projects, COALESCE(SUM(view_count),0) total_views,
                 COALESCE(SUM((SELECT COUNT(*) FROM likes l WHERE l.project_id=p.id)),0) total_likes,
                 COALESCE(ROUND(AVG((SELECT AVG(r.rating) FROM ratings r WHERE r.project_id=p.id)),1),0) avg_rating
          FROM projects p WHERE p.user_id=?
        """, (user["id"],)).fetchone()
        notifications = conn.execute("SELECT * FROM notifications WHERE user_id=? ORDER BY created_at DESC LIMIT 8", (user["id"],)).fetchall()
    return templates.TemplateResponse(request, "dashboard.html", context(request, projects=projects, stats=stats, notifications=notifications))


@app.get("/dashboard/project/new", response_class=HTMLResponse)
def new_project_page(request: Request):
    require_user(request)
    return templates.TemplateResponse(request, "project_form.html", context(request, project=None, page_title="Add Project"))


def save_upload(file: Optional[UploadFile]):
    if not file or not file.filename:
        return None
    ext = Path(file.filename).suffix.lower()
    if ext not in {".jpg", ".jpeg", ".png", ".webp"}:
        raise HTTPException(400, "Screenshot must be JPEG, PNG, or WebP")
    contents = file.file.read(5 * 1024 * 1024 + 1)
    if len(contents) > 5 * 1024 * 1024:
        raise HTTPException(400, "Screenshot must be 5 MB or less")
    name = f"{uuid.uuid4().hex}{ext}"
    (UPLOAD_DIR / name).write_bytes(contents)
    return f"/static/uploads/{name}"


@app.post("/dashboard/project/new")
def create_project(
    request: Request,
    title: str = Form(...), short_description: str = Form(...), description: str = Form(...),
    category: str = Form(...), technologies: str = Form(...), github_url: str = Form(""), demo_url: str = Form(""),
    project_type: str = Form(""), academic_year: Optional[int] = Form(None), screenshot: Optional[UploadFile] = File(None),
):
    user = require_user(request)
    if len(title.strip()) < 5 or len(title.strip()) > 150 or len(short_description) > 300:
        flash(request, "Check title and short description length.", "error")
        return RedirectResponse("/dashboard/project/new", status_code=303)
    shot = save_upload(screenshot)
    base = slugify(title)
    slug = base
    with db() as conn:
        n = 2
        while conn.execute("SELECT 1 FROM projects WHERE slug=?", (slug,)).fetchone():
            slug = f"{base}-{n}"; n += 1
        conn.execute("""
          INSERT INTO projects(user_id,title,slug,short_description,description,category,technologies,github_url,demo_url,project_type,academic_year,screenshot,status,created_at,updated_at)
          VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (user["id"], title.strip(), slug, short_description.strip(), description.strip(), category, technologies.strip(), github_url.strip(), demo_url.strip(), project_type, academic_year, shot, "pending", now(), now()))
        conn.commit()
    flash(request, "Project submitted and is pending moderation.", "success")
    return RedirectResponse("/dashboard", status_code=303)


@app.get("/dashboard/project/{project_id}/edit", response_class=HTMLResponse)
def edit_project_page(request: Request, project_id: int):
    user = require_user(request)
    with db() as conn:
        p = conn.execute("SELECT * FROM projects WHERE id=? AND user_id=?", (project_id, user["id"])).fetchone()
    if not p: raise HTTPException(404)
    return templates.TemplateResponse(request, "project_form.html", context(request, project=p, page_title="Edit Project"))


@app.post("/dashboard/project/{project_id}/edit")
def edit_project(
    request: Request, project_id: int,
    title: str = Form(...), short_description: str = Form(...), description: str = Form(...),
    category: str = Form(...), technologies: str = Form(...), github_url: str = Form(""), demo_url: str = Form(""),
    project_type: str = Form(""), academic_year: Optional[int] = Form(None), screenshot: Optional[UploadFile] = File(None),
):
    user = require_user(request)
    shot = save_upload(screenshot)
    with db() as conn:
        p = conn.execute("SELECT * FROM projects WHERE id=? AND user_id=?", (project_id, user["id"])).fetchone()
        if not p: raise HTTPException(404)
        shot = shot or p["screenshot"]
        conn.execute("""
          UPDATE projects SET title=?,short_description=?,description=?,category=?,technologies=?,github_url=?,demo_url=?,project_type=?,academic_year=?,screenshot=?,status='pending',rejection_reason=NULL,updated_at=? WHERE id=?
        """, (title.strip(), short_description.strip(), description.strip(), category, technologies.strip(), github_url.strip(), demo_url.strip(), project_type, academic_year, shot, now(), project_id))
        conn.commit()
    flash(request, "Project updated and sent for moderation again.", "success")
    return RedirectResponse("/dashboard", status_code=303)


@app.post("/dashboard/project/{project_id}/delete")
def delete_project(request: Request, project_id: int):
    user = require_user(request)
    with db() as conn:
        conn.execute("DELETE FROM projects WHERE id=? AND user_id=?", (project_id, user["id"]))
        conn.commit()
    flash(request, "Project deleted.", "success")
    return RedirectResponse("/dashboard", status_code=303)


@app.get("/admin", response_class=HTMLResponse)
def admin_dashboard(request: Request):
    require_admin(request)
    with db() as conn:
        stats = conn.execute("""
          SELECT (SELECT COUNT(*) FROM users) users,
                 (SELECT COUNT(*) FROM projects) projects,
                 (SELECT COUNT(*) FROM projects WHERE status='pending') pending,
                 (SELECT COUNT(*) FROM projects WHERE status='approved') approved,
                 (SELECT COUNT(*) FROM projects WHERE status='rejected') rejected,
                 (SELECT COUNT(*) FROM reports WHERE status='open') open_reports
        """).fetchone()
        pending = conn.execute("SELECT p.*,u.name creator_name FROM projects p JOIN users u ON u.id=p.user_id WHERE p.status='pending' ORDER BY p.created_at").fetchall()
        reports = conn.execute("""SELECT r.*,p.title project_title,p.slug,u.name reporter_name FROM reports r JOIN projects p ON p.id=r.project_id JOIN users u ON u.id=r.user_id WHERE r.status='open' ORDER BY r.created_at DESC LIMIT 10""").fetchall()
        users = conn.execute("SELECT * FROM users ORDER BY created_at DESC LIMIT 10").fetchall()
    return templates.TemplateResponse(request, "admin.html", context(request, stats=stats, pending=pending, reports=reports, users=users))


@app.post("/admin/project/{project_id}/{action}")
def moderate_project(request: Request, project_id: int, action: str, reason: str = Form("")):
    require_admin(request)
    if action not in {"approve", "reject", "remove"}: raise HTTPException(400)
    with db() as conn:
        p = conn.execute("SELECT * FROM projects WHERE id=?", (project_id,)).fetchone()
        if not p: raise HTTPException(404)
        status = {"approve": "approved", "reject": "rejected", "remove": "removed"}[action]
        conn.execute("UPDATE projects SET status=?,rejection_reason=?,updated_at=? WHERE id=?", (status, reason.strip() if status == "rejected" else None, now(), project_id))
        message = f'Your project "{p["title"]}" has been {status}.'
        if status == "rejected" and reason.strip(): message += f" Reason: {reason.strip()}"
        conn.execute("INSERT INTO notifications(user_id,message,type,created_at) VALUES(?,?,?,?)", (p["user_id"], message, "moderation", now()))
        conn.commit()
    flash(request, f"Project {status}.", "success")
    return RedirectResponse("/admin", status_code=303)


@app.post("/admin/report/{report_id}/close")
def close_report(request: Request, report_id: int):
    require_admin(request)
    with db() as conn:
        conn.execute("UPDATE reports SET status='closed' WHERE id=?", (report_id,))
        conn.commit()
    flash(request, "Report closed.", "success")
    return RedirectResponse("/admin", status_code=303)


@app.post("/admin/user/{user_id}/toggle")
def toggle_user(request: Request, user_id: int):
    admin = require_admin(request)
    if admin["id"] == user_id:
        flash(request, "You cannot suspend your own admin account.", "error")
        return RedirectResponse("/admin", status_code=303)
    with db() as conn:
        u = conn.execute("SELECT account_status FROM users WHERE id=?", (user_id,)).fetchone()
        if not u: raise HTTPException(404)
        new = "suspended" if u["account_status"] == "active" else "active"
        conn.execute("UPDATE users SET account_status=?,updated_at=? WHERE id=?", (new, now(), user_id))
        conn.commit()
    flash(request, f"User is now {new}.", "success")
    return RedirectResponse("/admin", status_code=303)


@app.get("/health")
def health():
    return {"status": "ok", "app": "ProjectVault"}
