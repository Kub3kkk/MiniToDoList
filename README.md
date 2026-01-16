# Mini To-Do List Flask

A simple web-based to-do list application built with **Flask**.  
The project allows users to add notes via a form and display them on the same page.


## Technologies used:

 <img src="https://skillicons.dev/icons?i=python,flask,html,Jinja2" />

## Features
- Flask backend
- HTML template rendering with Jinja2
- Add notes using a POST request
- Display notes dynamically in a list

## Project Structure
├── app.py <br>
└── templates <br>
&nbsp;&nbsp;&nbsp;&nbsp;└── index.html

## Requirements
- Python 3.x
- Flask

Install Flask:
```bash
pip install flask
```
Running the application
```bash
python app.py
```
The application will be available at
```
http://localhost/
```
## How It Works
- `GET /` renders `templates/index.html` with the form
- `POST /` receives the submitted note from the form
- Notes are stored in an in-memory Python list
- The list of notes is passed to the template and rendered using a Jinja2 loop
- Data is not persistent and resets when the server restarts
## Notes
- Data is stored only in memory (lost after restart)
- Debug mode is enabled
- Educational / demo project
## Purpose
This project was created for learning purposes to practice and understand the basics of Flask and web application development.
