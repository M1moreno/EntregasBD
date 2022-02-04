<?php
 
// Create connection
require('../configuraciones/conexion.php');

//query
$query="UPDATE lista_reproduccion SET nombre='$_POST[nombre]',plataforma='$_POST[plataforma]',cantidad_canciones='$_POST[cantidad_canciones]' WHERE codigoID='$_POST[CodigoID]'";
$result = mysqli_query($conn, $query) or 
die(mysqli_error($conn));
 
if($result){
    header ("Location: listaReproduccion.php");
    
     
 }else{
     echo "Ha ocurrido un error al editar la lista";
 }
 
mysqli_close($conn);



?>