<?php
	if($_COOKIE['ID']){
		setcookie('ID',"",1);
		echo "<script>history.back()</script>";
	}
	else{
		echo "Plz Login";
	}

?>




