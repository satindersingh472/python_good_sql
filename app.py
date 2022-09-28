
from helpers  import  connect_db, execute_statement, close_connection

def get_all_books():
    cursor = connect_db()
    print(execute_statement(cursor, 'call all_books()'))
    close_connection(cursor)


def get_author_books():
    author_name = input('Please enter the author name to get the book:  ')
    cursor = connect_db()
    results = execute_statement(cursor,'call books_by_author(?)',[author_name])
    close_connection(cursor)
    return results


results = get_author_books()
for result in results:
    print(result[3])
