import sqlite3 as lite

#//functionality goes here
class DatabaseManage():
    def __init__(self):
        global con
        try:
            con = lite.connect('courses.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS COURSE(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception as e:
            print("unable to create a db !" + str(e))
            return

    #todo: insert data
    def insert_data(self,data):
        try:
            with con:

                cur = con.cursor()
                cur.execute(
                    "INSERT INTO course(name,description,price, is_private) VALUES(? ,?,?,?)", data )

            return True
        except Exception:
            return 


    #todo: fetch data
    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall()
        except Exception:
            return 


    #todod:delete data
    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM COURSE WHERE ID = ? "
                cur.execute(sql, [id])
                return True
        except Exception:
            return 



    #todo:provide interface to user

def main(args=None):
    print("#"*20)
    print("\n :: COURSE MANAGEMENT :: \n")
    print("#"*20)


    db = DatabaseManage()

    print("#"*20)
    print("\n :: USER MANUAL ::\n ")
    print("#"*20)
    print('press 1, Insert a new course')
    print('press 2, show all courses')
    print('press 3, Delete a course(need id of course)\n')
    print("#"*20)
    print("\n")

    choice = input("\n Enter a choice: ")
    if choice == "1":
        name = input("\n enter course name:")
        description = input("\n enter course description:")
        price = input("\n enter course price")
        private = input("\n Is this course private (0/1): ")

        if db.insert_data([name,description, price,private]):
            print("coursev was inserted successfully")
        else:
            print("oops something is wrong...")


    elif choice == "2":
        print("::\n course list :: \n")
        for index, item in enumerate(db.fetch_data()):
            print("\n sl no : " + str(index + 1))
            print("course ID : " + str(item[0]))
            print("course Name : " + str(item[1]))
            print("course Description: " + str(item[2]))
            print("course Price: " + str(item[3]))
            private = 'yes' if item[4] else 'no'
            print("Is Private :" + private)
            print("\n")

    elif choice == "3":   
        record_id = input("enter the course ID:")

        if db.delete_data(record_id):
            print("course was deleted:")
        else:
            print("oops something went wrong")

    else:
        print("\n BAD CHOICE")


if __name__ == '__main__':
    main()

