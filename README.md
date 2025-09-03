# ACEestFitness - Fitness Tracking Application

[![CI/CD Pipeline](https://github.com/vamsigorle29/ACEestFitness-DevOps/workflows/CI%3ACD%20Pipeline/badge.svg)](https://github.com/vamsigorle29/ACEestFitness-DevOps/actions)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-2.3.3+-green.svg)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)

A Flask-based fitness tracking application with Docker containerization and automated CI/CD pipeline. Features both web interface and desktop application for comprehensive fitness tracking.

## Overview

ACEestFitness allows users to track workout sessions, monitor progress, and maintain fitness records. The application includes a web interface for workout management, RESTful APIs for integration, and a desktop application for offline use.

## Features

- **Web Application**: Flask-based web interface with responsive design
- **Desktop Application**: Tkinter-based GUI for offline use
- **Workout Tracking**: Duration, calories, and timestamp recording
- **RESTful API**: Complete API endpoints for integration
- **Data Persistence**: JSON-based storage with backup capabilities
- **Health Monitoring**: Built-in health check endpoints
- **Docker Support**: Full containerization for deployment
- **Comprehensive Testing**: Unit, integration, and API testing

## Tech Stack

- **Backend**: Flask (Python 3.9+)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Desktop**: Tkinter (Python GUI)
- **Testing**: Pytest with coverage reporting
- **Containerization**: Docker & Docker Compose
- **CI/CD**: GitHub Actions with automated testing
- **Security**: Automated vulnerability scanning

## Prerequisites

- Python 3.9+
- Docker and Docker Compose (optional)
- Git
- Modern web browser

## Getting Started

### Option 1: Web Application (Flask)

1. **Clone the repository**
   ```bash
   git clone https://github.com/vamsigorle29/ACEestFitness-DevOps.git
   cd ACEestFitness-DevOps
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the web application**
   ```bash
   python src/app.py
   ```

5. **Access the application**
   - Web Interface: http://localhost:5000
   - API Documentation: http://localhost:5000/api/workouts
   - Health Check: http://localhost:5000/health

### Option 2: Desktop Application (Tkinter)

1. **Run the desktop application**
   ```bash
   python ACEest_Fitness.py
   ```

2. **Features**
   - Simple GUI interface
   - Add workout sessions
   - View workout history
   - In-memory storage

### Option 3: Docker Deployment

**Using Docker Compose (recommended):**
```bash
docker-compose up --build
```

**Manual Docker build:**
```bash
docker build -t aceest-fitness .
docker run -p 5000:5000 aceest-fitness
```

## Testing

### Install Test Dependencies
```bash
pip install -r requirements-test.txt
```

### Run Tests
```bash
# All tests
python -m pytest tests/ -v

# With coverage
python -m pytest tests/ -v --cov=src --cov-report=html

# Specific test types
python -m pytest tests/ -v -m "unit"
python -m pytest tests/ -v -m "integration"
```

### Docker Testing
```bash
# Build test image
docker build -f Dockerfile.test -t aceest-fitness:test .

# Run tests in container
docker run --rm aceest-fitness:test
```

## Project Structure

```
ACEestFitness/
+-- src/                    # Source code
¦   +-- app.py             # Flask web application
¦   +-- __init__.py        # Package initialization
¦   +-- templates/         # HTML templates
+-- tests/                 # Test suite
¦   +-- test_app.py       # Comprehensive test suite
¦   +-- __init__.py       # Test package
+-- ACEest_Fitness.py      # Desktop application
+-- requirements.txt       # Production dependencies
+-- requirements-test.txt  # Test dependencies
+-- Dockerfile            # Production container
+-- Dockerfile.test       # Test container
+-- docker-compose.yml    # Local development
+-- Makefile              # Build automation
+-- .github/workflows/    # CI/CD pipeline
+-- README.md
```

## API Endpoints

### REST API
- `GET /api/workouts` - List all workouts
- `POST /api/workouts` - Create new workout
- `GET /health` - Health check endpoint

### Web Routes
- `GET /` - Home page with workout summary
- `GET /add_workout` - Add workout form
- `POST /add_workout` - Submit new workout
- `GET /workouts` - View all workouts

## Configuration

### Environment Variables
- `FLASK_ENV`: Environment (development/production)
- `FLASK_DEBUG`: Debug mode (0/1)
- `DATA_FILE`: Workout data file path

### Data Storage
- **Web App**: Persistent JSON storage in `workouts.json`
- **Desktop App**: In-memory storage (resets on restart)

## Docker Commands

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

- Runs comprehensive test suite
- Builds and tests Docker images
- Performs security vulnerability scanning
- Generates detailed coverage reports
- Deploys to production on main branch

### Pipeline Stages
1. **Test**: Unit and integration testing with coverage
2. **Build**: Docker image creation and validation
3. **Security**: Automated vulnerability scanning
4. **Deploy**: Production deployment with health checks
5. **Notify**: Status reporting and notifications

## Development

### Make Commands
```bash
make help          # Show available commands
make install       # Install production dependencies
make install-dev   # Install development dependencies
make test          # Run test suite
make test-cov      # Run tests with coverage
make run           # Run Flask application

make clean         # Clean generated files
make docker-build  # Build Docker image
make docker-test   # Build and test Docker image
make docker-run     # Run Docker container
make docker-stop    # Stop Docker container
make docker-compose-up   # Start with Docker Compose
make docker-compose-down # Stop Docker Compose
make lint            # Run code linting
make security        # Run security checks
make all             # Run all checks and tests
```

### Adding New Features
1. Create feature branch
2. Add tests for new functionality
3. Implement feature
4. Ensure all tests pass
5. Update documentation
6. Submit pull request

## Deployment

### Production Deployment
```bash
# Build production image
docker build -t aceest-fitness:prod .

# Run with production settings
docker run -d -p 80:5000 \
  -e FLASK_ENV=production \
  -e FLASK_DEBUG=0 \
  --name fitness-prod \
  aceest-fitness:prod
```

### Environment Configuration
```bash
FLASK_ENV=production
FLASK_DEBUG=0
DATA_FILE=/app/data/workouts.json
```

## Security Features

- Input validation and sanitization
- Comprehensive error handling
- Dependency vulnerability scanning
- Security headers implementation
- Health check monitoring

## Monitoring & Logging

- Health check endpoints (`/health`)
- Docker health checks
- Application logging
- Performance metrics
- CI/CD pipeline monitoring

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass (`make test`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Submit a pull request

## Troubleshooting

### Common Issues

**Flask app not starting:**
```bash
# Check if port 5000 is available
netstat -an | grep 5000

# Try different port
python src/app.py --port 5001
```

**Tests failing:**
```bash
# Install test dependencies
pip install -r requirements-test.txt

# Run tests with verbose output
python -m pytest tests/ -v --tb=short
```

**Docker issues:**
```bash
# Check Docker is running
docker --version

# Clean up containers
docker system prune -a
```

## License

Educational project demonstrating modern DevOps practices and full-stack development.

## Support

For issues and questions:
1. Check the test suite for usage examples
2. Review CI/CD pipeline logs
3. Check Docker container logs
4. Verify environment configuration
5. Create an issue in the repository

---

**Built with ?? for fitness tracking and DevOps excellence**
