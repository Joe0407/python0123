import models.user as md


def controllerUser():
    user=md.ModelUser()
    data=user.getUser()
    return data


def insertUser(data):
    user=md.ModelUser()
    user.insertUser(data)
    
def UpdateUser(data):
    user=md.ModelUser()
    user.UpdateUser(data)
    
def DeleteUser(data):
    user=md.ModelUser()
    user.DeleteUser(data)