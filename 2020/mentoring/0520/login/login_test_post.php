<?php 
	$ID = $_POST['ID'];
	$PW = $_POST['PW'];
	if($ID && $PW){
        echo "You entered " . $ID . " and " . $PW;
	}
	else{
		echo "<script>alert(\"No ID or PW\");</script>";
	}
?>
