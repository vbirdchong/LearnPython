$(document).ready(function(){
	alert("Good! You are login the web");
	$("#login").click(function(){
		var user = $("#username").val();
		var pwd = $("#password").val();
		var pd = {"username":user, "password":pwd};
		alert("step2 you are enter the username")
		
		$.ajax({
			type:"post",
			url:"/",
			data:pd,
			cache:false,
			success:function(data){
				alert(data);
			},
			error:function(){
				alert("error!");
			},
		})
			
	});
});