from flask import Flask, redirect, render_template, request, flash, url_for
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secretkey'

connect_db(app)
db.create_all()

@app.route('/')
def home():
    pets = Pet.query.all()
    return render_template('pets_list.html', pets=pets)

@app.route('/pets/new')
def add_pet_page():
    form = AddPetForm()
    return render_template('pets_add.html', form=form)

@app.route('/pets', methods=["POST"])
def add_pet():
    form = AddPetForm()
    
    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != 'csrf_token'}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('pets_add.html', form=form)

@app.route('/pets/<int:pet_id>')
def show_pet_page(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    return render_template('pets_pet_detail.html', pet=pet)
    
@app.route('/pets/<int:pet_id>/edit')
def edit_pet_page(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj = pet)
    return render_template('pets_edit.html', pet=pet, form=form)
    
@app.route('/pets/<int:pet_id>', methods=["POST"])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj = pet)
    
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('pets_edit.html', pet=pet, form=form)
    