function validate()
{
   if( document.SchoolRegistration.schoolname.value == "" )
   {
     alert( "Please provide your UserName!" );
     document.SchoolRegistration.schoolname.focus();
     return false;
   }
   var emails = document.SchoolRegistration.email.value;
  atpos = emails.indexOf("@");
  dotpos = emails.lastIndexOf(".");
   if (emails == "" || atpos < 1 || ( dotpos - atpos < 2 ))
 {
     alert("Please enter correct email ID")
     document.SchoolRegistration.email.focus() ;
     return false;
 }
   var passw = /^(?=.*[A-Z])\w{6,}$/;
   var pass1 = document.getElementById("password").value;
   if(pass1 == "" || !pass1.match(passw) || pass1.match(/^Password$/i))
   {
     document.SchoolRegistration.password.focus();
     alert("Password is Invalid! Password");
    return false;
   }
   var pass2 = document.getElementById("password2").value;
   if( pass2 != pass1)
   {
     alert( "Please Password Must Match!" );
     return false;
   }
   if( document.SchoolRegistration.mobilenumber.value == "" ||
           isNaN( document.SchoolRegistration.mobilenumber.value) ||
           document.SchoolRegistration.mobilenumber.value.length < 10 )
   {
     alert( "Please provide a Mobile No in the country code format excluding the '+' symbol e.g '2348000000000'" );
     document.SchoolRegistration.mobilenumber.focus() ;
     return false;
   }
   return true;
}