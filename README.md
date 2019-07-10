# Neighbourhood
#### A python application based on Django framework, 2019
####  **[Maurine sinami](https://github.com/maurinesinami)**
## Description
An application that keeps you in the loop of all the things happening in your neighborhood. A user can create a profile which is open to all users. They can also post events or occurrences in their hood, and view other people's businesses within their hood.
## Setup/Installation Requirements
* Python3.6 and above
* Postgresql for databases
* On this repository,, click on the green 'clone or download' button
* navigate to the cloned folder by `cd neighbourhood`
* Create a virtual environment using `virtualenv virtual` command
* Run `source virtual/bin/activate`
* Install Django  using `pip install django=1.11.5`
* create new file `requirements.txt` and run `pip freeze > requirements.txt`
* run `python3.6 manage.py runserver `
* for quick debugging run `python manage.py check` or  `python manage.py test album`
## Known Bugs
NO known Bugs.
## Behavior Driven Development

| Behaviour| Input | Output |
| ------------- | ----------------- | ------------------ |
| Display all data on database  | "https://sinamihome@heroku.com"   | Loads events in the hood  |
| Save uploaded posts | Upload event | Saves event |
| Update images as admin | update image at localhost/admin | Updates |
| Post events as user | update image at create/update/ route | Updates |
| Search by business| search businesses| returns businesses in region|



## Technologies Used
## main languages used are
* Python
* Bootstrap
* WhiteNoise
* Django
* PostgreSQL Database
* JavaScript
* CSS


## Support and contact details
Please reach out to me at 'maurine.sinami@gmail.com' for any queries concerning this or any other code.
### License
MIT LICENSE [Maurine sinami][2019]