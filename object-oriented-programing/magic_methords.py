class book :
    def __init__(self, author, pages):
        self.author =author
        self.pages =pages
        
    def __str__(self):
        return f"{self.author} is the author of this book, it has {self.pages} number of pages"
    
    def __repr__(self):
        return f"{self.author} is the author of this book, it has {self.pages} number of pages"   
        
if __name__ == "__main__":
    
        book1 = book("The great Gatsby", 230)
        
        print(str(book1))
        print(repr(book1))
        
         
            