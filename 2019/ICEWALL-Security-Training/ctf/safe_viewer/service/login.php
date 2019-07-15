<?php
include_once("../flag.php");
session_start();

function check_timeout() {
  if (time() - $_SESSION['time'] > 300)
    return 1;

  return 0;
}

function check_login() {
  $ret = 0;

  if (isset($_SESSION['id']) && $_SESSION['id'] !== "") {
    $ret = 1;

    if (isset($_SESSION['isAdmin']) && $_SESSION['isAdmin'] !== "")
      $ret = 2;
  }
  else if (isset($_COOKIE['id']) && $_COOKIE['id'] !== "") {
    $ret = 1;

    if (isset($_COOKIE['isAdmin']) && $_COOKIE['isAdmin'] !== "")
      $ret = 2;

    if (check_timeout())
      $ret = 0;
  }

  return $ret;
}

if (isset($_POST['id']) && isset($_POST['pw'])) {
  if ($_POST['id'] == 'guest' && $_POST['pw'] == 'guest') {
    $_SESSION['id'] = 'guest';
    $_SESSION['time'] = time();
  }
}

$priv = check_login();

if ($priv > 0) {
  echo "<script>alert(\"Hello " . $_SESSION['id'] . "\");";

  if ($priv == 2)
    echo "alert(\"" . $flag . "\");";

  echo "location.href=\"index.html\";</script>";
}

?>
