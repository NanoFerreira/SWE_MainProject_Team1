function Account_Button(Button_Functionality){
    let divArray = []
    divArray.push(document.getElementById("Your_Account_Div"));
    divArray.push(document.getElementById("Current_Orders_Div"));
    divArray.push(document.getElementById("Trade/Sell_Div"));
    divArray.push(document.getElementById("Contact_Us_Div"));
    divArray.push(document.getElementById("Sales_Report_Div"));
    divArray.push(document.getElementById("Add_Inventory_Div"));
    divArray.push(document.getElementById("Promote_User_Div"));

    for (const div of divArray) {
        if (div.id == Button_Functionality){
            div.style.display = "block";
        }
        else{
            div.style.display = "none";
        }
    }
}

function Go_Home(){
    window.location = "index.html";
}

function Go_Shopping_Cart(){
    window.location = "shopping_cart.html";
}

function Check_Account(Account_Type){
    switch(Account_Type){
        case 1:
            window.location = "login.html";
            break;
        case 2:
            window.location ="Account.html";
            break;    
    }

}
