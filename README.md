# Awwards

This application allows a user to post a project he/she has created and get it reviewed by his/her peers.

A project can be rated based on 3 different criteria

- Design

- Usability

- Content

These criteria can be reviewed on a scale of 1-10 and the average score is taken.

[Live Demo](#)

## Author
[Koskey Patience](https://github.com/p-koskey)

## User Stories
User would like to:

- View posted projects and their details
- Post a project to be rated/reviewed
- Rate/ review other users' projects
- Search for projects 
- View projects overall score
- View profile page

## Installation and Usage Guide:
- Python 3.8

- Pip

- Django

- Virtual enviroment

- Cloudinary

### Clone the application 
    $ git clone https://github.com/p-koskey/awwards.git
    $ cd uninstagram

### Run the application
- Install virtual environment using 

      $ python3 -m venv venv

- Activate virtual environment using 

      $ . venv/bin/activate

- Install all the dependencies from the requirements.txt file by running 

      $python3 pip install -r requirements.txt

- Create a database and edit the database configurations in settings.py to your own credentials.

- Make migrations

      $ python manage.py makemigrations app=website
      $ python manage.py migrate 
    
- To run the application, in your terminal

      $ python manage.py runserver

## License
This project is licensed under the MIT License.
MIT License
Copyright(2020) Patience Koskey

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


