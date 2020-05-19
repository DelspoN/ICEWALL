<?php 
	error_reporting(E_ALL);
	ini_set("display_errors", 1);

	$ID = $_GET['ID'];
	$PW = $_GET['PW'];
	if($ID && $PW){
		$conn = mysqli_connect("localhost", "root", "root", "Login");
		$result = mysqli_query($conn,"INSERT INTO Login (id,pw) VALUES ('$ID','$PW')");
		if($result==false){
			echo mysqli_error($conn);
		}
	}
	else{
		echo "<script>alert(\"No ID or PW\");</script>";
	}
?>



