from app import app
from models.player import db, Player

with app.app_context():
    players = [
        Player(
            name="Andre Onana",
            position="Goalkeeper",
            age=29,
            clean_sheets=15,
            appearances=48
        ),
        Player(
            name="Altay Bayindir",
            position="Goalkeeper",
            age=27,
            clean_sheets=1,
            appearances=2
        ),
        Player(
            name="Tom Heaton",
            position="Goalkeeper",
            age=39,
            clean_sheets=0,
            appearances=1
        ),
        Player(
            name="Noussair Mazraoui",
            position="Defender",
            age=27,
            goals=1,
            assists=3,
            appearances=35
        ),
        Player(
            name="Matthijs de Ligt",
            position="Defender",
            age=25,
            goals=3,
            assists=1,
            appearances=40
        ),
        Player(
            name="Harry Maguire",
            position="Defender",
            age=32,
            goals=2,
            assists=1,
            appearances=28
        ),
        Player(
            name="Lisandro Martinez",
            position="Defender",
            age=27,
            goals=1,
            assists=2,
            appearances=36
        ),
        Player(
            name="Tyrell Malacia",
            position="Defender",
            age=25,
            goals=0,
            assists=1,
            appearances=10
        ),
        Player(
            name="Leny Yoro",
            position="Defender",
            age=19,
            goals=1,
            assists=0,
            appearances=25
        ),
        Player(
            name="Diogo Dalot",
            position="Defender",
            age=26,
            goals=2,
            assists=4,
            appearances=42
        ),
        Player(
            name="Luke Shaw",
            position="Defender",
            age=29,
            goals=0,
            assists=2,
            appearances=20
        ),
        Player(
            name="Jonny Evans",
            position="Defender",
            age=37,
            goals=0,
            assists=0,
            appearances=15
        ),
        Player(
            name="Harry Amass",
            position="Defender",
            age=18,
            goals=0,
            assists=0,
            appearances=5
        ),
        Player(
            name="Victor Lindelof",
            position="Defender",
            age=30,
            goals=0,
            assists=0,
            appearances=12
        ),
        Player(
            name="Patrick Dorgu",
            position="Defender",
            age=20,
            goals=1,
            assists=2,
            appearances=18
        ),
        Player(
            name="Bruno Fernandes",
            position="Midfielder",
            age=30,
            goals=12,
            assists=10,
            appearances=46
        ),
        Player(
            name="Mason Mount",
            position="Midfielder",
            age=26,
            goals=4,
            assists=5,
            appearances=30
        ),
        Player(
            name="Christian Eriksen",
            position="Midfielder",
            age=33,
            goals=2,
            assists=3,
            appearances=22
        ),
        Player(
            name="Casemiro",
            position="Midfielder",
            age=33,
            goals=3,
            assists=2,
            appearances=28
        ),
        Player(
            name="Manuel Ugarte",
            position="Midfielder",
            age=24,
            goals=1,
            assists=2,
            appearances=38
        ),
        Player(
            name="Kobbie Mainoo",
            position="Midfielder",
            age=20,
            goals=5,
            assists=4,
            appearances=40
        ),
        Player(
            name="Toby Collyer",
            position="Midfielder",
            age=21,
            goals=0,
            assists=1,
            appearances=8
        ),
        Player(
            name="Daniel Gore",
            position="Midfielder",
            age=20,
            goals=0,
            assists=0,
            appearances=4
        ),
        Player(
            name="Marcus Rashford",
            position="Forward",
            age=27,
            goals=10,
            assists=6,
            appearances=40
        ),
        Player(
            name="Rasmus Højlund",
            position="Forward",
            age=22,
            goals=14,
            assists=3,
            appearances=38
        ),
        Player(
            name="Alejandro Garnacho",
            position="Forward",
            age=20,
            goals=10,
            assists=9,
            appearances=42
        ),
        Player(
            name="Joshua Zirkzee",
            position="Forward",
            age=24,
            goals=8,
            assists=4,
            appearances=35
        ),
        Player(
            name="Amad Diallo",
            position="Forward",
            age=22,
            goals=7,
            assists=5,
            appearances=30
        ),
        Player(
            name="Antony Matheus dos Santos",
            position="Forward",
            age=25,
            goals=3,
            assists=2,
            appearances=20
        ),
        Player(
            name="Ethan Wheatley",
            position="Forward",
            age=19,
            goals=1,
            assists=0,
            appearances=5
        )
    ]

    db.session.bulk_save_objects(players)
    db.session.commit()

    print("All players seeded successfully!")
