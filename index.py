from scanner import scanner_files
from deleter import removing_files
from deleter import read_files


dictionary = {}
file_type = ""

answer_question = False
while not answer_question:
	path = raw_input('Write the complete path you want to scan ex: "/home/pepe" ? :  ')
	if len(path) > 0 :
		answer_question = True

answer_question = False
while  not answer_question : 
	file_type = raw_input('Write file type ex : "mp3, pdf" , (leave blank to scan all files)  ? :  ')
	if file_type == "" or len(file_type) > 0 :
		answer_question = True


scanner_files(path, file_type, dictionary)
read_files(dictionary)	