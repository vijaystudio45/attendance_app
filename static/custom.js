$("#personal_information").click(function(e){
    e.preventDefault();
    formUrl = $('#personal_information_form').attr('action');
    t=$(this).closest("form")
    t.ajaxSubmit({url:formUrl,dataType:'JSON',success:function(e,r,n,l){
    if(e.status == 'success'){toastr.success(e.message);}else{toastr.error(e.message);}setTimeout(function(){
    if(typeof(e.print_error) != "undefined" && e.print_error !== null){
       var html = '<ul>';
       for(var key in e.print_error) {
           html +="<li><ul class='error'><li>"+key+" :</li>";
           html +="<li>"+e.print_error[key][0]+"</li></ul></li>";
        }
        html +='</ul>';
        $(".error-messages").html(html);
    }else{
        window.location.href = e.url;
    }},2e3)}})
})
function valid_ssn (elementValue){
		var  ssnPattern = /^[0-9]{3}\-?[0-9]{2}\-?[0-9]{4}$/;
		return ssnPattern.test(elementValue);
	}
$("#moov_information").click(function(e){
    var customerID = "b3d613316e210417547fcc22e59e71b23b9bfe6f";
    var accountID = "d2ae1c34-9af4-48a9-8c58-17282c4dd8a8";
    var formUrl = $('#admin_ach_form').attr('action');
    updateMoovResponseInUserProfile(customerID,accountID,formUrl);
    e.preventDefault();
//    var moovToken = $("#id_HiddenInput_token").val();
//    const moov = Moov(moovToken);
//    const customer = {
//				firstName: admin_ach_form.first_name.value,
//				lastName: admin_ach_form.last_name.value,
//				email: admin_ach_form.email.value,
//				ssn: admin_ach_form.Social_Security_Number.value,
//				type: 'individual'
//
//			};
//	const account = {
//				type: admin_ach_form.type.value, /* 'Checking' or 'Savings' */
//				holderName: `${admin_ach_form.first_name.value} ${admin_ach_form.last_name.value}`,
//				accountNumber: admin_ach_form.checking_account_number.value,
//				routingNumber: admin_ach_form.routing_number.value
//			};
//
//	moov.quickEnroll(customer, account)
//			.then((res) => {
//
//			    console.log(res)
//			});

})


function updateMoovResponseInUserProfile(customerID,accountID,formUrl){
     $.ajax({
            url: formUrl,
            type: 'POST',
            data: {'customerID':customerID,'accountID':accountID,'csrfmiddlewaretoken':window.CSRF_TOKEN},
            success:function(res){
                toastr.success(res.message);
            }
     })
}


//  Dtelnyx_api
$("#employee_register_btn").click(function(e){
    e.preventDefault();
    var formErrors = 0;
    $('.validateInput').each(function(){
        if($.trim($(this).val()) == '') {
            $(this).removeClass('border border-dark');
            $(this).addClass('border border-danger');
            formErrors++;
        } else {
            $(this).removeClass('border border-danger');
            $(this).addClass('border border-dark');
        }
    });
    if(formErrors == 0 && formErrors == '0') {
    formUrl = $('#employee_register_form').attr('action');
    t=$(this).closest("form")
    t.ajaxSubmit({url:formUrl,dataType:'JSON',success:function(e,r,n,l){
    if(e.status == 'success'){toastr.success(e.message);}else{toastr.error(e.message);}setTimeout(function(){
    if(typeof(e.print_error) != "undefined" && e.print_error !== null){
       var html = '<ul>';
       for(var key in e.print_error) {
           html +="<li><ul class='error'><li>"+key+" :</li>";
           html +="<li>"+e.print_error[key][0]+"</li></ul></li>";
        }
        html +='</ul>';
        $(".error-messages").html(html);
    }else{
        //$("#telnyx_response").text(JSON.stringify(e.response));
        //window.location.href = e.url;
    }},2e3)}})
    }
})


$(document).on('click', '#start_date_btn', function(e) {
e.preventDefault();
$.ajax({
   url:"/start-data-time-add/",
  data: {csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()},
   type: 'POST',
   success: function (data) {

       if ($.trim(data.status) == 'success')
        {
            toastr.success(data.message);
            window.location.href = "/employee-data-add/";


        }
        else
        {
            toastr.error(data.message);
        }

   }
});
});


$(document).on('click', '#end_date_btn', function(e) {
e.preventDefault();
$.ajax({
   url:"/end-data-time-add/",
  data: {csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()},
   type: 'POST',
   success: function (data) {

       if ($.trim(data.status) == 'success')
        {
            toastr.success(data.message);
             window.location.href = "/employee-data-add/";
        }
        else
        {
            toastr.error(data.message);
        }

   }
});
});


//$(document).ready(function(){
//    $('#end_date_btn').prop('disabled', true);
//});

$(document).ready(function() {
   let todayDate = new Date().getDate();
   let endD = new Date(new Date().setDate(todayDate));
   $('#start_datepicker_id').datepicker({
        format: 'yyyy-mm-dd',
//      startDate : endD,
//      weekStart: 7,
//      todayBtn:  1,
//      autoclose: 1,
//      todayHighlight: 1,
   });

		//endDate(new Date());
	});
    $(document).ready(function() {
	$('#start_datepicker_id').keypress(function(e) {
			e.preventDefault();
		});
 $('#start_datepicker_id').bind('copy paste cut',function(e) {
 e.preventDefault();
 });
});


$(document).ready(function() {
   let todayDate = new Date().getDate();
   let endD = new Date(new Date().setDate(todayDate));
   $('#end_datepicker_id').datepicker({
      format: 'yyyy-mm-dd',
      startDate : endD,
      weekStart: 7,
      todayBtn:  1,
      autoclose: 1,
      todayHighlight: 1,
   });

		//endDate(new Date());
	});
    $(document).ready(function() {
	$('#end_datepicker_id').keypress(function(e) {
			e.preventDefault();
		});
 $('#end_datepicker_id').bind('copy paste cut',function(e) {
 e.preventDefault();
 });
});