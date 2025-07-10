from flask import Flask, jsonify, request
from people import Person, Db_operations

people = Db_operations()
people.create_table()

app = Flask(__name__)

# Create a new person
@app.route('/people', methods=['POST'])
def people_create():
    body = request.get_json()
    new_person = Person(body['name'], body['gender'], body['location'], body['dob'])
    id = people.insert_row(new_person)
    person = people.search_row(id)
    if not person:
        return jsonify({'message': 'Failed to fetch inserted person'}), 500
    person_dict = {
        'id': person[0],
        'name': person[1],
        'gender': person[2],
        'location': person[3],
        'dob': person[4]
    }
    return jsonify(person_dict)

# Read a person by ID
@app.route('/people/<id>', methods=['GET'])
def people_read_by_id(id):
    person = people.search_row(int(id))
    if not person:
        return jsonify({'message': 'Person not found'}), 404
    person_dict = {
        'id': person[0],
        'name': person[1],
        'gender': person[2],
        'location': person[3],
        'dob': person[4]
    }
    return jsonify(person_dict)

# Read all people
@app.route('/people', methods=['GET'])
def people_read_all():
    persons_list = people.list_all_rows()
    persons_dict = []
    for person in persons_list:
        persons_dict.append({
            'id': person[0],
            'name': person[1],
            'gender': person[2],
            'location': person[3],
            'dob': person[4]
        })
    return jsonify(persons_dict)

# Update a person
@app.route('/people/<id>', methods=['PUT'])
def people_update(id):
    body = request.get_json()
    old_person_obj = people.search_row(int(id))
    if not old_person_obj:
        return jsonify({'message': 'Person not found'}), 404

    updated_person = (
        body['name'],
        body['gender'],
        body['location'],
        body['dob'],
        int(id)
    )
    people.update_row(updated_person)

    person = people.search_row(int(id))
    person_dict = {
        'id': person[0],
        'name': person[1],
        'gender': person[2],
        'location': person[3],
        'dob': person[4]
    }
    return jsonify(person_dict)

# Delete a person
@app.route('/people/<id>', methods=['DELETE'])
def people_delete(id):
    old_person_obj = people.search_row(int(id))
    if not old_person_obj:
        return jsonify({'message': 'Person not found', 'is_error': 1}), 404
    people.delete_row(int(id))
    return jsonify({'message': 'Person is deleted', 'is_error': 0})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
