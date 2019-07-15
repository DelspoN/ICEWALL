<?php
error_reporting(E_ALL);
ini_set("display_errors", 1);


if (!isset($_POST['id']) || !isset($_POST['pw'])) {
  die("access denied");
}

$id = $_POST['id'];
$pw = $_POST['pw'];

include_once('db.php');

$sql = "SELECT * FROM users WHERE id = '{$id}' AND pw = '{$pw}'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  $row = mysqli_fetch_assoc($result);
  $login_id = $row['id'];
  echo "Hello, {$login_id}";
}
else {
  die("login failed");
}

?>
