data=[
    {"january":2000,"February":2350,"March":2600,"April":2130,"May":2190},
    
]
print(data[0].get("january"))
x=int (input("Which data you want :\nClick 1 for for know in Feb, how many dollars you spent extra compare to January?\nClick 2 to find out your total expense in first quarter (first three months) of the year.\nClick 3 to Find out if you spent exactly 2000 dollars in any month\nClick 4 for know June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list\nClick 5 for know You returned an item that you bought in a month of April and got a refund of 200$.Make a correction to your monthly expense list based on this\n"))
if (x==1) :
    print(data[0].get("February")-data[0].get("january"))
elif x==2:
    print(data[0].get("january")+data[0].get("February")+data[0].get("March")) 
elif x==4:
    data.insert(1,{"january":1980})
    
        
        

            
else:
    print(data)    
    
