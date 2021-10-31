#list=[{"Appetizers":"Wings,Cookies,Spring Rolls"}]
#Created lists for menu
Appetizers=["Wings","Cookies","Spring Rolls"]
Entrees=["Salmon","Steak","Meat Tornado","A Literal Garden"]
Desserts=["Ice Cream","Cake","Pie"]
Drinks=["Coffee","Tea","Unicorn Tears"]


#Created dictionary  for menu

menu={"Appetizers":Appetizers,"Entrees":Entrees,"Desserts":Desserts,"Drinks":Drinks}
items={   
"wings":0,
"cookies":0,
"spring rolls":0,
"salmon":0,
"steak":0,
"meat tornado":0,
"a literal garden":0,
"ice cream":0,
"cake":0,
"pie":0,
"coffee":0,
"tea":0,
"unicorn tears":0,

}

# created function for welcome messages and has smaller functions for orders 
def snakes_cafe():
    print ("**************************************")
    print('**    Welcome to the Snakes Caf     **')    
    print('**    Please see our menu below.    **')      
    print('**') 
    print('**    To quit at any time, type "quit"  **')  
    print("**************************************")

    def order():
            
        for i in menu:
            print(i)
            print(" ")
            print("----------")
            print(" ")
            for y in menu[i]:
                print(" ")
                print(y)
            print(" ")
            print(" ")
    
    order()
    print("**************************************")
    print("**  What would you like to order?   **")
    print("**************************************")
    
    selected=input()
    selected=selected.lower()
    counter=0
    while selected !="quit":
         
           if(selected in items):
               # incremnet the chosen order
             items[selected]=items[selected]+1
             counter+=1
             print (f"{items[selected]} order of {selected} have been added to your meal")
             print("")
             print(f"Number of orders {counter}")
             selected=input(" would you like to order more? If yes tell me please ").lower()
             if selected=="quit":
               break
             else:
                continue
            #Here if the user ordered something doesn't exist 
           else:
               print("Sorry We don't have your order now ")
               selected=input(" would you like to order more? If yes tell me please If no just quit ").lower()
               if selected=="quit":
                break
               else:
                continue
    
                    
if __name__=="__main__":
    snakes_cafe()

      