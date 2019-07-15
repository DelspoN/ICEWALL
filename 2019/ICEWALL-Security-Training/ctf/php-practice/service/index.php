<!DOCTYPE html>
<html>
<head>
<title>PHP Practice</title>
</head>
<body>

<a href="?page=p.php">p tag</a>
<a href="?page=h1.php">h1 tag</a>

<?php
if (isset($_GET['page'])) {
  include_once($_GET['page']);
}
else {
  ?>
This is a default page.
  <?php
}
?>

<!-- flag is in /flag -->

</body>
</html>
