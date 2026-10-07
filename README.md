# ProjectVault

ProjectVault is a runnable MVP of a student project repository: students can create profiles, submit and manage projects, discover projects by keyword/technology/category, like and rate approved projects, while administrators moderate submissions and reports.

## Included MVP flows

- Registration, login, logout, password hashing and session authentication
- Public homepage, explore/search/filter/sort, project detail pages and student profiles
- Student dashboard with views, likes, rating summary and moderation notifications
- Add/edit/delete projects with technology tags, GitHub/demo links and screenshot upload
- Moderation states: pending, approved, rejected, removed
- Likes and 1–5 star ratings
- Project reporting
- Admin dashboard for approve/reject, report closing and user suspension
- SQLite relational database with seeded demo projects
- Responsive UI without a frontend build step

## Run locally

```bash
cd ProjectVault
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
```

Open: http://127.0.0.1:8000

## Demo accounts

Student:
- Email: `student@example.com`
- Password: `demo123`

Admin:
- Email: `admin@example.com`
- Password: `admin123`

## Important production upgrades

This package is an MVP suitable for a college project/demo. Before public production use, move SQLite to PostgreSQL, put uploads on Cloudinary/S3, use environment-managed secrets, add CSRF protection, email verification/password reset, stronger URL/file validation, OAuth, pagination, test coverage, rate limiting, and deployment-specific hardening.

## Main structure

```text
ProjectVault/
├── app.py
├── requirements.txt
├── README.md
├── data/
├── static/
│   ├── app.js
│   ├── style.css
│   └── uploads/
└── templates/
    ├── base.html
    ├── home.html
    ├── explore.html
    ├── project.html
    ├── profile.html
    ├── dashboard.html
    ├── project_form.html
    ├── admin.html
    ├── login.html
    ├── register.html
    └── _project_card.html
```
