from flask import Blueprint, render_template, redirect, request, url_for

from models.base import Session
from models.tour import Tour
# from models.travel Travel

tour_route = Blueprint("tours", "__name__")

@tour_route.get("/")
def index():
    return redirect(url_for("tours.menu"))

@tour_route.get("/menu/")
def menu():
    with Session() as session:
        tours = session.query(Tour).all()
        # travels = session.query(Travel).all()
        
        context = {
            "tours": tours,
            # "travels": travels,
            "title": "ТуріЯ"
        }
        return render_template("menu.html", **context)
    
@tour_route.post("/add_tour/")
def add_tour():
    with Session() as session:
        name = request.form.get("name")
        price = request.form.get("price")

        # travels = request.form.getlist("travels")
        # travels = session.query(travels).where(Travel.id.in_(travels)).all()

        tour = Tour(name=name, price=price)
        session.add(tour)
        session.commit()
        return redirect("/menu/")
    
@tour_route.get("/tour/del/<int:id>>/")
def del_tour(id):
    with Session() as session:
        tour = session.query(Tour).where(Tour.id == id).first()
        session.delete(tour)
        session.commit()
        return redirect(url_for("tours.menu"))
    
@tour_route.get("/poll/")
def poll():
    with Session() as session:
        tours = session.query(Tour).all()
        question = "Який тур тобі сподобався?"
    return render_template("poll.html", question=question, tours=tours)

@tour_route.get("/add_vote/")
def add_vote():
    tour = request.args.get("tour")
    
    with open("data/answers.txt", "a", encoding="UTF-8") as file:
        file.write(tour + "\n")
    
    return redirect(url_for("tours.results"))


@tour_route.get("/results/")
def results():
    with open("data/answers.txt", "r", encoding="UTF-8") as file:
        answers = file.readlines()
        
    return render_template("results.html", answers=answers)