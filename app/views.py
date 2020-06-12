from flask import render_template, request, session, redirect, url_for, flash, jsonify
from app import app, db
from app.models import District, Street, Request, Volunteer


@app.route("/", methods=["GET"])
def render_main():
    return render_template('index.html')


@app.route("/districts/", methods=["GET"])
def get_districts():
    districts = db.session.query(District)
    districts_list = []
    for district in districts:
        districts_list.append(district.serialize)
    return jsonify(districts_list)


@app.route("/streets/", methods=["GET"])
def get_streets():
    district_id = request.args.get("district")
    streets = db.session.query(Street)
    if district_id:
        streets = streets.filter(Street.district_id == district_id)
    streets_list = []

    for street in streets:
        streets_list.append(street.serialize)

    return jsonify(streets_list)


@app.route("/volunteers/", methods=["GET"])
def get_volunteers():
    street_id = request.args.get("streets")
    volunteers = db.session.query(Volunteer)
    if street_id:
        street = db.session.query(Street).get(street_id)
        volunteers = volunteers.filter(Volunteer.streets.contains(street))
    volunteers_list = []

    for volunteer in volunteers:
        volunteers_list.append(volunteer.serialize)

    return jsonify(volunteers_list)


@app.route("/helpme/", methods=["GET", "POST"])
def api_get():
    if request.method == "POST":
        data = request.json
        helpme = Request(district_id=data.get("district"),
                         street_id=data.get("street"),
                         volunteer_id=data.get("volunteer"),
                         address=data.get("address"),
                         name=data.get("name"),
                         surname=data.get("surname"),
                         phone=data.get("phone"),
                         text=data.get("text"),
                         )

        db.session.add(helpme)
        db.session.commit()
        return jsonify(), 201, {"status": "success"}
    elif request.method == "GET":
        helpmes = db.session.query(Request)
        helpme_list = []

        for helpme in helpmes:
            helpme_list.append(helpme.serialize)
        return jsonify(helpme_list)
