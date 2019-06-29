<?php

if (!isset($_GET['url']))
	die();

$url = $_GET['url'];

if (substr($url, 0, 1) == '/')
	die();
if (strpos($url, '..') !== FALSE)
	die();
if (strpos($url, 'file://') !== FALSE)
        die();

echo file_get_contents($url);
?>
