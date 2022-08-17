from replit import db
# UPDATE ANSWERS FROM db["cuvinte"]
def update_cuvinte(cuvinte_noi):
  # CURRENT DATABASE
  if "cuvinte" in db.keys():
    print(db["cuvinte"])
    if db["cuvinte"].count(cuvinte_noi) == 1:
      return 1
    else:
      cuvinte = db["cuvinte"]
      cuvinte.append(cuvinte_noi)
      db["cuvinte"] = cuvinte

  # INITIALIZE DATABASE EXCEPTION
  else:
    db["cuvinte"] = [cuvinte_noi]