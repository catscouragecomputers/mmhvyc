import datetime

username = "mmhvyc"
userInput = username
# user not found, userInput = "username"

fileSize = 32
maxFileSize = 64
# file too big, fileSize = 65

acceptedFileTypes = ['.doc', '.docx', '.pdf']
attachedFile = "assignment.docx"
# incorrect file type, attachedFile = "assignment.c"

due = datetime.datetime(2019, 9, 24)
submitted = datetime.datetime(2019, 9, 25)
latePenalty = 0.9
# no late penalty, submitted = datetime.datetime(2019, 9, 23)

instructors = ['valettas', 'saab', 'jurczyk', 'wergeles', 'goggins']
# instructor not in system, instructor = 'heinzman'
