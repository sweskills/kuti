$(function() {
  // Initialize form validation on the school profile form.
  // It has the name attribute "profile"
  $("form[name='profile']").validate({
    // Specify validation rules
    rules: {
      // The key name on the left side is the name attribute
      // of an input field. Validation rules are defined
      // on the right side
      schoolname: "required",
      location: "required",
      description: "required"
    },
    // Specify validation error messages
    messages: {
      schoolname: "Please enter the school name",
      location: "Please enter the school location",
      description: "Please enter a brief description of school"
    },
    submitHandler: function(form) {
      form.submit();
    }
  });
});