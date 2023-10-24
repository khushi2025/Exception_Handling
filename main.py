#FileNotFoundError
# with open("data.txt",mode="r") as file:
#     file.read()

#KeyError
# a_dict={"key":"value"}
# value=a_dict["non_existing_key"]
# print(value)

#IndexError
# fruits=["mango","apple","orange"]
# fruit_item=fruits[3]
# print(fruit_item)

#TypeError
# text="abc"
# print(text+5)

#Exception Handling
#There are 4 keywords used to handle an exception in our code:
#1 try - Something that might cause an exception
#2 except - Do this if there was an exception, this is never written alone because in that case if in thr try block there is some other type of error,
#           it will not be reflected in the console and  the code will execute, ignoring that error completely. Instead, we write, except followed by the type of error we are expecting might occur.
#3 else - Do this if there was no exception
#4 finally - Do this no matter what happens
#raise - We can alse raise our error by 'raise' keyword.
#eg:
# try:
#     file=open("data.txt")
#     a_dict={"key":"value"}
#     print(a_dict["dkjsah"])
# except FileNotFoundError:
#     file=open("data.txt",mode="w")
#     file.write("fisuhfajcki")
# except KeyError as error:
#     print(f"The key {error} doesn't exists.")
# else:
#     content=file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up!")
#     # file.close()
#     # print("File was  closed.")
height=float(input("Height: "))
weight=int(input("Weight: "))
if height>3:
    raise ValueError("Human height should not be more than 3 meters.")
bmi=weight/height**2
print(bmi)