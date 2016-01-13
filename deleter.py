import filecmp
import os.path

def removing_files(dictionary):
	"""
	 	Se le pasa un diccionario con todos los archivos que se repiten, no se elimina el primer archivo
	 	Se le pregunta al usuario si quiere eliminar recursivamentme todos los archivos
	"""
	i = 0
	os.system('clear')
	for d in dictionary.values():
		if i == 0:
			print ""			
			print "This is the master file, this file won't be deleted  :  '" + d + "'"
			print ""
			print "This files will be deleted : "
		else:
			print d
		i+=1

	not_empty = True
	answer = raw_input('Are you sure you want to delete these repeatable files (Yes, No) ? : ')
	
	if answer == 'Yes':
		os.system('clear')
		print "The following files have been deleted"
		while not_empty:
			key_dictionary = dictionary.keys()[0]
			x = dictionary[key_dictionary]

			temporal_list = dictionary.copy()
			del temporal_list[key_dictionary]

			list_keys_delete = []

			for key, y in temporal_list.iteritems():
				if filecmp.cmp(x , y):
					print y 
					#del temporal_list[key_dictionary]
					list_keys_delete.append(key)
					os.remove(y)


			for key in list_keys_delete:
				del temporal_list[key]

			dictionary = temporal_list

			if not dictionary:
				not_empty = False
	else:
		print "None file was deleted"

def read_files(dictionary):
	if not dictionary:
		print " None files were founded"
	else:
		for d in dictionary:
			if dictionary[d]['coincidences'] > 0 :
				path_files_list = dictionary[d]['path_size'].keys()
				path_files = dict(zip(range(0, len(path_files_list)), path_files_list ))


				removing_files(path_files)

			
