# Pizarra

A collaborative project management web application built with Django and PostgreSQL, designed for team collaboration and task organization.

![Pizarra Screenshot](static/screenshot.png) <!-- Add actual screenshot path -->

## Features

- **User Authentication**: Secure signup/login with custom user model
- **Project Management**: 
  - Create/Edit projects
  - Add project files and notes
  - Collaborative workspace
- **Task System**:
  - Todo lists with progress tracking
  - Task assignments and due dates
- **Responsive Design**: Mobile-friendly interface using Tailwind CSS
- **Dockerized**: Containerized development and production setup
- **PostgreSQL**: Robust database backend
- **Security**: CSRF protection and secure headers

## Technology Stack

### Backend
- Django 5.1
- Django Compressor
- WhiteNoise
- PostgreSQL 16
- Gunicorn

### Frontend
- Tailwind CSS 3.4
- HTML5
- Django Templates

### DevOps
- Docker 24.0+
- Docker Compose 2.23+
- Render.com deployment
- GitHub Actions (example config included)

## Development Setup

### Prerequisites
- Docker Desktop 4.25+
- Docker Compose 2.23+
- Python 3.10+
- Node.js 18+ (for Tailwind CSS)

### Installation
```bash
git clone https://github.com/yourusername/pizarra.git
cd pizarra
cp .env.example .env  # Update with your values
docker-compose up --build
```

### Environment Variables
```env
# Required
DEBUG=True
DJANGO_SECRET_KEY=your-secret-key
POSTGRES_DB=pizarradb
POSTGRES_USER=pizarrauser
POSTGRES_PASSWORD=pizarrapass

# Optional
CSRF_TRUSTED_ORIGINS=http://localhost:8000,http://127.0.0.1:8000
```

### Common Commands
```bash
# Run database migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser

# Collect static files
docker-compose exec web python manage.py collectstatic

# Tailwind CSS development
docker-compose exec web npm run dev
```

## Production Deployment

### Render.com Setup
1. Create new Web Service
2. Connect GitHub repository
3. Set environment variables:
   ```env
   DEBUG=False
   EXTERNAL_DATABASE_URL=postgres://user:pass@host:port/db
   CSRF_TRUSTED_ORIGINS=https://your-render-url.onrender.com
   ```
4. Use Dockerfile deployment

### Required Services
- PostgreSQL database on Render.com
- Web service with Docker runtime

## Project Structure

```text
pizarra/
├── Docker/            # Docker configurations
├── account/           # Authentication system
├── project/           # Project management
├── task/              # Task tracking
├── templates/         # HTML templates
├── static/            # Static assets
│   ├── src/           # Tailwind source
│   └── css/           # Compiled CSS
├── requirements.txt   # Python dependencies
├── docker-compose.yml # Development setup
└── .env.example       # Environment template
```

## Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Support

For issues and feature requests, please [open an issue](https://github.com/abdulhamid97mousa/pizarra/issues).


