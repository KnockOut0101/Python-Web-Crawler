import tkinter as tk
from tkinter import Pack, ttk, Text
from operator import itemgetter
from tkinter.messagebox import showinfo
from typing_extensions import IntVar
from main import PROJECT_NAME, crawl,create_workers,HOMEPAGE,DOMAIN_NAME
from DataBase_Connector import *
from general import *
from spider import Spider

window = tk.Tk()
window.title("WEB CRAWLER")
window.geometry('600x600')
window.resizable(False,False)

website = tk.StringVar()
depth = tk.IntVar()

def btn():
    #HOMEPAGE = str(website.get())
    #print(HOMEPAGE)
    Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)
    create_workers()
    crawl()
    #print(website.get())
    message = ttk.Label(crawler_frame, text="Done Crawling").pack(fill='x',expand=True,padx=5)

def btn2():
    obj = Connect_to_database(Queue_path=QUEUE_FILE,Crawled_path=CRAWLED_FILE)
    obj.file_to_table()
    message = ttk.Label(crawler_frame, text="Updated in database").pack(fill='x',expand=True,padx=5)

crawler_frame = ttk.Frame(window).pack(padx=0,pady=0,fill='x',expand=True)

#message = ttk.Label(crawler_frame, text="Site to Crawl  :").pack(fill='x',expand=True,padx=5)
#website_entry = ttk.Entry(crawler_frame, textvariable=website).pack(fill='x',expand=True,padx=5)
#message = ttk.Label(crawler_frame, text="Max depth  :").pack(fill='x',expand=True,padx=5)
#depth_entry = ttk.Entry(crawler_frame, textvariable=depth).pack(fill='x',expand=True,padx=5)

crawl_button = ttk.Button(crawler_frame,text='Crawl',command=btn).pack(fill='x',expand=True,padx=5)
adddb_button = ttk.Button(crawler_frame,text='Add to Database',command=btn2).pack(fill='x',expand=True,padx=5)

data_box = Text(crawler_frame,width=18)
data_box.pack(fill='x',expand=True,padx=5)

def ins():
    Database = Connect_to_database(project_name=PROJECT_NAME)
    rows = Database.check_content()
    #data_box.delete(tk.BEGIN,tk.END)
    #data_box.insert(tk.END,rows)
    
    list_rows = list(map(itemgetter(1),rows))

    for x in list_rows:
        data_box.insert(tk.END,x)
        #print(x)


view_button = ttk.Button(crawler_frame,text='View Results',command=ins).pack(fill='x',expand=True,padx=5)

def del_all():
    obj = Connect_to_database(Queue_path=QUEUE_FILE,Crawled_path=CRAWLED_FILE)
    obj.empty_table()
    rm_project_dir(PROJECT_NAME)
    #print('Deleting all saved data')
    message = ttk.Label(crawler_frame, text="Deleted all saved data").pack(fill='x',expand=True,padx=5)
    
del_button = ttk.Button(crawler_frame,text='Delete All Saved Results',command=del_all).pack(fill='x',expand=True,padx=5)

window.mainloop()