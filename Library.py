library=[]
wishlist=[]
my_book=input("enter a name of the book you in your library \n")
library.append(my_book)
my_book=input("enter a name of another book , or (press [enter] to skip) \n")
if my_book :
    library.append(my_book)
print("your books are " , library)



my_book=input("enter a name of  a book you want to own \n ")
wishlist.append(my_book)
my_book=input("enter a name of another book you want , or (press [enter] to skip) \n")
if my_book :
    wishlist.append(my_book)
print("your wishlist is" , wishlist)



acquired_book=input("enter a name of a book you acquired \n")
if acquired_book in wishlist :
    library.append(acquired_book)
    wishlist.remove(acquired_book)
print("your library is" , library )
print("your wishlist is" , wishlist)


donated_book=input("enter a name of a book you donated \n")
if donated_book in library :
    library.remove(donated_book)
print("your library after every thing is " , library)