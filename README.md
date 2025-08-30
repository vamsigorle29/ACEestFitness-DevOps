# ACEestFitness - Fitness Tracking Application

[![CI/CD Pipeline](https://github.com/vamsigorle29/ACEestFitness-DevOps/workflows/CI%3ACD%20Pipeline/badge.svg)](https://github.com/vamsigorle29/ACEestFitness-DevOps/actions)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-2.3.3+-green.svg)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)

A Flask-based fitness tracking application with Docker containerization and automated CI/CD pipeline. Built for the DevOps assignment demonstrating modern development practices.

## Overview

ACEestFitness allows users to track workout sessions, monitor progress, and maintain fitness records. The application includes a web interface for workout management and RESTful APIs for integration.

## Features

- Workout tracking with duration and calorie information
- Web-based interface with responsive design
- RESTful API endpoints
- JSON-based data persistence
- Health monitoring endpoints
- Docker containerization

## Tech Stack

- **Backend**: Flask (Python 3.9+)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Testing**: Pytest with coverage
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Security**: Automated vulnerability scanning

## Prerequisites

- Python 3.9+
- Docker and Docker Compose
- Git
- Modern web browser

## Getting Started

### Local Development

1. Clone the repository
   ```bash
   git clone https://github.com/vamsigorle29/ACEestFitness-DevOps.git
   cd ACEestFitness-DevOps
   ```

2. Set up virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application
   ```bash
   python app.py
   ```

5. Open http://localhost:5000 in your browser

### Docker Deployment

Using Docker Compose (recommended):
```bash
docker-compose up --build
```

Or manual Docker build:
```bash
docker build -t aceest-fitness .
docker run -p 5000:5000 aceest-fitness
```

## Testing

### Local Testing

Install test dependencies:
```bash
pip install -r requirements-test.txt
```

Run tests:
```bash
# All tests
pytest test_app.py -v

# With coverage
pytest test_app.py -v --cov=app --cov-report=html

# Specific test types
pytest test_app.py -v -m "unit"
pytest test_app.py -v -m "integration"
```

### Docker Testing

```bash
# Build test image
docker build -f Dockerfile.test -t aceest-fitness:test .

# Run tests in container
docker run --rm aceest-fitness:test
```

## Docker

### Building Images

```bash
# Production image
docker build -t aceest-fitness:latest .

# Test image
docker build -f Dockerfile.test -t aceest-fitness:test .
```

### Running Containers

```bash
# Production container
docker run -d -p 5000:5000 --name fitness-app aceest-fitness:latest

# Development with volume mounting
docker run -d -p 5000:5000 -v $(pwd):/app aceest-fitness:latest

# Health check
docker exec fitness-app curl -f http://localhost:5000/health
```

## CI/CD Pipeline

The GitHub Actions workflow automatically:

- Runs all tests on every push
- Builds and tests Docker images
- Performs security scanning
- Generates coverage reports
- Deploys to production on main branch

### Pipeline Stages

1. **Test**: Unit and integration testing
2. **Build**: Docker image creation
3. **Security**: Vulnerability scanning
4. **Deploy**: Production deployment
5. **Notify**: Status reporting

## Project Structure

```
ACEestFitness/
├── app.py                 # Flask application
├── requirements.txt       # Dependencies
├── requirements-test.txt  # Test dependencies
├── test_app.py           # Test suite
├── pytest.ini           # Pytest config
├── Dockerfile            # Production image
├── Dockerfile.test       # Test image
├── docker-compose.yml    # Local development
├── .github/workflows/    # CI/CD pipeline
├── templates/            # HTML templates
└── README.md
```

## Configuration

### Environment Variables

- `FLASK_ENV`: Environment (development/production)
- `FLASK_DEBUG`: Debug mode (0/1)
- `DATA_FILE`: Workout data file path

## API Endpoints

### REST API

- `GET /api/workouts` - List all workouts
- `POST /api/workouts` - Create new workout
- `GET /health` - Health check

### Web Routes

- `GET /` - Home page
- `GET /add_workout` - Add workout form
- `POST /add_workout` - Submit workout
- `GET /workouts` - View workouts

## Test Coverage

The test suite covers:

- Flask route testing
- Data function validation
- API endpoint testing
- Integration workflows
- Error handling scenarios

## Deployment

### Production

1. Build production image
   ```bash
   docker build -t aceest-fitness:prod .
   ```

2. Run with production settings
   ```bash
   docker run -d -p 80:5000 \
     -e FLASK_ENV=production \
     -e FLASK_DEBUG=0 \
     --name fitness-prod \
     aceest-fitness:prod
   ```

### Environment Variables

```bash
FLASK_ENV=production
FLASK_DEBUG=0
DATA_FILE=/app/data/workouts.json
```

## Security

- Input validation and sanitization
- Error handling and logging
- Dependency vulnerability scanning
- Security headers implementation

## Monitoring

- Health check endpoints
- Docker health checks
- Application logging
- Performance metrics

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## License

Educational project for DevOps assignment.

## Support

For issues:

1. Check the test suite for examples
2. Review CI/CD pipeline logs
3. Check Docker container logs
4. Verify environment configuration

## Assignment Status

- ✅ Flask Application
- ✅ Version Control (Git)
- ✅ Unit Testing (Pytest)
- ✅ Automated Testing
- ✅ Docker Containerization
- ✅ CI/CD Pipeline (GitHub Actions)
- ✅ Documentation

---

Built for DevOps excellence 