import json
from app.models import District, Street, Volunteer
from app import app, db


def read_json(json_path):
    with open(json_path, 'r', encoding='utf-8') as file:
        contents = file.read()
    if contents:
        return json.loads(contents)
    return []


def add_volunteers(json_path):
    volunteers = read_json(json_path)
    for id, data in volunteers.items():
        volunteer = Volunteer(id=id, name=data['name'], userpic=data['userpic'], phone=data['phone'])
        db.session.add(volunteer)
    db.session.commit()


def add_streets(json_path):
    streets = read_json(json_path)
    for id, data in streets.items():
        street = Street(id=id, title=data['title'])
        volunteers = data['volunteer']
        for volunteer_id in volunteers:
            volunteer = db.session.query(Volunteer).get(volunteer_id)
            street.volunteers.append(volunteer)
        db.session.add(street)
    db.session.commit()


def add_districts(json_path):
    districts = read_json(json_path)
    for id, data in districts.items():
        district = District(id=id, title=data['title'])
        streets = data['streets']
        for street_id in streets:
            street = db.session.query(Street).get(street_id)
            district.streets.append(street)
        db.session.add(district)
    db.session.commit()


def main():
    with app.app_context():
        add_volunteers('volunteers.json')
        add_streets('streets.json')
        add_districts('districts.json')


if __name__ == '__main__':
    main()
