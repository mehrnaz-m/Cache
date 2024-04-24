# Mehrnaz Miri

#defining the cache and requests lists
cache = []
requests = []

while True:
    #taking user requests
    print()
    print("Welcome to the main menu!")
    while True:
        user_requests = int(input("Please give me an integer <3 (press 0 when you're done) "))

        if user_requests != 0:
            requests.append(user_requests)
        else: #exit once user enters 0
            print("Thank you for your input!")

            break


    while True:        
        #Asking what the user wants to do now that they've put in their requests
        print()
        user_choice = input("You have 3 choices:\n1. Press 1 for fifo \n2. Press 2 for lfu \n3. Press Q to exit Program ")
        
        if user_choice == "1":
            #defining the FIFO algorithm
            def fifo():  
                    for page in requests:
                        if page in cache:
                            print("hit!")
                        else:
                            print("miss!")
                            cache.append(page)
                            
            fifo()
            #show only the last 8 requests
            if len(cache) <= 8:
                print(cache)
                #clearing the cache for further requests
                cache.clear()
            else:
                print(cache[-8:])
                #clearing the cache for further requests
                cache.clear()

        if user_choice == "2":

            #defining the LFU algorithm
            def lfu():
                for page in requests:
                    if page in cache:
                        print("hit!")
                        print(cache) #delete
                    else:
                        print("miss!")
                        cache.append(page)

            lfu()
            print(cache)
            print(requests)

        if user_choice == "q":

            #showing the final cache list, clearing it, and starting the whole thing all over again
            print(cache)
            cache.clear()
            requests.clear()
            break



