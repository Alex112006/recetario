from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

class Platillo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), nullable=False)
    ingrediente = db.Column(db.Text, nullable=False)
    instruccion = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Platillo {self.nombre}>"