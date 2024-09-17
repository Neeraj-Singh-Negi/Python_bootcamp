# Program to generate a text file

f=open("neeraj.txt","w")
f.write("My name is Neeraj Singh Negi")
f.close()

# Program to generate a json file
import json 
	
# python object(dictionary) to be dumped 
dict1 ={ 
	"emp1": { 
		"name": "Mohit", 
		"designation": "programmer", 
		"age": "34", 
		"salary": "54000"
	}, 
	"emp2": { 
		"name": "Rohit", 
		"designation": "Trainee", 
		"age": "24", 
		"salary": "40000"
	}, 
} 
	
# the json file where the output must be stored 
out_file = open("myfile.json", "w") 
	
json.dump(dict1, out_file, indent = 6) 
	
out_file.close() 
