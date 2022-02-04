<?php
 
// Create connection
require('../configuraciones/conexion.php');

//query
$query="delete FROM lista_reproduccion where codigoID='$_POST[d]'";
$result = mysqli_query($conn, $query) or 
die(mysqli_error($conn));
 
if($result){
    header ("Location: listaReproduccion.php");
    
     
 }else{
     echo "Ha ocurrido un error al eliminar la lista";
 }
 
mysqli_close($conn);



?>