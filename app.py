from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Data file to persist workouts
DATA_FILE = 'workouts.json'

def load_workouts():
    """Load workouts from JSON file"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

def save_workouts(workouts):
    """Save workouts to JSON file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(workouts, f, indent=2)

@app.route('/')
def index():
    """Home page showing workout summary"""
    workouts = load_workouts()
    total_workouts = len(workouts)
    total_duration = sum(workout['duration'] for workout in workouts)
    
    return render_template('index.html', 
                         total_workouts=total_workouts, 
                         total_duration=total_duration,
                         recent_workouts=workouts[-5:])  # Show last 5 workouts

@app.route('/add_workout', methods=['GET', 'POST'])
def add_workout():
    """Add a new workout"""
    if request.method == 'POST':
        workout_name = request.form.get('workout_name')
        duration = request.form.get('duration')
        calories = request.form.get('calories', 0)
        
        if not workout_name or not duration:
            flash('Please fill in all required fields!', 'error')
            return redirect(url_for('add_workout'))
        
        try:
            duration = int(duration)
            calories = int(calories) if calories else 0
            
            new_workout = {
                'id': len(load_workouts()) + 1,
                'workout_name': workout_name,
                'duration': duration,
                'calories': calories,
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            workouts = load_workouts()
            workouts.append(new_workout)
            save_workouts(workouts)
            
            flash('Workout added successfully!', 'success')
            return redirect(url_for('index'))
            
        except ValueError:
            flash('Duration and calories must be valid numbers!', 'error')
            return redirect(url_for('add_workout'))
    
    return render_template('add_workout.html')

@app.route('/workouts')
def view_workouts():
    """View all workouts"""
    workouts = load_workouts()
    return render_template('workouts.html', workouts=workouts)

@app.route('/api/workouts')
def api_workouts():
    """API endpoint to get all workouts"""
    workouts = load_workouts()
    return jsonify(workouts)

@app.route('/api/workouts', methods=['POST'])
def api_add_workout():
    """API endpoint to add workout"""
    data = request.get_json()
    
    if not data or 'workout_name' not in data or 'duration' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:
        new_workout = {
            'id': len(load_workouts()) + 1,
            'workout_name': data['workout_name'],
            'duration': int(data['duration']),
            'calories': int(data.get('calories', 0)),
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        workouts = load_workouts()
        workouts.append(new_workout)
        save_workouts(workouts)
        
        return jsonify({'message': 'Workout added successfully', 'workout': new_workout}), 201
        
    except ValueError:
        return jsonify({'error': 'Invalid data types'}), 400

@app.route('/health')
def health_check():
    """Health check endpoint for monitoring"""
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 