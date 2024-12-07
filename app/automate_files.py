def create_file():
    content="""
         this a test file 
         line 2
         line 3
           """
    try:
        with open("./test.txt",'x') as file:
            file.write(content)
    except FileExistsError as e:
        print("file exist")
     

def read_file():
    with open("./test.txt","r") as file:
        content_file=file.read()
        print(content_file)

###################################################################
# using a pathlib 
def pathlib():
    from pathlib import Path
    policy_json = {
    "Version": "2012-10-17",
    "Statement": {
        "Effect": "Allow",
        "Action": "service-prefix:action-name",
        "Resource": "*",
        "Condition": {
            "DateGreaterThan": {"aws:CurrentTime": "2017-07-01T00:00:00Z"},
            "DateLessThan": {"aws:CurrentTime": "2017-12-31T23:59:59Z"}
        }
    }
}



if __name__== "__main__" :
    #create_file()
    #read_file()



