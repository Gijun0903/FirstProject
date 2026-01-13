"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, jsonify
from FIrstProject import app
import os

@app.route('/')
@app.route('/home')
def home():
    """Renders the sorry page."""
    return render_template(
        'sorry.html',
        title='I\'m Sorry',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/sorry')
def sorry():
    """Renders the sorry page."""
    return render_template(
        'sorry.html',
        title='I\'m Sorry',
        year=datetime.now().year,
    )

@app.route('/submit_response', methods=['POST'])
def submit_response():
    """Handles the meeting response submission."""
    data = request.get_json()
    
    # Log the response
    response = data.get('response')
    
    # Get the absolute path to save the file
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'meeting_response.txt')
    file_path = os.path.abspath(file_path)
    
    # Print to console so you can see where it's saved
    print(f"Saving response to: {file_path}")
    
    if response == 'yes':
        date = data.get('date')
        time = data.get('time')
        
        # Save to a file so you can see her response
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(f"\n{'='*50}\n")
            f.write(f"Response: YES! 💕\n")
            f.write(f"Date: {date}\n")
            f.write(f"Time: {time}\n")
            f.write(f"Submitted at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"{'='*50}\n")
        
        print(f"YES response saved! Date: {date}, Time: {time}")
        return jsonify({'status': 'success', 'message': 'Meeting scheduled!'})
    else:
        # Save "No" response
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(f"\n{'='*50}\n")
            f.write(f"Response: No 😢\n")
            f.write(f"Submitted at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"{'='*50}\n")
        
        print("NO response saved!")
        return jsonify({'status': 'success', 'message': 'Response recorded'})