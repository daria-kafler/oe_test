# Octopus Energy technical challenge
Submitted by Daria Kafler.

## How to install and set the project up
- Open the 'Octop' folder in your development environment of choice (VSCode, PyCharm, etc).

From the "OCTOP" folder, 
- Create and activate a virtual environment
  ```
  python -m venv env
  source ./env/bin/activate
  ```
- Install Django with 
  ```
  pip install django
  ```
- Create the database locally with
  ```
  python manage.py migrate
  ```
- Create a super user in Django, so that you can later access the Django admin panel
  ```
    python manage.py createsuperuser
  ```
- Run the server with 
  ```
  python manage.py runserver
  ```

## How to use the management command
The management command is located in `octopchallange/management/commands/importflow.py`

To run it, 
- drop a flow file into `octopchallange/sample_data/` (or use one of the existing valid files aready there)
- Run 
  ```
  python manage.py importflow <flow_file_filepath>
  ```
  for example:
  ```
  python manage.py importflow octopchallange/sample_data/ZHV|0000475656|D0010002|D|UDMS|X|MRCY|20.uff
  ```

* In the terminal, you'll see whether it ran successfully. Navigate to [http://127.0.0.1:8000/admin](url) (or [http://localhost:8000/admin](url)) and log into the admin panel with the credentials created for the super user.

* On the admin panel, you should see a section called "Octopchallange", and "Readings" underneath it. Clicking on "Readings" will show you the flow file data, organised in a human friendly way 🎉 


### If I had more time, in the management command I would--
-  Turn the line 'types' ("026=MPAN Cores", "028=Meter/Reading Types" and "030=030Register Readings") into ENUMS, making the `if` statements cleaner and improve readability.
- Refactor the parsing logic into it's own component, to improve readability.
- Add error handling. Currently there is only one small try-except which isn't doing much. I'd add additional error handling for the management command to address invalid data, such as missing required lines.
- Fix the date_time conversion (line 35). Wasn't able to figure out how to directly convert to the format Django wanted, so ended up taking a string and converting into date_tim object, then again into a string formatted to Django's liking.

