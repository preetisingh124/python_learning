health_file = open(r"C:\Users\HP\Documents\file_handling\healthcare.txt",'r')
health_list = health_file.readlines()
health_list_cleaned = []
for tag in health_list:
    health_list_cleaned.append(tag.strip())
health_file.close()
for tag in health_list_cleaned:
    if tag in ["ice cream","garlic","petrol","diesel"]:
        health_list_cleaned.remove(tag)
health_cleaned_file = open(r"C:\Users\HP\Documents\file_handling\healthcare.txt",'w')
for tag in health_list_cleaned:
    health_cleaned_file.write(tag+ "\n")
health_cleaned_file.close()# not run but showing any error.