from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

streets_volunteers_association = db.Table(
    "streets_volunteers",
    db.Column("street_id", db.Integer, db.ForeignKey("streets.id")),
    db.Column("volunteer_id", db.Integer, db.ForeignKey("volunteers.id")),
)


class District(db.Model):
    __tablename__ = "districts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    streets = db.relationship("Street")

    @property
    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
        }


class Street(db.Model):
    __tablename__ = "streets"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    district = db.relationship("District")
    district_id = db.Column(db.Integer, db.ForeignKey('districts.id'))
    volunteers = db.relationship("Volunteer", secondary=streets_volunteers_association, back_populates="streets")

    @property
    def serialize(self):
        volunteers = []
        for volunteer in self.volunteers:
            volunteers.append(volunteer.id)
        return {
            "id": self.id,
            "title": self.title,
            "volunteer": volunteers
        }


class Volunteer(db.Model):
    __tablename__ = "volunteers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    userpic = db.Column(db.String(200))
    phone = db.Column(db.String(20))
    streets = db.relationship("Street", secondary=streets_volunteers_association, back_populates="volunteers")

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "userpic": self.userpic,
            "phone": self.phone
        }

class Request(db.Model):
    __tablename__ = "requests"
    id = db.Column(db.Integer, primary_key=True)
    district = db.relationship("District")
    district_id = db.Column(db.Integer, db.ForeignKey('districts.id'))
    street = db.relationship("Street")
    street_id = db.Column(db.Integer, db.ForeignKey('streets.id'))
    volunteer = db.relationship("Volunteer")
    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteers.id'))
    address = db.Column(db.String(200))
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    text = db.Column(db.String(200))

    @property
    def serialize(self):
        return {
            "id": self.id,
            "district": self.district_id,
            "street": self.street_id,
            "volunteer": self.volunteer_id,
            "address": self.address,
            "name": self.name,
            "surname": self.surname,
            "phone": self.phone,
            "text": self.text,
        }
