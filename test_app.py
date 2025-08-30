import pytest
import json
import os
import tempfile
from app import app, load_workouts, save_workouts

@pytest.fixture
def client():
    """Create a test client for the Flask application"""
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    
    # Create a temporary file for testing
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        f.write('[]')
        temp_file = f.name
    
    # Override the data file path for testing
    app.config['DATA_FILE'] = temp_file
    
    with app.test_client() as client:
        yield client
    
    # Clean up temporary file
    os.unlink(temp_file)

@pytest.fixture
def sample_workout():
    """Sample workout data for testing"""
    return {
        'workout_name': 'Running',
        'duration': 30,
        'calories': 200
    }

class TestAppRoutes:
    """Test all Flask application routes"""
    
    def test_index_route(self, client):
        """Test the home page route"""
        response = client.get('/')
        assert response.status_code == 200
        assert b'ACEestFitness' in response.data
        assert b'Welcome to ACEestFitness' in response.data
    
    def test_add_workout_get(self, client):
        """Test GET request to add workout page"""
        response = client.get('/add_workout')
        assert response.status_code == 200
        assert b'Add New Workout' in response.data
        assert b'Workout Name' in response.data
    
    def test_add_workout_post_success(self, client, sample_workout):
        """Test successful POST request to add workout"""
        response = client.post('/add_workout', data=sample_workout, follow_redirects=True)
        assert response.status_code == 200
        assert b'Workout added successfully' in response.data
    
    def test_add_workout_post_missing_fields(self, client):
        """Test POST request with missing required fields"""
        response = client.post('/add_workout', data={'workout_name': 'Running'}, follow_redirects=True)
        assert response.status_code == 200
        assert b'Please fill in all required fields' in response.data
    
    def test_add_workout_post_invalid_duration(self, client):
        """Test POST request with invalid duration"""
        response = client.post('/add_workout', data={
            'workout_name': 'Running',
            'duration': 'invalid',
            'calories': '200'
        }, follow_redirects=True)
        assert response.status_code == 200
        assert b'Duration and calories must be valid numbers' in response.data
    
    def test_view_workouts_empty(self, client):
        """Test viewing workouts when none exist"""
        response = client.get('/workouts')
        assert response.status_code == 200
        assert b'No workouts found' in response.data
    
    def test_view_workouts_with_data(self, client, sample_workout):
        """Test viewing workouts when data exists"""
        # First add a workout
        client.post('/add_workout', data=sample_workout)
        
        # Then view workouts
        response = client.get('/workouts')
        assert response.status_code == 200
        assert b'Running' in response.data
        assert b'30 min' in response.data
    
    def test_api_workouts_get(self, client):
        """Test API endpoint to get all workouts"""
        response = client.get('/api/workouts')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert isinstance(data, list)
        assert len(data) == 0
    
    def test_api_workouts_post_success(self, client, sample_workout):
        """Test API endpoint to add workout successfully"""
        response = client.post('/api/workouts', 
                             data=json.dumps(sample_workout),
                             content_type='application/json')
        assert response.status_code == 201
        data = json.loads(response.data)
        assert data['message'] == 'Workout added successfully'
        assert 'workout' in data
    
    def test_api_workouts_post_missing_fields(self, client):
        """Test API endpoint with missing fields"""
        response = client.post('/api/workouts', 
                             data=json.dumps({'workout_name': 'Running'}),
                             content_type='application/json')
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
    
    def test_api_workouts_post_invalid_data(self, client):
        """Test API endpoint with invalid data types"""
        response = client.post('/api/workouts', 
                             data=json.dumps({
                                 'workout_name': 'Running',
                                 'duration': 'invalid'
                             }),
                             content_type='application/json')
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
    
    def test_health_check(self, client):
        """Test health check endpoint"""
        response = client.get('/health')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['status'] == 'healthy'
        assert 'timestamp' in data

class TestDataFunctions:
    """Test data handling functions"""
    
    def test_load_workouts_empty_file(self):
        """Test loading workouts from empty file"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            f.write('[]')
            temp_file = f.name
        
        try:
            # Temporarily override the data file
            original_file = app.config.get('DATA_FILE', 'workouts.json')
            app.config['DATA_FILE'] = temp_file
            
            workouts = load_workouts()
            assert isinstance(workouts, list)
            assert len(workouts) == 0
        finally:
            os.unlink(temp_file)
    
    def test_load_workouts_with_data(self):
        """Test loading workouts from file with data"""
        test_data = [
            {'id': 1, 'workout_name': 'Running', 'duration': 30, 'calories': 200}
        ]
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(test_data, f)
            temp_file = f.name
        
        try:
            # Temporarily override the data file
            original_file = app.config.get('DATA_FILE', 'workouts.json')
            app.config['DATA_FILE'] = temp_file
            
            workouts = load_workouts()
            assert isinstance(workouts, list)
            assert len(workouts) == 1
            assert workouts[0]['workout_name'] == 'Running'
        finally:
            os.unlink(temp_file)
    
    def test_save_workouts(self):
        """Test saving workouts to file"""
        test_data = [
            {'id': 1, 'workout_name': 'Running', 'duration': 30, 'calories': 200}
        ]
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_file = f.name
        
        try:
            # Temporarily override the data file
            original_file = app.config.get('DATA_FILE', 'workouts.json')
            app.config['DATA_FILE'] = temp_file
            
            save_workouts(test_data)
            
            # Verify data was saved
            with open(temp_file, 'r') as f:
                saved_data = json.load(f)
            
            assert saved_data == test_data
        finally:
            os.unlink(temp_file)

class TestIntegration:
    """Integration tests for the complete workflow"""
    
    def test_complete_workout_workflow(self, client):
        """Test the complete workflow: add workout -> view workouts -> check API"""
        # Add a workout
        workout_data = {
            'workout_name': 'Weight Training',
            'duration': '45',
            'calories': '300'
        }
        
        response = client.post('/add_workout', data=workout_data, follow_redirects=True)
        assert response.status_code == 200
        assert b'Workout added successfully' in response.data
        
        # View workouts page
        response = client.get('/workouts')
        assert response.status_code == 200
        assert b'Weight Training' in response.data
        assert b'45 min' in response.data
        
        # Check API endpoint
        response = client.get('/api/workouts')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) == 1
        assert data[0]['workout_name'] == 'Weight Training'
        assert data[0]['duration'] == 45
    
    def test_multiple_workouts(self, client):
        """Test adding multiple workouts and verifying they all appear"""
        workouts = [
            {'workout_name': 'Running', 'duration': '30', 'calories': '200'},
            {'workout_name': 'Yoga', 'duration': '60', 'calories': '100'},
            {'workout_name': 'Swimming', 'duration': '45', 'calories': '400'}
        ]
        
        # Add all workouts
        for workout in workouts:
            response = client.post('/add_workout', data=workout, follow_redirects=True)
            assert response.status_code == 200
            assert b'Workout added successfully' in response.data
        
        # Verify all workouts appear in the list
        response = client.get('/workouts')
        assert response.status_code == 200
        for workout in workouts:
            assert workout['workout_name'].encode() in response.data
        
        # Verify API returns all workouts
        response = client.get('/api/workouts')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) == 3

if __name__ == '__main__':
    pytest.main([__file__]) 