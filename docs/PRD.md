# ProjectVault
## Product Requirements Document (PRD)

**Product Name:** ProjectVault  
**Product Type:** Web Application / Student Project Repository  
**Target Users:** College students, faculty members, recruiters, developers, and administrators  
**Version:** 1.0

---

## 1. Product Overview

ProjectVault is a centralized platform where college students can upload, document, showcase, and discover academic and personal projects.

Students often build useful projects during their academic journey, but these projects remain scattered across GitHub repositories, Google Drive folders, local systems, or college submissions. ProjectVault creates a structured portfolio and discovery platform where projects can be presented with documentation, screenshots, technology stacks, source-code links, live-demo links, and community ratings.

Users can search projects by technology, category, department, project type, or keywords. Other users can like and rate projects, while administrators moderate submitted content.

---

## 2. Problem Statement

Students develop multiple projects during college, but there is no organized platform within the college ecosystem to:

- Showcase completed projects.
- Discover projects created by other students.
- Search projects based on technologies such as React, Python, Java, AI/ML, Blockchain, etc.
- Access project documentation and source code.
- View screenshots and live demonstrations.
- Identify highly rated projects.
- Build a public technical portfolio.
- Prevent duplicate, spam, inappropriate, or low-quality project submissions.

ProjectVault solves this problem by creating a searchable and moderated student project repository.

---

## 3. Product Vision

Create a digital project ecosystem where students can:

**Build → Document → Showcase → Discover → Collaborate**

ProjectVault should eventually become a searchable knowledge base of student innovation across departments, colleges, technologies, and academic years.

---

## 4. Objectives

The primary objectives of ProjectVault are:

1. Allow students to showcase their projects professionally.
2. Create a centralized repository of college projects.
3. Allow users to discover projects based on technologies.
4. Encourage students to learn from projects developed by others.
5. Provide project visibility through likes and ratings.
6. Provide administrators with moderation tools.
7. Help students build a technical portfolio that can be shared with recruiters or faculty.
8. Encourage collaboration between students with similar technical interests.

---

# 5. Target Users

## 5.1 Student / Project Creator

A student who wants to upload and showcase a project.

Students should be able to:

- Create an account.
- Create a profile.
- Upload projects.
- Add project descriptions.
- Add documentation.
- Add technology stacks.
- Add GitHub links.
- Add live-demo links.
- Upload screenshots.
- Edit projects.
- Delete projects.
- View likes and ratings.

---

## 5.2 Student / Visitor

A student who wants to discover projects.

Users should be able to:

- Browse projects.
- Search projects.
- Filter projects by technology.
- View project details.
- Open GitHub repositories.
- Open demo links.
- Like projects.
- Rate projects.
- View student profiles.

---

## 5.3 Faculty

Faculty members may use ProjectVault to:

- Explore student projects.
- Identify innovative projects.
- Review student work.
- Discover projects related to a particular technology.
- Recommend good projects.
- Monitor projects created by students.

Faculty-specific features may be introduced in later versions.

---

## 5.4 Recruiter

Recruiters can use public ProjectVault profiles to:

- Explore student portfolios.
- View technical skills.
- View completed projects.
- Access GitHub repositories.
- View live demonstrations.

Recruiter accounts are not required for the MVP.

---

## 5.5 Administrator

Administrators manage the platform.

Administrators should be able to:

- View submitted projects.
- Approve projects.
- Reject projects.
- Remove inappropriate projects.
- Manage users.
- Manage reported projects.
- Manage technology tags.
- Monitor platform statistics.

---

# 6. User Roles

| Role | Permissions |
|---|---|
| Guest | Browse, search and view public projects |
| Student | Upload, edit, delete, like and rate projects |
| Faculty | Browse and review projects |
| Admin | Full moderation and management access |

---

# 7. Core Features

## 7.1 User Registration and Authentication

Users should be able to register using:

- Name
- Email address
- Password
- College
- Department
- Graduation year

Optional authentication:

- Google Sign-In
- GitHub Sign-In

### Functional Requirements

- User can register.
- User can log in.
- User can log out.
- Password should be securely encrypted.
- Email addresses should be unique.
- Users should be able to reset forgotten passwords.

---

# 8. Student Profile

Each registered student should have a public profile.

### Profile Information

- Profile photo
- Name
- College
- Department
- Graduation year
- Bio
- Skills
- GitHub profile
- LinkedIn profile
- Portfolio link

### Profile Statistics

Display:

- Number of uploaded projects
- Total project likes
- Average project rating

Example:

**Rahul Sharma**

Computer Science Engineering  
ABC Institute of Technology

Skills:

`React` `Node.js` `Python` `Machine Learning`

Projects: 8  
Total Likes: 420  
Average Rating: 4.5

---

# 9. Project Submission

Students should be able to upload projects using a structured project submission form.

## Required Fields

### Project Title

Example:

**AI-Based Plant Disease Detection**

### Short Description

A short project summary.

### Detailed Description

Full explanation of the project.

### Project Category

Examples:

- Web Development
- Mobile Application
- Artificial Intelligence
- Machine Learning
- Data Science
- Blockchain
- Cybersecurity
- IoT
- Robotics
- Cloud Computing
- Computer Vision
- Natural Language Processing
- Embedded Systems
- Other

### Tech Stack

Users should be able to add multiple technologies.

Example:

`React`  
`Node.js`  
`MongoDB`  
`Express.js`

### GitHub Repository

Example:

github.com/user/project

### Live Demo

Optional.

Example:

projectvault-demo.com

### Screenshots

Students should be able to upload multiple screenshots.

Recommended:

- Minimum: 1
- Maximum: 10

### Project Documentation

Students should be able to provide documentation using:

- Rich text editor

and optionally:

- Upload PDF documentation.

### Academic Information

Optional fields:

- College
- Department
- Academic year
- Semester
- Project type

Project types:

- Mini Project
- Major Project
- Final Year Project
- Hackathon Project
- Personal Project
- Research Project

---

# 10. Project Status

Every project should have a moderation status.

Possible statuses:

**Draft**

Project saved but not submitted.

**Pending**

Project submitted for admin moderation.

**Approved**

Project is visible publicly.

**Rejected**

Admin rejected the project.

**Removed**

Admin removed an existing project.

Example workflow:

Student uploads project

↓

Project Status: Pending

↓

Admin Reviews

↓

Approve / Reject

↓

Approved Project becomes publicly visible.

---

# 11. Project Detail Page

Each project should have a dedicated page.

Example URL:

`projectvault.com/project/ai-plant-disease-detection`

The page should contain:

### Project Header

- Project name
- Project creator
- College
- Category
- Creation date
- Rating
- Like count

### Project Description

Detailed project explanation.

### Tech Stack

Example:

`Python` `TensorFlow` `Flask` `OpenCV`

### Screenshots

Image gallery / carousel.

### Project Documentation

Full documentation.

### External Links

Buttons:

**View GitHub**

**Live Demo**

### Engagement

Users should be able to:

- Like project
- Rate project

---

# 12. Search System

Search is one of the main features of ProjectVault.

Users should be able to search using:

### Keyword Search

Example:

`Attendance system`

Possible results:

- Face Recognition Attendance System
- RFID Attendance Management
- Smart College Attendance System

---

# 13. Search by Technology

Users should be able to search projects based on technologies.

Example:

Search:

`React`

Results should include projects using React.

Technology examples:

- React
- Angular
- Vue
- Node.js
- Python
- Java
- C++
- Django
- Flask
- Spring Boot
- TensorFlow
- PyTorch
- MongoDB
- MySQL
- PostgreSQL
- Firebase
- AWS
- Docker
- Solidity
- Arduino

---

# 14. Filtering

Search results should support filters.

### Filters

**Technology**

Example:

React

**Category**

Example:

Artificial Intelligence

**Department**

Example:

Computer Science

**Project Type**

Example:

Final Year Project

**Academic Year**

Example:

2026

**Rating**

Example:

4 Stars & Above

**Sort By**

- Most Recent
- Most Liked
- Highest Rated
- Most Viewed

---

# 15. Like System

Logged-in users should be able to like projects.

Rules:

- One user can like a project only once.
- Users can remove their like.
- Project creators cannot artificially add multiple likes.
- Like count should update automatically.

Example:

❤️ **246 Likes**

---

# 16. Rating System

Users should be able to rate projects.

Rating scale:

**1–5 Stars**

Users can submit only one rating per project.

Example:

★★★★★

**4.6 / 5**

Based on 126 ratings.

Users should be allowed to update their rating.

Average rating:

Average Rating = Total Rating Score / Number of Ratings

---

# 17. Admin Dashboard

The admin dashboard should provide complete platform management.

Dashboard example:

**Total Users:** 4,520

**Total Projects:** 2,340

**Pending Projects:** 82

**Approved Projects:** 2,205

**Rejected Projects:** 53

---

# 18. Project Moderation

Admin should see a moderation queue.

Example:

| Project | Student | Category | Submitted | Status |
|---|---|---|---|---|
| AI Attendance | Rahul | AI | Today | Pending |
| Smart Farming | Priya | IoT | Today | Pending |
| Blockchain Voting | Aman | Blockchain | Yesterday | Pending |

Admin actions:

**View**

**Approve**

**Reject**

**Remove**

Admin should optionally provide rejection reasons.

Example:

> Project documentation is incomplete. Please add proper screenshots and GitHub repository details.

The student should then be able to edit and resubmit the project.

---

# 19. User Management

Admins should be able to:

- Search users.
- View profiles.
- Suspend users.
- Activate users.
- Delete users.
- Review uploaded projects.

Possible account statuses:

- Active
- Suspended
- Banned

---

# 20. Reporting System

Users should be able to report inappropriate projects.

Possible report reasons:

- Spam
- Copyright violation
- Fake project
- Inappropriate content
- Broken GitHub link
- Broken demo link
- Misleading information
- Other

Admin should receive reports in the moderation dashboard.

---

# 21. Homepage

The homepage should highlight project discovery.

Suggested structure:

## Navbar

ProjectVault Logo

Search Bar

Explore

Technologies

Login

Register

---

## Hero Section

### Discover Projects Built by Students

Explore innovative college projects, source code, documentation and technology stacks.

**Explore Projects**

**Upload Your Project**

---

## Trending Projects

Show highly liked or highly rated projects.

Example cards:

AI Resume Analyzer

Rating: 4.8

❤️ 540

Python • NLP • Flask

---

## Browse by Technology

Popular technology cards:

React

Python

Java

Machine Learning

Blockchain

Flutter

Node.js

IoT

---

## Latest Projects

Recently approved projects.

---

## Top Contributors

Students with popular projects.

---

# 22. Explore Page

The Explore page should provide project discovery.

Example:

### Explore Projects

Search:

`Search projects, technologies or keywords...`

Filters:

Technology | Category | Department | Rating

Cards should display:

- Screenshot
- Project name
- Creator
- Short description
- Tech stack
- Likes
- Rating

---

# 23. Project Card

Example:

**AI Resume Analyzer**

Automatically analyzes resumes using NLP.

`Python` `Flask` `NLP`

⭐ 4.8

❤️ 340

By Rahul Sharma

**View Project**

---

# 24. Student Dashboard

Students should have a personal dashboard.

Dashboard statistics:

**Total Projects**

**Total Likes**

**Average Rating**

**Total Views**

Sections:

### My Projects

| Project | Views | Likes | Rating | Status |
|---|---:|---:|---:|---|
| AI Resume Analyzer | 2,300 | 340 | 4.8 | Approved |
| Smart Attendance | 950 | 125 | 4.5 | Approved |
| Chat Application | — | — | — | Pending |

Actions:

- View
- Edit
- Delete

---

# 25. Notifications

Students should receive notifications for important actions.

Examples:

> Your project "AI Resume Analyzer" has been approved.

> Your project "Smart Farming System" was rejected.

> Your project received 100 likes.

> Your project received a new rating.

MVP can initially include only moderation notifications.

---

# 26. Recommended Technology Stack

## Frontend

Recommended:

**React.js**

or

**Next.js**

Other options:

- Tailwind CSS
- Material UI
- Bootstrap

Recommended combination:

**Next.js + Tailwind CSS**

---

## Backend

Recommended options:

**Node.js + Express.js**

Alternative:

**Django**

or

**Spring Boot**

Recommended:

**Node.js + Express.js**

---

## Database

Recommended:

**PostgreSQL**

Alternative:

**MongoDB**

For structured relationships such as users, projects, ratings, likes and technology tags, PostgreSQL is a strong choice.

---

## Image Storage

Possible services:

- Cloudinary
- AWS S3
- Firebase Storage

Recommended for a college project:

**Cloudinary**

---

## Authentication

Options:

- JWT Authentication
- NextAuth
- Firebase Authentication

---

## Deployment

Frontend:

- Vercel

Backend:

- Render
- Railway
- AWS

Database:

- Supabase
- Neon
- PostgreSQL

---

# 27. Suggested System Architecture

```text
                     ┌─────────────────┐
                     │     Users       │
                     └────────┬────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │   Web Frontend  │
                     │ React / Next.js │
                     └────────┬────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │   REST API      │
                     │ Node + Express  │
                     └────────┬────────┘
                              │
              ┌───────────────┼────────────────┐
              │               │                │
              ▼               ▼                ▼
       ┌────────────┐   ┌────────────┐   ┌────────────┐
       │ PostgreSQL │   │ Cloudinary │   │ GitHub URL │
       │ Database   │   │ Images     │   │ Demo Links │
       └────────────┘   └────────────┘   └────────────┘
```

---

# 28. Database Design

Major database tables:

## Users

```text
id
name
email
password_hash
profile_image
bio
college
department
graduation_year
github_url
linkedin_url
role
account_status
created_at
updated_at
```

---

## Projects

```text
id
user_id
title
slug
short_description
description
category_id
github_url
demo_url
project_type
academic_year
status
view_count
created_at
updated_at
```

---

## Technologies

```text
id
name
slug
```

Examples:

```text
React
Node.js
Python
TensorFlow
MongoDB
Flutter
```

---

## ProjectTechnologies

Many-to-many relationship:

```text
id
project_id
technology_id
```

---

## Screenshots

```text
id
project_id
image_url
display_order
created_at
```

---

## Likes

```text
id
user_id
project_id
created_at
```

Unique constraint:

```text
user_id + project_id
```

---

## Ratings

```text
id
user_id
project_id
rating
created_at
updated_at
```

Rating values:

```text
1
2
3
4
5
```

---

## Reports

```text
id
user_id
project_id
reason
description
status
created_at
```

---

## Notifications

```text
id
user_id
message
type
is_read
created_at
```

---

# 29. Important API Endpoints

## Authentication

```text
POST /api/auth/register

POST /api/auth/login

POST /api/auth/logout

GET /api/auth/me
```

---

## Projects

```text
GET /api/projects

GET /api/projects/:id

POST /api/projects

PUT /api/projects/:id

DELETE /api/projects/:id
```

---

## Search

```text
GET /api/projects/search?q=machine-learning
```

Filters:

```text
GET /api/projects?technology=react

GET /api/projects?category=ai

GET /api/projects?rating=4

GET /api/projects?sort=popular
```

---

## Likes

```text
POST /api/projects/:id/like

DELETE /api/projects/:id/like
```

---

## Ratings

```text
POST /api/projects/:id/rating

PUT /api/projects/:id/rating
```

---

## Admin

```text
GET /api/admin/projects/pending

PUT /api/admin/projects/:id/approve

PUT /api/admin/projects/:id/reject

DELETE /api/admin/projects/:id

GET /api/admin/users
```

---

# 30. User Flow – Upload Project

```text
Login
  ↓
Student Dashboard
  ↓
Add New Project
  ↓
Enter Project Information
  ↓
Add Tech Stack
  ↓
Upload Screenshots
  ↓
Add GitHub / Demo Links
  ↓
Submit
  ↓
Pending Moderation
  ↓
Admin Review
  ↓
Approved
  ↓
Project becomes Public
```

---

# 31. User Flow – Discover Project

```text
Homepage
  ↓
Search / Explore
  ↓
Apply Technology Filter
  ↓
View Project Cards
  ↓
Open Project
  ↓
Read Documentation
  ↓
View Screenshots
  ↓
GitHub / Demo
  ↓
Like / Rate Project
```

---

# 32. Admin Flow

```text
Admin Login
  ↓
Admin Dashboard
  ↓
Pending Projects
  ↓
Open Project
  ↓
Review Details
  ↓
Approve / Reject
  ↓
Student receives notification
```

---

# 33. Functional Requirements

The system must allow users to:

1. Register and login.
2. Create and update profiles.
3. Upload projects.
4. Edit their projects.
5. Delete their projects.
6. Upload screenshots.
7. Add GitHub links.
8. Add demo links.
9. Specify project technology stack.
10. Browse approved projects.
11. Search projects.
12. Filter projects by technology.
13. Like projects.
14. Rate projects.
15. View project ratings.
16. View student profiles.
17. Report projects.
18. Allow admins to approve projects.
19. Allow admins to reject projects.
20. Allow admins to manage users.

---

# 34. Non-Functional Requirements

## Performance

Normal API responses should ideally return within:

**< 500 ms**

Project pages should load quickly even when screenshots are present.

Images should be optimized.

---

## Security

The platform should provide:

- Password hashing.
- Secure authentication tokens.
- Role-based authorization.
- Input sanitization.
- Rate limiting.
- File upload restrictions.
- SQL injection protection.
- XSS protection.

Users should only be allowed to edit their own projects.

Admin APIs should only be available to administrators.

---

## Scalability

The system should support:

- Thousands of students.
- Tens of thousands of projects.
- Large numbers of likes and ratings.
- Increasing numbers of screenshots.

Pagination should therefore be implemented for project lists.

---

## Responsive Design

The application should support:

- Desktop
- Laptop
- Tablet
- Mobile

---

# 35. Validation Rules

### Project Title

Minimum:

```text
5 characters
```

Maximum:

```text
150 characters
```

### Short Description

Maximum:

```text
300 characters
```

### Screenshots

Allowed formats:

```text
JPEG
PNG
WebP
```

Suggested maximum size:

```text
5 MB per image
```

### GitHub URL

Must be a valid URL.

### Demo URL

Must be a valid URL.

### Rating

Must be:

```text
1 ≤ rating ≤ 5
```

---

# 36. MVP Scope

The first version should focus only on the essential features.

## MVP Features

### Authentication

- Register
- Login
- Logout

### Student

- Student profile
- Upload project
- Edit project
- Delete project
- Project dashboard

### Project

- Project description
- Technology stack
- GitHub link
- Demo link
- Screenshots

### Discovery

- Browse projects
- Search projects
- Filter by technology

### Engagement

- Likes
- Ratings

### Admin

- Admin dashboard
- Pending projects
- Approve project
- Reject project
- Delete project

---

# 37. Features Outside MVP

These can be introduced later.

### Project Comments

Users can discuss projects.

### Collaboration Requests

Example:

> Looking for a Flutter developer to contribute.

### Project Fork / Inspiration

Students can mark projects they used as inspiration.

### Follow Students

Users can follow project creators.

### Collections

Users can save projects into collections.

Example:

```text
AI Projects
Final Year Project Ideas
React Projects
```

### Faculty Verification

Faculty can verify selected projects.

Example:

**✓ Faculty Verified**

### Project Certificates

Generate shareable certificates or achievement badges.

### Leaderboard

Possible categories:

- Most Liked Student
- Most Viewed Project
- Highest Rated Project
- Top Contributor

---

# 38. Future AI Features

ProjectVault can later include AI functionality.

## AI Project Summary

AI automatically creates a short summary from documentation.

---

## AI Technology Detection

AI identifies technologies from:

- GitHub repository
- README
- Project description

---

## AI Recommendation System

Example:

If a student frequently views:

```text
React
Node.js
MongoDB
```

recommend MERN-stack projects.

---

## AI Project Quality Score

Projects could receive a quality score based on:

- Documentation quality
- Code availability
- Screenshots
- Demo availability
- Description quality

---

## AI Similar Project Detection

AI could identify projects that are highly similar.

Useful for:

- Duplicate detection.
- Plagiarism detection.
- Project discovery.

---

# 39. Analytics

Administrators should eventually be able to view:

### Platform Analytics

- Total users
- Total projects
- Approved projects
- Rejected projects
- Daily registrations
- Daily project submissions

### Technology Analytics

Example:

```text
Python             32%
React              24%
Java               17%
Machine Learning   15%
Flutter             12%
```

### Popular Categories

Example:

```text
AI / ML
Web Development
Mobile Development
IoT
Blockchain
```

---

# 40. Success Metrics

ProjectVault can measure success using:

### User Metrics

- Registered students
- Monthly active users
- Returning users

### Project Metrics

- Projects uploaded
- Approved projects
- Projects viewed
- GitHub link clicks
- Demo link clicks

### Engagement Metrics

- Likes per project
- Ratings per project
- Average session duration
- Searches performed

---

# 41. Example Project

## AI-Based Plant Disease Detection

**Created by:** Rahul Sharma

**Category:** Artificial Intelligence

**Project Type:** Final Year Project

### Description

An AI-powered web application capable of identifying plant diseases from uploaded leaf images using a trained convolutional neural network.

### Tech Stack

```text
Python
TensorFlow
OpenCV
Flask
React
```

### Project Links

**GitHub**

View Source Code

**Live Demo**

Try Project

### Screenshots

Application Dashboard

Image Upload Screen

Disease Detection Result

### Statistics

```text
Views: 2,450

Likes: 320

Rating: 4.7/5
```

---

# 42. Suggested Development Phases

## Phase 1 – Foundation

Develop:

- Database
- Authentication
- User roles
- Student profiles

---

## Phase 2 – Project Management

Develop:

- Project creation
- Editing
- Deletion
- Screenshot upload
- Technology tags
- GitHub/demo links

---

## Phase 3 – Discovery

Develop:

- Explore page
- Search
- Technology filters
- Category filters
- Sorting

---

## Phase 4 – Engagement

Develop:

- Likes
- Ratings
- View counter

---

## Phase 5 – Admin

Develop:

- Admin dashboard
- Project moderation
- User management
- Reporting

---

## Phase 6 – UI/UX & Deployment

Complete:

- Responsive design
- Performance optimization
- Security testing
- Deployment

---

# 43. Suggested Project Folder Structure

```text
projectvault/

├── frontend/
│   ├── components/
│   ├── pages/
│   ├── services/
│   ├── hooks/
│   ├── utils/
│   └── assets/
│
├── backend/
│   ├── controllers/
│   ├── routes/
│   ├── models/
│   ├── middleware/
│   ├── services/
│   ├── utils/
│   └── config/
│
├── database/
│   ├── migrations/
│   └── seeds/
│
└── README.md
```

---

# 44. Recommended Pages

The application should initially contain the following pages:

```text
/
Homepage

/explore
Explore Projects

/project/:slug
Project Details

/login
Login

/register
Registration

/profile/:username
Student Profile

/dashboard
Student Dashboard

/dashboard/projects
My Projects

/dashboard/project/new
Add Project

/dashboard/project/:id/edit
Edit Project

/admin
Admin Dashboard

/admin/projects
Project Moderation

/admin/users
User Management

/admin/reports
Reports
```

---

# 45. Key MVP Acceptance Criteria

The MVP will be considered successful when:

1. A student can successfully create an account.
2. A student can log in securely.
3. A student can create a project.
4. A student can add multiple technologies.
5. A student can upload screenshots.
6. A student can add GitHub and demo links.
7. A submitted project enters the moderation queue.
8. An administrator can approve or reject the project.
9. Approved projects appear publicly.
10. Users can search projects.
11. Users can filter projects by technology.
12. Logged-in users can like projects.
13. Logged-in users can rate projects.
14. Students can edit and delete their own projects.
15. Administrators can remove inappropriate projects.

---

# 46. Main Differentiating Feature

ProjectVault should not behave only like a file-uploading website.

The main value proposition should be:

> **A searchable portfolio and knowledge repository of student-built projects organized by technology, domain and academic background.**

Platforms like GitHub focus primarily on source code.

ProjectVault focuses on presenting the complete project:

```text
Project Idea
+
Documentation
+
Technology Stack
+
Screenshots
+
Source Code
+
Live Demo
+
Student Profile
+
Community Rating
```

This makes ProjectVault particularly useful for students looking for:

- Project inspiration
- Learning resources
- Final-year project references
- Technology-specific projects
- Portfolio visibility
- Collaboration opportunities