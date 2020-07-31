# Library Catalog

Web Programming with Python and JavaScript


project1:
    application.py
    has all the functions and renders html templates or redirect to html
### Files:
    templates/
        book.html
        books.html
        login.html
        register.html
        index.html
        success.html
        error.html
        layout.html
    templates/includes
        _messages.html
        _navbar.html
        _formhelpers.html

    static/
        styles/styles.css
        img/ some images that are used from cloudinary
## Usage
The home page (index.html) only gives an option to register or login, taking the user to register.html

or login.html
After being registered, the user has to login, and it is taken to books page to search for a book. 

In books.html the user can search for a particular book, by isbn or author+title. 

books.html renders results, of either a book, or list of books if search yielded more results. 

Each book is a link for book.html with /isbn that the user can go to find out the reviews on the 

book or to post its own review.

Once the review is posted, the user is thanked if successful, and taken back to the books page  
If review post resulted in error, error.html the user is informed.  
If review post is success, success.html is shown.  

