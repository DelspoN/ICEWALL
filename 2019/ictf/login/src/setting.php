<?php
include "./flag";
$Email=$_POST['Email'];
$Password=$_POST["Password"];
$conn = new mysqli("mysql", "root", ".sweetpwd.", "login");

if ($conn->connect_error) {
 	die("Connection failed: " . $conn->connect_error);
 }

$sql = "CREATE database login;use login";
$result = $conn->query($sql);
$sql = "use login";
$result = $conn->query($sql);
$sql = "CREATE tables user(Email varchar(50) null,Password varchar(20) null)";
$result = $conn->query($sql);
$sql = "INSERT INTO user values('admni@icewall.com','you_WIll_NeVEr_know')";
$result = $conn->query($sql);
$conn->close();
?>
