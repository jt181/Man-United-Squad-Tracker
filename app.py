import os
from flask import Flask, render_template, request, redirect, url_for, flash
from models.player import db, Player

app = Flask(__name__)

app.secret_key = "replace_with_a_real_secret_key"

# DB Config (using SQLite locally for now)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///manutd.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route("/")
def home():
    return redirect(url_for("list_players"))

@app.route("/players")
def list_players():
    players = Player.query.all()
    return render_template("index.html", players=players)

@app.route("/players/add", methods=["GET", "POST"])
def add_player():
    if request.method == "POST":
        name = request.form["name"]
        position = request.form["position"]
        age = int(request.form["age"])
        appearances = int(request.form["appearances"])

        # Optional stats
        goals = request.form.get("goals")
        goals = int(goals) if goals else None

        assists = request.form.get("assists")
        assists = int(assists) if assists else None

        clean_sheets = request.form.get("clean_sheets")
        clean_sheets = int(clean_sheets) if clean_sheets else None

        new_player = Player(
            name=name,
            position=position,
            age=age,
            goals=goals,
            assists=assists,
            appearances=appearances,
            clean_sheets=clean_sheets
        )
        db.session.add(new_player)
        db.session.commit()
        flash(f"Added {new_player.name}!", "success")
        return redirect(url_for("list_players"))

    return render_template("add_player.html")

@app.route("/players/edit/<int:player_id>", methods=["GET", "POST"])
def edit_player(player_id):
    player = Player.query.get_or_404(player_id)

    if request.method == "POST":
        player.name = request.form["name"]
        player.position = request.form["position"]
        player.age = int(request.form["age"])
        player.appearances = int(request.form["appearances"])

        goals = request.form.get("goals")
        player.goals = int(goals) if goals else None

        assists = request.form.get("assists")
        player.assists = int(assists) if assists else None

        clean_sheets = request.form.get("clean_sheets")
        player.clean_sheets = int(clean_sheets) if clean_sheets else None

        db.session.commit()
        flash(f"Updated {player.name}!", "success")
        return redirect(url_for("list_players"))

    return render_template("edit_player.html", player=player)

@app.route("/players/delete/<int:player_id>", methods=["POST"])
def delete_player(player_id):
    player = Player.query.get_or_404(player_id)
    db.session.delete(player)
    db.session.commit()
    flash(f"Deleted {player.name}.", "warning")
    return redirect(url_for("list_players"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)