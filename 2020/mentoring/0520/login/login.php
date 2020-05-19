<?php 

	$ID = $_GET['ID'];
	$PW = $_GET['PW'];
	if($ID && $PW){
		$conn = mysqli_connect("localhost", "root", "root", "Login");
		$result = mysqli_query($conn,"SELECT * FROM Login WHERE id = $ID and pw =$PW");
		$User = mysqli_fetch_array($result);
		if($User[0]==$ID){
			echo  "GOOD";
			setcookie('ID', $ID, time() + 3600);
			echo "<script>document.location='/index.php'</script>";
		}
		else{
			echo "No User";
		}
	}
	else{
		echo "<script>alert(\"No ID or PW\");</script>";
	}
?>



