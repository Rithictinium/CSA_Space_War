from database import Database

db = Database()

def display_players():
    players = db.get_all_players()  
    if players:
        print("ID | Name      | Age | Wins | Losses")
        print("-" * 30)
        for player in players:
          
            print(f"{player[0]:<3} | {player[1]:<10} | {player[2]:<3} | {player[3]:<4} | {player[4]:<6}")
    else:
        print("No players found in the database.")

display_players()


db.close()
