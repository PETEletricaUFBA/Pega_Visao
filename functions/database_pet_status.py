import mariadb


def connectPETDB():
    try:
        mydb = mariadb.connect(
            host="localhost",
            user="root",
            password="new_password"
        )

        mycursor = mydb.cursor()

        try:
            mycursor.execute("use pet_database")
            return mydb

        except:
            print("Não foi encontrado a database do PET!")
    except:
        print("Não foi possivel conectar a database!")


def sig_up_petian(name, surname, RFID=0):

    mydb = connectPETDB()
    mycursor = mydb.cursor()

    sql = "INSERT INTO petian (name_pet, surname_pet, cod_RFID) VALUES ('" + str(
        name) + "', '" + str(surname) + "', '" + str(RFID) + "')"

    mycursor.execute(sql)
    mydb.commit()


def set_up_status(pID, status, RFID=0):

    mydb = connectPETDB()
    mycursor = mydb.cursor()

    sql = "UPDATE petian SET status_pet = " + str(status) + ", cod_RFID = "+str(RFID)+" WHERE pet_id = " + str(pID)

    mycursor.execute(sql)
    mydb.commit()

def petian_is_active(pID):
    mydb = connectPETDB()
    mycursor = mydb.cursor()

    sql = "SELECT status_pet FROM petian WHERE pet_id = " + str(pID) + " LIMIT 1"

    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    return myresult
