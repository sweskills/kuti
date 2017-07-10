function validate()
{
   if( document.StudentRegistration.textnames.value == "" )
   {
     alert( "Please provide your Name!" );

     return false;
   }
   if( document.StudentRegistration.fathername.value == "" )
   {
     alert( "Please provide your Father Name!" );
     document.StudentRegistration.fathername.focus() ;
     return false;
   }

   if( document.StudentRegistration.paddress.value == "" )
   {
     alert( "Please provide your Postal Address!" );
     document.StudentRegistration.paddress.focus() ;
     return false;
   }
   if( document.StudentRegistration.personaladdress.value == "" )
   {
     alert( "Please provide your Personal Address!" );
     document.StudentRegistration.personaladdress.focus() ;
     return false;
   }
   if ( ( StudentRegistration.sex[0].checked == false ) && ( StudentRegistration.sex[1].checked == false ) )
   {
   alert ( "Please choose your Gender: Male or Female" );
   return false;
   }
   if( document.StudentRegistration.City.value == "-1" )
   {
     alert( "Please provide your City!" );
     document.StudentRegistration.City.focus() ;
     return false;
   }
   if( document.StudentRegistration.Course.value == "-1" )
   {
     alert( "Please provide your Course!" );

     return false;
   }
   if( document.StudentRegistration.District.value == "-1" )
   {
     alert( "Please provide your Select District!" );

     return false;
   }
   if( document.StudentRegistration.State.value == "-1" )
   {
     alert( "Please provide your Select State!" );

     return false;
   }
   if( document.StudentRegistration.pincode.value == "" ||
           isNaN( document.StudentRegistration.pincode.value) ||
           document.StudentRegistration.pincode.value.length != 6 )
   {
     alert( "Please provide a pincode in the format ######." );
     document.StudentRegistration.pincode.focus() ;
     return false;
   }
 var email = document.StudentRegistration.emailid.value;
  atpos = email.indexOf("@");
  dotpos = email.lastIndexOf(".");
 if (email == "" || atpos < 1 || ( dotpos - atpos < 2 ))
 {
     alert("Please enter correct email ID")
     document.StudentRegistration.emailid.focus() ;
     return false;
 }
  if( document.StudentRegistration.dob.value == "" )
   {
     alert( "Please provide your DOB!" );
     document.StudentRegistration.dob.focus() ;
     return false;
   }
  if( document.StudentRegistration.mobileno.value == "" ||
           isNaN( document.StudentRegistration.mobileno.value) ||
           document.StudentRegistration.mobileno.value.length != 10 )
   {
     alert( "Please provide a Mobile No in the format 123." );
     document.StudentRegistration.mobileno.focus() ;
     return false;
   }
   return( true );
}