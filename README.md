# Project 1

Web Programming with Python and JavaScript


project1:
    application.py
    has all the functions and renders html templates or redirect to html

    templates/
        book.html
        books.html
        login.html
        register.html
        index.html
        success.html
        error.html
        review.html

The home page (index.html) only give an option to register or login
After being registered, the user has to login, and it is taken to books page
In books the user can search for a particular book, by isbn or author+title
The same html renders results, of either a book, or list of books 
Each book is also a link that the user can click on to find out the reviews on the book or to post its own review
Once the review is posted, the user is Thanked if successful, and taken back to the books page
If review post resulted in error, the user is informed, and taken back to the books page
There is a link for logout, if user is logged in.

In README.md, include a short writeup describing your project, what’s contained in each file, and (optionally) any other additional information the staff should know about your project.
If you’ve added any Python packages that need to be installed in order to run your web application, be sure to add them to requirements.txt!
