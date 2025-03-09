import pickle

# Create a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "Wonderland"
}

# Open a file in write-binary mode
with open("my_dict1.txt", "wb") as file:
    # Dump the dictionary into the file
    pickle.dump(my_dict, file)

print("Dictionary has been pickled and saved to my_dict.pkl")
'''
myfile=open("my_dict1.txt","rb")
new_dict = pickle.load(myfile)
print(new_dict)
'''