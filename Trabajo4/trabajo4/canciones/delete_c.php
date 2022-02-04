<?php
 
// Create connection
require('../configuraciones/conexion.php');

//query
$query="delete FROM cancion where codigoID='$_POST[d]'";
$result = mysqli_query($conn, $query) or 
die(mysqli_error($conn));
 
if($result){
    header ("Location: canciones.php");
    
     
 }else{
     echo "Ha ocurrido un error al eliminar la cancion";
 }
 
mysqli_close($conn);



?>