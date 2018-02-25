## Main Menu
import os, pyperclip
try:
	import readline
except:
	pass

def print_mainmenu():
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. CREATE"
    print "2. CONNECT"
    print "3. UPDATE"
    print "4. MOVE"
    print "5. DELETE"
    print "6. READ"
    print "7. Exit"
    print 67 * "-"

def print_createmenu():
    print 30 * "-", "CREATE", 30 * "-"
    print "Syntax:\t \"name\" [\":label1:label2...\"]"
    print "Only Enter - back"
    params = raw_input(": ")
    if not params:
        return
    os.system("./create.sh "+params)
    print

def print_connectmenu():
    print 30 * "-", "CONNECT", 30 * "-"
    print "Syntax for id1 ->\tid2 :\t id1 id2"
    print "Syntax for id1 -r->\tid2 :\t id1 id2 'rel'"
    print "Syntax for id1 -r->\tid2 :\t id1 id2 'rel' 'specialattr1: bla, specialattr2:blub'"
    print "Escape quotes e.g. 'URL:\\\"https://github.com/andrew-d/static-binaries\\\"'"
    print "Only Enter - back"
    params = raw_input(": ")
    if not params:
        return
    os.system("./connect.sh "+params)
    print

def print_updatemenu():
    print 30 * "-", "UPDATE", 30 * "-"
    print "l/L. Add Label on Node"
    print "p/P. Property"
    print "Only Enter - back"
    choice = raw_input(": ")
    if not choice:
        return

    if choice.lower() == "l":
        print "Syntax:\t id \":labelname\""
        print "Only Enter - back"
        params = raw_input(": ")
        if not params:
            return
        os.system("./update.sh l " + params)
        print

    elif choice.lower() == "p":
        print "n/N. Property on Node"
        print "r/R. Property on Relationship"
        print "Only Enter - back"
        choice = raw_input(": ")
        if not choice:
            return

        if choice.lower() == "n":
            print "Syntax:\t node_id \"propertyname\" \"propertyvalue\""
            print "Only Enter - back"
            params = raw_input(": ")
            if not params:
                return
            os.system("./update.sh p n " + params)
            print

        elif choice.lower() == "r":
            print "Syntax:\t relationship_id \"propertyname\" \"propertyvalue\""
            print "Only Enter - back"
            params = raw_input(": ")
            if not params:
                return
            os.system("./update.sh p r " + params)
            print


def print_movemenu():
    print 30 * "-", "MOVE", 30 * "-"
    print "r/R. Relationship"
    print "Only Enter - back"
    choice = raw_input(": ")
    if not choice:
        return

    if choice.lower() == "r":
        print "r/R. new root node"
        # print "t/T. new target node"
        print "Only Enter - back"
        choice = raw_input(": ")
        if not choice:
            return

        if choice.lower() == "r":
            print "Syntax:\t new_root_id1 to_id2 \"rel\" "
            print "Only Enter - back"
            params = raw_input(": ")
            if not params:
                return
            os.system("./connect.sh " + params)
            print "\n\nSyntax:\t relationship_id_to_delete"
            print "Only Enter - back"
            relid = raw_input(": ")
            if not relid:
                return
            os.system("./delete.sh r " + relid)
            print


def print_deletemenu():
    print 30 * "-", "DELETE", 30 * "-"
    print "n/N. Node"
    print "r/R. Relationship"
    print "Only Enter - back"
    choice = raw_input(": ")

    if choice.lower() == "n":
        print "Syntax:\t id"
        print "Only Enter - back"
        id = raw_input(": ")
        if not id:
            return
        os.system("./delete.sh n " + id)
        print

    if choice.lower() == "r":
        print "Syntax:\t relationship_id"
        print "Only Enter - back"
        relid = raw_input(": ")
        if not relid:
            return
        os.system("./delete.sh r " + relid)
        print

def print_readmenu():
    print 30 * "-", "READ", 30 * "-"
    print "a/A. Output all"
    print "n/N. Node Environment"
    print "Only Enter - back"
    choice = raw_input(": ")

    if choice.lower() == "a":
        outputstring = "MATCH (n) RETURN n LIMIT 500"
        print outputstring + """

copied to clipboard"""
        pyperclip.copy(outputstring)
        print

    if choice.lower() == "n":
        print "Syntax:\t id"
        print "Only Enter - back"
        id = raw_input(": ")
        if not id:
            return
        outputstring = """
MATCH (n) WHERE ID(n) = """+id+""" 
MATCH (n) -[r]- ()
MATCH () -[r]- (n)
RETURN n,r LIMIT 10"""
        print outputstring + """

copied to clipboard"""
        pyperclip.copy(outputstring)
        print

## Main

loop=True
wrongOptionString = "Wrong option selection. Enter any key to try again.."

while loop:          ## While loop which will keep going until loop = False
    print_mainmenu() ## Displays menu
    try:
        choice = int(raw_input("Enter your choice [1-5]: "))
    except Exception:
        choice = 99

    if choice==1:
        print_createmenu()
    elif choice==2:
        print_connectmenu()
    elif choice==3:
        print_updatemenu()
    elif choice==4:
        print_movemenu()
    elif choice==5:
        print_deletemenu()
    elif choice==6:
        print_readmenu()
    elif choice==7:
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input(wrongOptionString)
