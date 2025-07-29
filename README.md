# Play It Forward – Student & Parent Portal

A web-based portal designed for **Play It Forward**, a nonprofit music education organization, to help students, parents, and teachers easily access schedules, assignments, class resources, and updates.

This project extends the organization’s existing WordPress site with a dedicated, login-based portal for families and staff.

---

## 🚀 Current Features

- **Core Pages**  
  - Dashboard (quick student overview)  
  - Calendar (lesson and event schedule)  
  - Assignments (with due dates)  
  - Materials (dynamic resources, Google Drive + uploads)  
  - Profile (student info & contacts)  
  - Gallery (event photos)  

- **Teacher/Admin Dashboard (Planned)**  
  - Teachers can **post resources** (Google Drive links or small file uploads).  
  - Manage and update class materials without technical steps.  

- **Student Materials Page (Planned)**  
  - Students preview PDFs and videos directly in the portal.  
  - Links to Google Drive folders and other resources open in new tabs.  
  - Dynamic filtering by class and resource type.

---

## 🛠 Tech Stack

- **Backend:** Flask (Python)  
- **Frontend:** Tailwind CSS (latest version)  
- **Database:** Postgres (via Render)  
- **File Hosting:** Amazon S3 (for uploaded files)  
- **Third-Party Integration:**  
  - Google Drive (for primary resource sharing)  
  - NEON CRM (for student/family login & class data)

---

## 📂 Project Structure

playitforward-student-portal/
│
├── server.py # Flask app & routes (staging features planned)
├── models.py # SQLAlchemy models (Materials, etc.)
├── templates/ # All HTML templates (with Jinja2)
│ ├── layout.html
│ ├── dashboard.html
│ ├── calendar.html
│ ├── course-materials.html
│ ├── admin-dashboard.html
│ └── ...
├── static/
│ ├── css/main.css # Tailwind-compiled styles
│ ├── images/ # Static assets (gallery, logos)
│ └── icons/ # SVG icons
├── mock_data/ # Sample student JSON (for testing)
├── requirements.txt # Project dependencies
├── Procfile # For Render deployment
└── render.yaml # Staging + Production setup

---

## 🌐 Deployment

The portal is deployed on **Render** with separate environments:
- **Staging:** Used for testing features and getting feedback.  
- **Production:** (Planned) Will go live once features are finalized.

---

## 🎯 Next Steps

- Build out the **Admin Dashboard** for resource posting.  
- Connect to **NEON CRM** for real logins and student data.  
- Finalize **dynamic resource loading** (Drive + uploads) on the Materials page.  
- Test with teachers and staff before launch.

---

## 👩‍💻 About This Project

This portal is being built as part of my web development internship with Play It Forward.  
My role covers:
- Designing the **page structure and layouts** in Figma.  
- Developing the **frontend and backend** (Flask, Tailwind, Postgres, S3).  
- Integrating external systems (**Google Drive** and **NEON CRM**).  
- Managing deployment on **Render** for staging and production.

---

## 📸 Screenshots (Optional)

*(Add images of your Dashboard, Materials page, and Admin Dashboard here for recruiters/managers.)*

---

## 🔗 Live Site

- **Staging:** [https://playitforward-student-portal.onrender.com](https://playitforward-student-portal.onrender.com)  
*(Currently showing page structure; dynamic features in progress.)*
