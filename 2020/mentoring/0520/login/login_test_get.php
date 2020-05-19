<?php 
	$ID = $_GET['ID'];
	$PW = $_GET['PW'];
	if($ID && $PW){
        echo "You entered " . $ID . " and " . $PW;
	}
	else{
		echo "<script>alert(\"No ID or PW\");</script>";
	}
?>
