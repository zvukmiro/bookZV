    isbn= '0380795272'
    username = "usernew2"
    review = "5"
    res = db.execute("INSERT INTO reviews (rw_isbn, rw_user, rating) VALUES (:bookNum, :person, :numb)", {"bookNum":isbn, "person":username, "numb":review})
    db.commit()
    #                           name of table(table rows names)             (some names any)      ( match names from VALUES() with variables defined before)

