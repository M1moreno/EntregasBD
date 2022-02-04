<?php
 
// Create connection
require('../configuraciones/conexion.php');

$codigoID = $_POST["codigoID"];

//query
if($codigoID<0){
	echo "codigoID debe ser positivo";
}

else{
	$query="INSERT INTO `lista_reproduccion`(`codigoID`,`nombre`, `plataforma`, `cantidad_canciones`)
 	VALUES ('$_POST[codigoID]','$_POST[name]','$_POST[plataforma]','$_POST[cantidad_canciones]')";
	$result = mysqli_query($conn, $query) or die(mysqli_error($conn));

 	if($result){
        header ("Location: listaReproduccion.php");
        
         
 	}else{
 		echo "Ha ocurrido un error al crear la lista";
 	}


}

?>
