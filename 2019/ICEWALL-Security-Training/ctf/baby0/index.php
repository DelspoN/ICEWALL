<?php
include_once("./flag.php");
if (isset($_GET['get_param']) && isset($_POST['post_param']) && isset($_COOKIE['cookie_data']) &&
	$_GET['get_param'] === "get" && $_POST['post_param'] === "the" && $_COOKIE['cookie_data'] === "flag")
	echo $flag;
highlight_string(file_get_contents(__FILE__))
?>
