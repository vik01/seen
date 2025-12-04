# CLAUDE.md - AI Assistant Development Guide

**Last Updated:** 2025-12-04
**Project:** Seen - Student Project Showcase Platform
**Tagline:** "Are you unseen or are you on seen."

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Technology Stack](#technology-stack)
3. [Repository Structure](#repository-structure)
4. [Development Environment Setup](#development-environment-setup)
5. [Key Conventions and Patterns](#key-conventions-and-patterns)
6. [Application Architecture](#application-architecture)
7. [Current Development Status](#current-development-status)
8. [Working with This Codebase](#working-with-this-codebase)
9. [Common Development Tasks](#common-development-tasks)
10. [Important Considerations](#important-considerations)
11. [Next Steps for Development](#next-steps-for-development)

---

## Project Overview

**Seen** is a Django-based social platform designed for students to showcase their projects, connect with communities, and gain recognition for their work. The platform enables users to:

- Create and manage project portfolios
- Share posts and updates with the community
- Join and participate in communities
- Display certifications and achievements
- Connect with other students and collaborate
- Integrate projects from external platforms (GitHub, etc.)

**Current Phase:** Early development / Prototype stage with comprehensive UI design but minimal backend implementation.

---

## Technology Stack

### Backend
- **Framework:** Django 5.2.7
- **Language:** Python 3.11.14
- **Database:** SQLite3 (development)
- **Server:** WSGI (production) / ASGI (async support)

### Data Analysis Libraries (Installed but Currently Unused)
- pandas - Data manipulation
- numpy - Numerical computing
- seaborn - Statistical visualization
- matplotlib - Plotting

### Frontend
- **HTML5** with embedded CSS and JavaScript
- **No external frameworks** - Pure vanilla JavaScript and custom CSS
- **Design System:** Navy blue gradient theme (#001f3f, #003366)
- **Approach:** Responsive, mobile-first design with card-based layouts

### Dependencies
See `requirements.txt`:
```
pandas
numpy
seaborn
matplotlib
django
```

---

## Repository Structure

```
/home/user/seen/
├── .git/                           # Git repository
├── .gitignore                      # Ignores: /set_up, /seenenv, /myseen
├── README.md                       # Basic setup instructions
├── requirements.txt                # Python dependencies
├── pages/                          # Prototype HTML files (not active)
│   ├── .gitignore
│   ├── seen_platform copy.html
│   ├── seen_profile_page_stage_1.html
│   └── seen_profile_page_stage_4.html
└── seen/                          # Django project root
    ├── db.sqlite3                 # SQLite database (128KB)
    ├── manage.py                  # Django CLI entry point
    ├── seen/                      # Project configuration
    │   ├── __init__.py
    │   ├── asgi.py               # ASGI server config
    │   ├── settings.py           # Django settings
    │   ├── urls.py               # Root URL routing
    │   └── wsgi.py               # WSGI server config
    └── seen_app/                 # Main Django application
        ├── __init__.py
        ├── admin.py              # Admin panel config
        ├── apps.py               # App configuration
        ├── models.py             # Database models (EMPTY)
        ├── tests.py              # Tests (EMPTY)
        ├── urls.py               # App URL routes
        ├── views.py              # View functions
        ├── migrations/           # Database migrations (EMPTY)
        │   └── __init__.py
        └── templates/            # HTML templates (8,689 lines)
            ├── connecting_project.html       # Platform connection
            ├── first_html.html               # Early prototype
            ├── seen_add_project.html         # Add project page
            ├── seen_communities_page.html    # Communities page
            ├── seen_home_feed.html           # Main feed
            ├── seen_login_page.html          # Login/landing
            ├── seen_profile_page.html        # User profile
            ├── seen_profile_page(old).html   # Old version
            ├── seen_profile_page_stage_2.html # Profile editor
            └── seen_publish_project.html     # Manual project entry
```

---

## Development Environment Setup

### Initial Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd seen
   ```

2. **Create Python virtual environment:**
   ```bash
   python3 -m venv seenenv
   ```

3. **Activate virtual environment:**
   ```bash
   # Linux/macOS
   source seenenv/bin/activate

   # Windows
   seenenv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Navigate to Django project:**
   ```bash
   cd seen
   ```

6. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

7. **Start development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the application:**
   - Open browser to `http://127.0.0.1:8000/`

---

## Key Conventions and Patterns

### URL Routing Pattern

The project uses a two-tier URL routing system:

**Project-level** (`seen/urls.py`):
```python
urlpatterns = [
    path('', include('seen_app.urls')),  # Delegates to app
    path('admin/', admin.site.urls),     # Admin interface
]
```

**App-level** (`seen_app/urls.py`):
```python
urlpatterns = [
    path('', views.seen, name='seen_app'),                                 # /
    path('home/', views.home, name='home'),                                # /home/
    path('profile/', views.profile, name='profile'),                       # /profile/
    path('communities/', views.communities, name='communities'),           # /communities/
    path('add_project/', views.add_project, name='add_project'),          # /add_project/
    path('add_project/add_manual_project/', views.manual_project, ...),   # Nested route
    path('add_project/connecting_project/', views.connect_waiting, ...),  # Nested route
    path('update_profile/', views.update_profile, name='update_profile'), # /update_profile/
]
```

### View Function Pattern

All current views follow a simple template rendering pattern:

```python
def view_name(request):
    template = loader.get_template('template_name.html')
    return HttpResponse(template.render())
```

**Important Notes:**
- No class-based views currently used
- No form handling implemented
- No database queries (models are empty)
- No authentication/authorization checks
- No request data processing (GET/POST)

### File Naming Conventions

- **HTML templates:** `seen_<page_name>.html` (e.g., `seen_login_page.html`)
- **URLs:** Snake case (e.g., `add_project`, `update_profile`)
- **View functions:** Snake case matching URL names
- **Python modules:** Standard Django conventions

### Design System

When working with frontend code, maintain consistency with the existing design system:

- **Primary Colors:** Navy blue gradient (#001f3f → #003366)
- **Background:** Light gray (#f5f7fa)
- **Card Backgrounds:** White with subtle shadows
- **Typography:** System fonts (San Francisco, Segoe UI, Roboto)
- **Border Radius:** 16-20px for cards and containers
- **Shadows:** Layered, subtle (0 2px-20px rgba(0,0,0,0.05-0.3))
- **Layout:** Card-based with consistent spacing
- **Responsive:** Mobile-first approach

---

## Application Architecture

### Django MVC (Model-View-Template) Pattern

```
Request Flow:
Browser → Django URL Router (seen/urls.py)
        → App URL Router (seen_app/urls.py)
        → View Function (seen_app/views.py)
        → Template (seen_app/templates/*.html)
        → HTTP Response
```

### Current Pages and Routes

| Route | View Function | Template | Purpose |
|-------|--------------|----------|---------|
| `/` | `seen()` | `seen_login_page.html` | Landing/login page |
| `/home/` | `home()` | `seen_home_feed.html` | Main feed |
| `/profile/` | `profile()` | `seen_profile_page.html` | User profile |
| `/communities/` | `communities()` | `seen_communities_page.html` | Communities page |
| `/add_project/` | `add_project()` | `seen_add_project.html` | Add project |
| `/add_project/add_manual_project/` | `manual_project()` | `seen_publish_project.html` | Manual entry |
| `/add_project/connecting_project/` | `connect_waiting()` | `connecting_project.html` | Platform connect |
| `/update_profile/` | `update_profile()` | `seen_profile_page_stage_2.html` | Edit profile |

### Static Files

**Configuration** (`seen/settings.py`):
```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
```

**Note:** The `static/` directory does not currently exist. Create it when adding separate CSS/JS files.

---

## Current Development Status

### ✅ Completed

- Django project setup and configuration
- URL routing structure
- Comprehensive HTML/CSS UI design for all major pages
- Basic view functions (template rendering only)
- SQLite database configuration
- Virtual environment setup documentation

### 🚧 In Progress / Not Implemented

- **Database models** - `models.py` is empty
- **Database migrations** - No migrations created
- **User authentication** - No login/logout functionality
- **Form handling** - No POST request processing
- **CRUD operations** - No data persistence
- **Testing** - `tests.py` is empty
- **Static file organization** - All CSS/JS is inline in templates
- **Admin panel configuration** - Not customized
- **Data visualization** - Installed libraries not used
- **API endpoints** - Pure template-based rendering only

### ⚠️ Critical Gaps

1. **No database models defined** - All UI is static
2. **No authentication system** - Login page is non-functional
3. **No form processing** - Forms don't submit data
4. **Secret key exposed** - Hardcoded in settings.py
5. **DEBUG mode enabled** - Not production-ready
6. **No environment variables** - Configuration is hardcoded
7. **No tests** - Zero test coverage

---

## Working with This Codebase

### For AI Assistants: Critical Guidelines

#### 1. Understanding the Current State

**This is a UI-first project.** The frontend design is comprehensive and polished, but the backend logic is minimal. When working on this codebase:

- **Always read before modifying** - Use the `Read` tool to examine existing code
- **Respect the design system** - The UI has a consistent visual language
- **Don't assume functionality exists** - Most features are UI mockups only
- **Check for dependencies** - Many features depend on unimplemented models

#### 2. Database Development

When creating models, infer structure from the UI templates:

**Expected Models** (based on templates):
- `User` (extend Django's built-in User model)
- `Profile` (user profile with bio, banner, avatar, etc.)
- `Project` (user projects with title, description, links, etc.)
- `Post` (social feed posts)
- `Community` (student communities)
- `Certification` (user certifications)
- `Recommendation` (peer recommendations)
- `PortfolioLink` (external portfolio links)
- `Collaboration` (project collaborations)

**After creating models, always:**
```bash
python manage.py makemigrations
python manage.py migrate
```

#### 3. Working with Views

Current views are placeholder functions. When enhancing them:

```python
# Current pattern (simple):
def view_name(request):
    template = loader.get_template('template_name.html')
    return HttpResponse(template.render())

# Enhanced pattern (with data):
def view_name(request):
    context = {
        'data': Model.objects.all(),
        # ... other context variables
    }
    return render(request, 'template_name.html', context)
```

**When adding form handling:**
```python
def view_name(request):
    if request.method == 'POST':
        # Handle form submission
        form = SomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        # Display form
        form = SomeForm()
    return render(request, 'template.html', {'form': form})
```

#### 4. Template Modifications

Templates contain embedded CSS and JavaScript. When modifying:

- **Preserve existing styles** - Don't break the design system
- **Test responsiveness** - Design is mobile-first
- **Extract to static files** - Consider moving CSS/JS to separate files
- **Use Django template tags** - Add `{% csrf_token %}`, `{% url %}`, etc.

#### 5. Security Considerations

**Before deploying to production:**
- Move SECRET_KEY to environment variable
- Set DEBUG = False
- Configure ALLOWED_HOSTS
- Add HTTPS/SSL configuration
- Implement proper authentication
- Add CSRF protection to forms
- Validate and sanitize user inputs
- Use Django's built-in security features

#### 6. Testing Strategy

When writing tests:

```python
from django.test import TestCase, Client
from django.urls import reverse

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page_loads(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'seen_home_feed.html')
```

Run tests with:
```bash
python manage.py test
```

---

## Common Development Tasks

### Creating a New Model

1. **Define model in `seen_app/models.py`:**
```python
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

2. **Create and run migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

3. **Register in admin panel (`seen_app/admin.py`):**
```python
from django.contrib import admin
from .models import Project

admin.site.register(Project)
```

### Adding a New Page

1. **Create template in `seen_app/templates/`:**
```html
<!-- seen_new_page.html -->
<!DOCTYPE html>
<html>
<head>
    <title>New Page</title>
</head>
<body>
    <h1>New Page Content</h1>
</body>
</html>
```

2. **Create view in `seen_app/views.py`:**
```python
def new_page(request):
    template = loader.get_template('seen_new_page.html')
    return HttpResponse(template.render())
```

3. **Add URL route in `seen_app/urls.py`:**
```python
urlpatterns = [
    # ... existing patterns
    path('new-page/', views.new_page, name='new_page'),
]
```

### Working with Static Files

1. **Create static directory structure:**
```bash
mkdir -p seen/static/css
mkdir -p seen/static/js
mkdir -p seen/static/images
```

2. **Add CSS file (`seen/static/css/style.css`):**
```css
/* Your styles here */
```

3. **Use in templates:**
```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
</html>
```

4. **Collect static files (for production):**
```bash
python manage.py collectstatic
```

### Creating Superuser

```bash
python manage.py createsuperuser
```

Follow prompts to create admin account, then access admin panel at `/admin/`.

### Running Development Server

```bash
cd seen  # Navigate to Django project directory
python manage.py runserver
```

Access at `http://127.0.0.1:8000/`

---

## Important Considerations

### Working Directory

**Django commands must be run from `/home/user/seen/seen/` directory** (where `manage.py` is located).

### Database State

- SQLite database exists but contains only Django's default tables
- No custom models have been migrated
- Database is suitable for development only
- Consider PostgreSQL for production

### Data Analysis Libraries

pandas, numpy, seaborn, and matplotlib are installed but unused. Consider:
- User analytics dashboards
- Project statistics visualization
- Community engagement metrics
- Platform growth tracking

### Pages Directory

`/pages/` contains prototype HTML files that are **not actively used** by Django. These appear to be design mockups. Templates in `/seen/seen_app/templates/` are the active versions.

### Git Workflow

- **Current branch:** `claude/claude-md-miriorx48zkvfd7o-01LyxWVfDSgiYcwHWeve7Kev`
- **Repository:** github.com/vik01/seen
- Virtual environment directories are gitignored: `/set_up`, `/seenenv`, `/myseen`

---

## Next Steps for Development

### Immediate Priorities

1. **Define database models** (`seen_app/models.py`)
   - User Profile model with fields matching UI
   - Project model with all necessary fields
   - Post, Community, Certification models
   - Define relationships (ForeignKey, ManyToMany)

2. **Create and run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Implement authentication**
   - Use Django's built-in auth system
   - Create login/logout views
   - Add registration functionality
   - Protect views with `@login_required`

4. **Add form handling**
   - Create Django forms for project creation
   - Handle POST requests in views
   - Add form validation
   - Implement CSRF protection

5. **Connect UI to backend**
   - Pass data from models to templates
   - Make forms functional
   - Add CRUD operations
   - Implement user-specific content filtering

### Short-term Goals

6. **Organize static files**
   - Create `static/` directory structure
   - Extract inline CSS to separate files
   - Extract JavaScript to separate files
   - Optimize for performance

7. **Write tests**
   - Unit tests for models
   - View tests for all pages
   - Form validation tests
   - Integration tests for workflows

8. **Configure admin panel**
   - Register all models
   - Customize admin interface
   - Add list filters and search
   - Configure permissions

9. **Add user features**
   - Profile editing functionality
   - Project CRUD operations
   - Community joining/leaving
   - Social interactions (likes, comments)

10. **Implement platform integrations**
    - GitHub API integration
    - OAuth authentication for external platforms
    - Project import functionality

### Long-term Goals

11. **Production readiness**
    - Environment variable configuration
    - Production settings file
    - Database migration to PostgreSQL
    - Static file serving configuration
    - Security hardening

12. **Data visualization**
    - Utilize installed data analysis libraries
    - Create analytics dashboards
    - Generate reports and insights
    - Visualize platform metrics

13. **API development**
    - REST API for mobile clients
    - Authentication tokens
    - API documentation
    - Rate limiting

14. **Deployment**
    - Containerization (Docker)
    - CI/CD pipeline
    - Cloud hosting setup
    - Domain and SSL configuration

---

## Quick Reference

### Essential Commands

```bash
# Navigate to project
cd /home/user/seen/seen

# Activate virtual environment
source ../seenenv/bin/activate

# Run development server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run tests
python manage.py test

# Django shell (for debugging)
python manage.py shell
```

### Important File Paths

```
Settings:         /home/user/seen/seen/seen/settings.py
URLs (project):   /home/user/seen/seen/seen/urls.py
URLs (app):       /home/user/seen/seen/seen_app/urls.py
Views:            /home/user/seen/seen/seen_app/views.py
Models:           /home/user/seen/seen/seen_app/models.py
Templates:        /home/user/seen/seen/seen_app/templates/
Admin:            /home/user/seen/seen/seen_app/admin.py
Tests:            /home/user/seen/seen/seen_app/tests.py
Requirements:     /home/user/seen/requirements.txt
Database:         /home/user/seen/seen/db.sqlite3
```

### Helpful Resources

- Django Documentation: https://docs.djangoproject.com/en/5.2/
- Django Tutorial: https://docs.djangoproject.com/en/5.2/intro/tutorial01/
- Django REST Framework: https://www.django-rest-framework.org/
- Python Virtual Environments: https://docs.python.org/3/tutorial/venv.html

---

## Notes for AI Assistants

When working with this codebase, remember:

1. **UI is ahead of backend** - Don't assume features work just because they're in the UI
2. **Models need to be created** - Infer structure from template files
3. **Security is not implemented** - Authentication and authorization are placeholders
4. **Testing is required** - No tests exist yet
5. **Design system is established** - Maintain visual consistency
6. **Simple is better** - Don't over-engineer solutions
7. **Read before writing** - Always examine existing code first
8. **Django conventions** - Follow Django best practices
9. **Documentation matters** - Update this file as the project evolves
10. **Ask when uncertain** - Clarify requirements before implementing

---

**End of CLAUDE.md**
