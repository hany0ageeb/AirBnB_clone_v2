# 0x04. AirBnB clone - Web framework

## Resources

- [What is a Web Framework?](https://intranet.alxswe.com/rltoken/64SQpOGx46Ljp0zFJchESg)
- [A Minimal Application](https://intranet.alxswe.com/rltoken/NopQlHIr9J_9OPX9XRgfvw)
- [Routing (except “HTTP Methods”)](https://intranet.alxswe.com/rltoken/cQiIhbSdIcg1Ao1MICseBg)
- [Rendering Templates](https://intranet.alxswe.com/rltoken/DBM65T59nySd0ZRlZZ0CXw)
- [Synopsis](https://intranet.alxswe.com/rltoken/5Y_A7XB9Qo1JeZgiSUq0yQ)
- [Variables](https://intranet.alxswe.com/rltoken/ITzobwYP1Lc4KqEUUcYCGw)
- [Comments](https://intranet.alxswe.com/rltoken/ykUFuQSE9KD1M7WGY-4v4w)
- [Whitespace Control](https://intranet.alxswe.com/rltoken/NMLZom50ZVOxQlgYW3rnuQ)
- [List of Control Structures (read up to “Call”)](https://intranet.alxswe.com/rltoken/5AGhzIt0zSpPJh9SFysdMQ)
- [Flask](https://intranet.alxswe.com/rltoken/VJs151_hsE9g7Cw-Pz5bVg)
- [Jinja](https://intranet.alxswe.com/rltoken/2y_hunzGCCvSot06EW67UQ)

## Recommended YouTube playlist to get you started

[Python Flusk Tutorial](https://youtu.be/MwZwr5Tvyxo?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)

## What are web frameworks and why you need them?

- Web applications have evolved at a rate that the usability and interactivity they provide rival that of a native application. The technology and the expertise needed to build tailored solutions that reach this level of proficiency is demanding.
- Thankfully, there are tools that make web application development easier, one of them being a web app framework.

### What are web application frameworks (web frameworks)?

- Web application frameworks: software frameworks that is designed to support the development of web applications including web services, web resources and web API.
- Web frameworks are a piece of software that offers a way to create and run web applications. Thus, you don't need to code on your own and look for probable miscalculations and faults.

### Types of web framework

- As web standards began to advance, the app logic shifted towards the client ensuring smarter communication between the user and the web application. With logic on client-side, they (client) can react swiftly to user input.
- This makes web apps more responsive, easily navigate-able on any device. Thus, we have 2 functions of frameworks:
    1. the one to work on the server side (backend).
    2. to work on the client-side(front-end).

### 1. Server-side Frameworks
- Server-side frameworks handle HTTP requests, database control and management, URL mapping, etc. These frameworks can improve security and form the output data-simplifying the development process
- Some of the top server-side frameworks are:
    - NET (C#)
    - Django (python)
    - Ruby on Rails (Ruby)
    - Express (JavaScript/NodeJS)
    - Symfony (PHP)

### 2. Client-side Frameworks

- Client-side frameworks don't take care of the business logic like the server-side ones.
- They function inside the browser. Therefore, you can enhance and implement new user interfaces.
- Here are some client-side frameworks; all of whom use JavaScript as their programming language:
    - Angular
    - Ember.Js
    - Vue.Js
    - React.JS

### Web Application framework architecture

- Most of the web frameworks depend on the MVC (Model-View-Controller) architecture.

#### Model

The Model comprises of all the data, business logic layers, its guidelines and functions. The Model, upon getting user input data from the Controller, tells the way an updated interface should be displayed directly to the View.

#### View

The View is for the graphical representation of the data like graph or charts etc. It is the apps’ front-end. The View gets the user input and communicates the same to the Controller for examination and then update and reconstructs itself according to the Model’s instructions, or the Controller’s in case the modification requirement is minimum.

#### Controller

The Controller translates the input data into the scope of commands of the previous ones. It is the midway between the Model and the View. It gets the user input from the View; after processing it, the Controller notifies the Model (or View) of the changes required.

## Flask

Flask is a backend micro-framework written in Python for the rapid development process. It is famous for its simplicity and independence. It does not need any external library for work, which makes it beginner-friendly, and many people choose this framework. Flask is generally used for building a REST API.

Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.

```Python
# save this as app.py
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
```

### A Minimal Application

```python
from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"
```

1. First we import Flask class. An instance of this class will be our WSGI application.
2. Next we create an instance of this class. The first argument is the name of the applications's module or package. `__name__` is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.
3. We then use the `route()` decorateor to tell Flask what URL should trigger our function.
4. The function returns the message we want to display in the user's browser. The default content type is HTML.

To run the application, use the `flask` command or `python -m flask`. you need to tell flask where your application is with the `--app` option.
```bash
$ flask --app hello run
```
