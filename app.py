from flask import Flask, request, jsonify
from flask import Flask, request, jsonify
from models import db, Flavor, Ingredient, CustomerSuggestion

app = Flask(_name_)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chocolate_house.db'
db.init_app(app)

@app.route('/flavors', methods=['GET', 'POST'])
def manage_flavors():
    if request.method == 'POST':
        data = request.json
        new_flavor = Flavor(name=data['name'], seasonal=data['seasonal'])
        db.session.add(new_flavor)
        db.session.commit()
        return jsonify({"message": "Flavor added!"}), 201
    flavors = Flavor.query.all()
    return jsonify([{'id': f.id, 'name': f.name, 'seasonal': f.seasonal} for f in flavors])

@app.route('/suggestions', methods=['POST'])
def add_suggestion():
    data = request.json
    suggestion = CustomerSuggestion(flavor_name=data['flavor_name'], allergy_concerns=data.get('allergy_concerns'))
    db.session.add(suggestion)
    db.session.commit()
    return jsonify({"message": "Suggestion added!"}), 201

if _name_ == '_main_':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
