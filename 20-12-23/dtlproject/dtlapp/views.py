from django.shortcuts import render ,HttpResponse

# Create your views here.


def index(r):
    # context = "Chiro"
    # return render(r,"index.html",{"context":context})

    # context = {}
    # context ["name"]= "Chiro"
    # context ["Roll_No"]= "305"
    # context ["Email"]= "Chiro305@gmail.com"
    # context ["SID"]= "1"
    # return render(r,"index.html",context)

    # SID = int(input("Enter Id ="))
    # name = input("Enter Name =")
    # Email = input("Enter Email Id =")
    # Roll_No = int(input("Enter Roll no ="))
    # context = {"SID": SID, "name":name, "Email":Email, "Roll_No":Roll_No}
    # return render(r,"index.html",context)


    username = input("Enter Username =")
    userdata = []
    if username == "admin":
        try:

            count = int(input("Enter user count ="))
            for i in range(count):
                SID = int(input("Enter Id ="))
                name = input("Enter Name =")
                Email = input("Enter Email Id =")
                Roll_No = int(input("Enter Roll no ="))
                context = {"SID": SID, "name":name, "Email":Email, "Roll_No":Roll_No}
                userdata.append(context)
            print(userdata)
            
        except:
            # return HttpResponse("Count can't be empty")
            errmsg = "Count can't be empty"
            return render(r,"index.html",{"errmsg": errmsg})
        
        return render(r,"index.html",{"userdata": userdata, "errmsg": errmsg})
    else:
        errmsg = "You don't have permission. Please login With admin user"
        return render(r,"index.html",{"errmsg": errmsg})