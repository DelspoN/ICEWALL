<?php
include "./flag";
$Email=$_POST['Email'];
$Password=$_POST["Password"];
$conn = new mysqli("mysql", "root", ".sweetpwd.", "login");
// Check connection

if ($conn->connect_error) {
 	die("Connection failed: " . $conn->connect_error);
 }

$sql = "SELECT * FROM user WHERE Email = '$Email' and Password = '$Password'";
 $result = $conn->query($sql);
 if ($result->num_rows > 0) {
	 echo "Hello admin! flag is ";
	 echo $flag; 
 }
 else {
	 echo "This service has not been created yet.\n";
	 echo "If you have any problems, please contact us by email below.\n";
	 echo "admni@icewall.com";
 	}
 $conn->close();
?>
