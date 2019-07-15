<?php
session_start();
unset($_SESSION['id']);
unset($_SESSION['isAdmin']);
header("location:index.html");
?>
