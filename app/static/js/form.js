function validate(){
	submitOK="True"
	x=document.form1

	emailattherate=x.email.value.indexOf("@")
	if(emailattherate==-1)
	{
	alert("Invalid Email")
	submitOK="False"
	}
	if(submitOK=="False")
	{
	return false
	}
}

//function recorded(){
	//alert("Thank you, your account has been created")  
  
    password=x.pwd.value
    if (password.length==0) 
    {
    	alert("This password field cannot remain blank.")
    	submitOK="False"
    }
    verifypassword=x.pwd1.value
    if(verifypassword.length==0){
    	alert("Please reenter password")
    	submitOK="False"
    }
    if(password!=verifypassword)
    {
    	alert("Passwords do not match")
    	submitOK="False"
    }
-->