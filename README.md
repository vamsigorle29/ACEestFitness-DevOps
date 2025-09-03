# ACEestFitness - Fitness Tracking Application

[![CI/CD Pipeline](https://img.shields.io/badge/CI/CD-Pipeline-green.svg)](https://github.com/vamsigorle29/ACEestFitness-DevOps)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-2.3.3+-green.svg)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)
[![Tests](https://img.shields.io/badge/tests-17%20passed-brightgreen.svg)](#testing)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](#testing)

> 🏋️‍♂️ **A comprehensive fitness tracking application with both web and desktop interfaces, featuring Docker containerization and automated CI/CD pipeline.**

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-start)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Docker Deployment](#docker-deployment)
- [Development](#development)
- [Contributing](#contributing)

## 🎯 Overview

ACEestFitness is a modern, full-stack fitness tracking application that allows users to:

- 📊 **Track workout sessions** with duration, calories, and timestamps
- 🌐 **Access via web interface** with responsive design
- 💻 **Use desktop application** for offline tracking
- 🔌 **Integrate via REST API** for third-party applications
- 📈 **Monitor progress** with comprehensive analytics
- 🐳 **Deploy anywhere** with Docker containerization

## ✨ Features

### 🌐 Web Application
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Real-time Updates**: Instant workout tracking and progress monitoring
- **User-friendly Interface**: Intuitive forms and data visualization
- **RESTful API**: Complete API endpoints for integration

### 💻 Desktop Application
- **Offline Capability**: Works without internet connection
- **Simple GUI**: Clean Tkinter-based interface
- **Quick Access**: Fast workout logging and viewing
- **Local Storage**: In-memory data persistence

### 🔧 Technical Features
- **Data Persistence**: JSON-based storage with backup capabilities
- **Health Monitoring**: Built-in health check endpoints
- **Comprehensive Testing**: 17 test cases with 100% coverage
- **Security**: Input validation and error handling
- **CI/CD Pipeline**: Automated testing and deployment

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| **Backend** | Flask (Python 3.9+) |
| **Frontend** | HTML5, CSS3, Bootstrap 5 |
| **Desktop** | Tkinter (Python GUI) |
| **Testing** | Pytest with coverage reporting |
| **Containerization** | Docker & Docker Compose |
| **CI/CD** | GitHub Actions |
| **Security** | Automated vulnerability scanning |

## �� Quick Start

### Option 1: Web Application (Recommended)

```bash
# Clone the repository
git clone https://github.com/vamsigorle29/ACEestFitness-DevOps.git
cd ACEestFitness-DevOps

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python src/app.py
```

🌐 **Access the application at:** http://localhost:5000

### Option 2: Desktop Application

```bash
# Run the desktop application
python ACEest_Fitness.py
```

### Option 3: Docker Deployment

```bash
# Using Docker Compose (recommended)
docker-compose up --build

# Or manual Docker build
docker build -t aceest-fitness .
docker run -p 5000:5000 aceest-fitness
```

## 📚 API Documentation

### REST API Endpoints

| Method | Endpoint | Description | Example |
|--------|----------|-------------|---------|
| `GET` | `/api/workouts` | List all workouts | `curl http://localhost:5000/api/workouts` |
| `POST` | `/api/workouts` | Create new workout | `curl -X POST -H "Content-Type: application/json" -d '{"workout_name":"Running","duration":30,"calories":300}' http://localhost:5000/api/workouts` |
| `GET` | `/health` | Health check | `curl http://localhost:5000/health` |

### Web Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page with workout summary |
| `/add_workout` | GET/POST | Add workout form and submission |
| `/workouts` | GET | View all workouts |

### Example API Usage

```bash
# Add a new workout
curl -X POST http://localhost:5000/api/workouts \
  -H "Content-Type: application/json" \
  -d '{
    "workout_name": "Running",
    "duration": 30,
    "calories": 300
  }'

# Get all workouts
curl http://localhost:5000/api/workouts

# Health check
curl http://localhost:5000/health
```

## 🧪 Testing

### Run Tests

```bash
# Install test dependencies
pip install -r requirements-test.txt

# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ -v --cov=src --cov-report=html

# Run specific test types
python -m pytest tests/ -v -m "unit"
python -m pytest tests/ -v -m "integration"
```

### Test Results
- ✅ **17/17 tests passing**
- ✅ **100% code coverage**
- ✅ **Unit tests**: Route testing, data functions
- ✅ **Integration tests**: Complete workflows
- ✅ **API tests**: All endpoints validated

## 🐳 Docker Deployment

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

## 🔧 Development

### Project Structure

```
ACEestFitness/
├── 📁 src/                    # Source code
│   ├── 📄 app.py             # Flask web application
│   ├── 📄 __init__.py        # Package initialization
│   └── 📁 templates/         # HTML templates
├── 📁 tests/                 # Test suite
│   ├── �� test_app.py       # Comprehensive test suite
│   └── 📄 __init__.py       # Test package
├── 📄 ACEest_Fitness.py      # Desktop application
├── 📄 requirements.txt       # Production dependencies
├── 📄 requirements-test.txt  # Test dependencies
├── 📄 Dockerfile            # Production container
├── 📄 Dockerfile.test       # Test container
├── 📄 docker-compose.yml    # Local development
├── 📄 Makefile              # Build automation
├── 📁 .github/workflows/    # CI/CD pipeline
└── 📄 README.md
```

### Make Commands

```bash
make help              # Show available commands
make install           # Install production dependencies
make install-dev       # Install development dependencies
make test              # Run test suite
make test-cov          # Run tests with coverage
make run               # Run Flask application
make clean             # Clean generated files
make docker-build      # Build Docker image
make docker-run        # Run Docker container
make docker-test       # Build and test Docker image
make docker-stop       # Stop Docker container
make docker-compose-up # Start with Docker Compose
make docker-compose-down # Stop Docker Compose
make lint              # Run code linting
make security          # Run security checks
make all               # Run all checks and tests
```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `FLASK_ENV` | Environment (development/production) | `development` |
| `FLASK_DEBUG` | Debug mode (0/1) | `1` |
| `DATA_FILE` | Workout data file path | `workouts.json` |

## 🔄 CI/CD Pipeline

The GitHub Actions workflow automatically:

- ✅ **Runs comprehensive test suite** (17 tests)
- ✅ **Builds and tests Docker images**
- ✅ **Performs security vulnerability scanning**
- ✅ **Generates detailed coverage reports**
- ✅ **Deploys to production** on main branch

### Pipeline Stages

1. **🧪 Test**: Unit and integration testing with coverage
2. **🏗️ Build**: Docker image creation and validation
3. **🔒 Security**: Automated vulnerability scanning
4. **🚀 Deploy**: Production deployment with health checks
5. **📢 Notify**: Status reporting and notifications

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**
4. **Add tests** for new functionality
5. **Ensure all tests pass**: `make test`
6. **Commit your changes**: `git commit -m 'Add amazing feature'`
7. **Push to the branch**: `git push origin feature/amazing-feature`
8. **Submit a pull request**

### Development Guidelines

- Write tests for new features
- Follow PEP 8 style guidelines
- Update documentation as needed
- Ensure all CI/CD checks pass

## 🐛 Troubleshooting

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

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

Need help? Here are your options:

1. 📖 **Check the documentation** above
2. 🧪 **Review the test suite** for usage examples
3. 📋 **Check CI/CD pipeline logs**
4. 🐳 **Check Docker container logs**
5. ⚙️ **Verify environment configuration**
6. 🐛 **Create an issue** in the repository

---

<div align="center">

**Built with <3 for fitness tracking and DevOps excellence**

[⬆ Back to Top](#aceestfitness---fitness-tracking-application)

</div>
