<?php 
	error_reporting(E_ALL);
	ini_set("display_errors", 1);

	$conn = mysqli_connect("localhost", "user", "Qwer1234!", "test");
	$result = mysqli_query($conn,"SELECT * FROM test_table");

	var_dump($result->num_rows);
	while ($row = $result->fetch_assoc()) {
		var_dump($row);
	}

	$result = mysqli_query($conn,"SELECT * FROM test_table");

	while ($row = $result->fetch_assoc()) {
		echo "</br>";
		echo $row['num'];
		echo " ";
		echo $row['str'];
	}


?>



