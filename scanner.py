import os.path

def scanner_files(path, file_type, dictionary):
	"""Escanea todos los archivos en la ruta seleccionada, recursivamente, si se eligio una extension, solo elegira estos
		Trae los archivos en un diccionario, donde el indice es el nombre del archivo
			ademas tiene  una variable llamada "coincidences" que dice la cantidad de veces que se encontro el archivo
			en la variable "path_size" indica la ruta del archivo y el peso de este
	"""
	files = os.listdir(path)

	for f in files:	
		path_file = path + "/" + f
		is_file = os.path.isfile(path_file)

		if is_file == False:
			new_path = path_file
			scanner_files(new_path, file_type, dictionary)
		elif f[0] != ".":
			file_size = os.path.getsize(path_file)

			if file_type == "" or os.path.splitext(f)[1] == "."+file_type :
				name_file = f
				if name_file in dictionary:
					dictionary[name_file]['coincidences'] += 1 
					dictionary[name_file]['path_size'].update({path_file : file_size})
				else:
					dictionary[name_file] = {'coincidences': 0}
					dictionary[name_file]['path_size']= {path_file : file_size}
