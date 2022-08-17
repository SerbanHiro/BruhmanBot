from replit import db
# UPDATE WORDS FROM db["cuvinte"]
def update_cuvinte_bruhman(cuvinte_noi_bruhman):
  # CURRENT DATABASE
  if "cuvinte_bruhman" in db.keys():
    print(db["cuvinte_bruhman"])
    if db["cuvinte_bruhman"].count(cuvinte_noi_bruhman) == 1:
      return 1
    else:
      cuvinte = db["cuvinte_bruhman"]
      cuvinte.append(cuvinte_noi_bruhman)
      db["cuvinte_bruhman"] = cuvinte

  # INITIALIZE DATABASE EXCEPTION
  else:
    db["cuvinte_bruhman"] = [cuvinte_noi]