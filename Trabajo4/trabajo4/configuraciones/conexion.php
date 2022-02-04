<?php
$host = 'localhost';
$user = "root";
$pass = "";
$DB = "nidofaust";
$conn = new mysqli($host, $user, $pass, $DB) or die("Error al conectar a la DB " . mysqli_error($link));
?>