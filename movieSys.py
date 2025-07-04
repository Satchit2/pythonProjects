#Current Status: Bugged
#Desc: Menu function not working and program directly shifting to Add
import sys

globalMovieList = []
def menu():
    cmdDir = {
        "ADD" : add,
        "SHOW" : show,
        "FIND" : findMovie,
        "Q" : sysQuit,
        "CL" : cmdList
    }
    cmdR=input("What Would you like to do? (Enter CL for command list): ").upper()
    if cmdR not in cmdDir.keys():
        print("Invalid Command")
        menu()
    cmdDir[cmdR]()
    return 1

def add():
    print("Type 'Menu' to return to Main Menu")
    movieAdd = input("Enter the title of movie to add to Your Collection:")
    if movieAdd.lower()=="menu":
        menu()
        return
    cnf = input(f"Are you sure you want to add {movieAdd} to Your Collection? (Y/N)").upper()
    if cnf=='Y':
        globalMovieList.append(movieAdd)
        menuRet()
        add()
        return
    elif cnf=='N':
        add()
        return
    else:
        print("Invalid Entry")
        add()
    menu() 
    return

def show():
    print("Your Movie Collection:")
    if len(globalMovieList)==0:
        print("Nothing to see here! Add a movie first.")
        menu()
        return
    for c,i in enumerate(globalMovieList,start=1):
        print(f"{c}. {i}")
    menu()
    return

def findMovie():
    movieFind = input("Enter the movie you would like to find from your list: ")
    searchResult = [mov for mov in globalMovieList if mov.lower()==movieFind.lower()]
    if len(searchResult)==0:
        print("Movie Not Found. Maybe the time for a new entry!")
    elif len(searchResult)==1:
        print(f"We found the movie in Your Collection! \n  {globalMovieList.index(searchResult[0])+1}. {searchResult[0]}")
    else:
        print("We found multiple entries for this movie!")
        startVal=0
        for i in range(len(searchResult)):
            indexVal=globalMovieList.index(searchResult[i], startVal)+1
            print(f"{indexVal}. {searchResult[i]}")
            startVal=indexVal
    menu()
    return

def cmdList():
    print(
        "ADD - Adds a new movie to Your Collection \n"
        "CL - Shows the list of available commands \n"
        "FIND -  Finds if a movie is already present in Your Collection \n"
        "Q - Quits the program \n"
        "SHOW - Shows the movies in Your Collection \n"
        )
    menu()
    return

def menuRet():
    cnf = input("Would you like to go back to Main Menu? (Y/N)").upper()
    if cnf=='Y':
        menu()
    elif cnf=='N':
        return
    else:
        print("Invalid Entry")
        menuRet()
    return

def sysQuit():
    sys.exit()
    return


#Main

print("Welcome to the Movie Collection Organizer!")
cmdList()
menu()