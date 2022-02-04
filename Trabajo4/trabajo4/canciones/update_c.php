<?php
 
// Create connection
require('../configuraciones/conexion.php');

//query
$query="UPDATE cancion SET nombre='$_POST[nombre]',artista='$_POST[artista]',album='$_POST[album]',genero='$_POST[genero]',fecha_creacion='$_POST[fecha_creacion]',duracion='$_POST[duracion]',id_lista_reproduccion='$_POST[identificador]' WHERE codigoID='$_POST[codigoID]'";
$result = mysqli_query($conn, $query) or 
die(mysqli_error($conn));
 
if($result){
    header ("Location: canciones.php");
    
     
 }else{
     echo "Ha ocurrido un error al editar la cancion";
 }
 
mysqli_close($conn);



?>