from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory "database"
students = [
    {"id": 1, "name": "Ali", "grade": "A"},
    {"id": 2, "name": "Sara", "grade": "B"}
]
next_id = 3

# Health check
@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'message': 'Flask is running'}), 200

# Get all students
@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify(students), 200

# Get one student
@app.route('/api/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        return jsonify({'error': 'Student not found'}), 404
    return jsonify(student), 200

# Add a student
@app.route('/api/students', methods=['POST'])
def add_student():
    global next_id
    data = request.get_json()
    if not data or 'name' not in data or 'grade' not in data:
        return jsonify({'error': 'name and grade are required'}), 400
    new_student = {'id': next_id, 'name': data['name'], 'grade': data['grade']}
    students.append(new_student)
    next_id += 1
    return jsonify(new_student), 201

# Update a student
@app.route('/api/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        return jsonify({'error': 'Student not found'}), 404
    data = request.get_json()
    if 'name' in data:
        student['name'] = data['name']
    if 'grade' in data:
        student['grade'] = data['grade']
    return jsonify(student), 200

# Delete a student
@app.route('/api/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        return jsonify({'error': 'Student not found'}), 404
    students = [s for s in students if s['id'] != student_id]'status': 'ok', 'message': 'Flask is running'}), 500f __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)