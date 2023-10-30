# ***Airbnb - The Console***

<div align="center">
  <a href="https://holbertonschool.uy">
    <img src="https://ml.globenewswire.com/Resource/Download/a08e6c28-55be-44c8-8461-03544f094b38" align="center" height="250" width="800" />
  </a>
</div>

# **Project Description**
The Airbnb - The Console project serves as the first project/step to build a functioning replica of the real Airbnb website. 
This project includes creating objects, learning about file serialization, and creating our first storage engine (the file storage).

![image](https://github.com/DominusJP/holbertonschool-AirBnB_clone/assets/135638564/eebc5b65-2aaf-42af-9402-7bf70550821c)

Diagram that might come in hundy for this project:
![image](https://github.com/DominusJP/holbertonschool-AirBnB_clone/assets/135638564/240fe4fc-d4c5-4407-a6a6-45f72da0a65e)



# **Command Interpreter Description**
In order to start it, write `./console.py` in the terminal
In order to use it, you can use any of the following commands:
- `help` shows a guide for the console
- `create` creates a new ID for the given class
- `show` prints a string representation based on the class name and ID
- `destroy` removes the previous ID from the given instance
- `all` Prints all string representation of all instances based or not on the class name
- `update` Updates an instance based on the class name and ID by adding or updating attribute

# **Example**
Open the console in the terminal
`$ ./console.py`

Open the manual of the console
```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
```

Create an ID for a BaseModel class
```bash
(hbnb) create BaseModel
d5d0cbe6-a256-423f-90e8-802e7eac60f1
```

Print the representation of the class and it's ID
```bash
(hbnb) show BaseModel d5d0cbe6-a256-423f-90e8-802e7eac60f1
[BaseModel] (d5d0cbe6-a256-423f-90e8-802e7eac60f1) {'id': 'd5d0cbe6-a256-423f-90e8-802e7eac60f1', 'created_at': datetime.datetime(2023, 10, 30, 2, 14, 12, 560250), 'updated_at': datetime.datetime(2023, 10, 30, 2, 14, 12, 560271)}
```
Remove the previous ID for the BaseModel instance
```bash
(hbnb) destroy BaseModel d5d0cbe6-a256-423f-90e8-802e7eac60f1
(hbnb) show BaseModel d5d0cbe6-a256-423f-90e8-802e7eac60f1
** no instance found **
```

# **Installation**
1. Copy the repository link and `git clone` in your terminal with it
2. Once you're inside the repository after using `cd`, check if the file `console.py` allows you to execute it
3. Were the last condition not to be the case, execute `chmod u+x console.py` to allow the file to be executed
4. Now you can finally use the console by typing `./console.py` in your terminal!
