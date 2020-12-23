### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

  - Javascript isn't as picky about types (`"1" == 1` --> true) whereas Python is picky about types. (unless we are using `===` in javascript)
  - In JS, comparing two arrays or objects always compares their memory addresses, so two lists with the same data aren't going to be equal. In python, both lists are compared by contents.
  - in JS, indentation is suggested to make the syntax more readable. In Python, indentation IS the syntax for code blocks.

- Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
  can try to get a missing key (like "c") _without_ your programming
  crashing.

  - `my_dict.get("c", 3)`

- What is a unit test?

  - A unit test is a check to determine if a small piece of your code works as intended (typically a function or class method)

- What is an integration test?

  - An integration test is a check to ensure multiple portions of your code all work together to ensure expected output.

- What is the role of web application framework, like Flask?

  - A web framework is in charge of supplying us with tools to help us handle HTTP requests, interface with Databases, and generating dynamic web pages among other things.

- You can pass information to Flask either as a parameter in a route URL
  (like `'/foods/pretzel'`) or using a URL query param (like
  `'foods?type=pretzel'`). How might you choose which one is a better fit
  for an application?

  - We should generally use route parameters when routing to the "subject" of the page
  - We should use URL query parameters when we are trying to give additional / refined details about the subject of an existing page

- How do you collect data from a URL placeholder parameter using Flask?
  - @app.route("/users/<username>)
    def user(username):
    name = users[username]
  - we wrap the URL placeholder in GT/LT signs (<>) and pass the **exact** name of that variable into the function for later use.
- How do you collect data from the query string using Flask?

  - @app.route("/search")
    def search():
    search_term = request.args["term"]
  - In this example, if a user sent an HTTP request in for _"/search?term=dogs"_ then the request.args[**"term"**] would contain "dogs" and we can use that for a DB query and so on.

- How do you collect data from the body of the request using Flask?

  - `request.form` (used for HTML post form or JS request that isn't JSON encoded)
  - `request.values` (combines request.args and request.form, but defaults to args if duplicate keys exist)
  - `request.json` (used for JSON encoded JS AJAX requests)

- What is a cookie and what kinds of things are they commonly used for?

  - Cookies help to save state data in a web session with a particular domain.
  - They allow us to store small bits of information in a client browser that we can reference later.
  - A cookie contains name/string-value pairs of information.
  - A cookie is different than local storage because localstorage persists even after the browser is closed.
  - Once a cookie is set, it is sent on every request to that domain/sub-domain (whichever is specified in the cookie)

- What is the session object in Flask?

  - The session object is a lot like a cookie, except that it preserves data types in a dictionary style.
  - A session is signed so a user cannot modify the data.
  - accessed like so: `session["name_of_variable"]`

- What does Flask's `jsonify()` do?
  - jsonify() is used to send a JSON response back to a browser. We can then manipulate this JSON data in our front-end JS code or send this response directly to the client browser for API development.
