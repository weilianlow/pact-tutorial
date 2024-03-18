import json

from flask import Flask, request

app = Flask(__name__)


class Student:
    status = 0
    body = None
    error = None


def get_student_json(student: str):
    s = Student()
    if student == 'Amy':
        s.status = 0
        s.body = {'name': 'Amy', 'age': 49, 'education':
            ['Nanyang Technological University', 'Singapore Polytechnic']}
    elif student == 'Ben':
        s.status = 0
        s.body = {'name': 'Benjamin Tan', 'age': 29, 'education':
            ['National University of Singapore', 'National Junior College']}
    else:
        s.status = 1
        s.error = f'{student} is not available'

    return {key: value for key, value in s.__dict__.items() if not key.startswith('__') and not callable(key) and value is not None}


@app.route('/get-student')
def get_student():
    student = request.args.get('name', default='', type=str)
    data = get_student_json(student)
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.run(debug=True)
