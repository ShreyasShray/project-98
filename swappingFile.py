file1_name = input("Enter first file Name: ")
file2_name = input("Enter second file Name: ")

file1 = open(file1_name, "r")
file2 = open(file2_name, "r")

dataFromFile1 = file1.read()
dataFromFile2 = file2.read()

writeFile1 = open(file1_name, "w")
writeFile2 = open(file2_name, "w")

writeFile1.write(dataFromFile2)
writeFile2.write(dataFromFile1)