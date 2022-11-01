# AirBnB Clone
First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

# Description
A clone of the popular vacation rental company
To see more commands type `(hbnb) help`

# Example
Type this on your terminal to enter the interactive mode on you command line
`./console.py` \
type quit or an EOF (CTRL+D on Linux) to quit the session \
`(hbnb) quit` to quit the session \

Accepted model classes are `BaseModel, User, City, Place, Amenity, Review, State\` 
shows all data stored for the model class `(hbnb) show BaseUser` \

`(hbnb) help`\
`Documented commands (type help <topic>):`
`========================================`\
`EOF  User  all  create  destroy  help  quit  show  update`

When trying to create a model that is not accepted\
`(hbnb) create BaseUser`\
`** class doesn't exist **`

Model that exist returns the instance ID\
`(hbnb) create BaseModel` \
`8e5b48c3-24fb-41fe-97b3-431996048ba5`

If the instance ID does not exit it returns \
`(hbnb) show User 8e5b48c3-24fb-41fe-97b3-431996048ba5`\
`** class doesn't exist **`
