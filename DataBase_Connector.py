import mysql.connector

from main import CRAWLED_FILE, QUEUE_FILE

# Read from files
def read_from_files(file_path):
    file_content_list = []
    file = open(file_path)
    for f in file:
        read = file.readline()
        file_content_list.append(read)
    return file_content_list


class Connect_to_database():
    def __init__(self,project_name="",domain_name="",Queue_path = "", Crawled_path=""):
        self.mydb = mysql.connector.connect(host="localhost",user="Kshitij",password = "",database ="kshitij")
        print(self.mydb)
        self.cursor = self.mydb.cursor()
        self.project_name = project_name
        self.domain_name = domain_name
        self.queue_path = Queue_path
        self.crawler_path = Crawled_path
    def check_tables(self):
        self.tables = self.cursor.execute("show tables")
        self.rows = self.cursor.fetchall()
        print(self.rows)
    def file_to_table(self):
        #self.read_queue = read_from_files(self.queue_path)
        self.read_crawled = read_from_files(self.crawler_path)
        for i in range(len(self.read_crawled)):
            string_query = "insert into reddit values({},'{}')".format(i,self.read_crawled[i])
            self.insert = self.cursor.execute(string_query)
            self.mydb.commit()
    def check_content(self):
        self.show = self.cursor.execute("select * from reddit")
        self.rows = self.cursor.fetchall()
        return self.rows
        #print(self.rows)

    def empty_table(self):
        self.del_all = self.cursor.execute("delete from reddit")
        self.mydb.commit()
        print("All rows removed")



#check = Connect_to_database(Queue_path=QUEUE_FILE,Crawled_path=CRAWLED_FILE)

#check.file_to_table()

