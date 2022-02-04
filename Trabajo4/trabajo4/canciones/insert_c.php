<?php
 
// Create connection
require('../configuraciones/conexion.php');

$codigoID = $_POST["codigoID"];
$lista = $_POST["identificador"];

//query
if($codigoID<0){
	echo "codigoID debe ser positivo";
}

else if ($lista == '0'){

	$query="INSERT INTO `cancion`(`codigoID`,`nombre`, `artista`, `album`,`genero`,`fecha_creacion`,`duracion`,`id_lista_reproduccion`)
 	VALUES ('$_POST[codigoID]','$_POST[name]','$_POST[artista]','$_POST[album]','$_POST[genero]','$_POST[fecha_creacion]','$_POST[duracion]',NULL)";
	$result = mysqli_query($conn, $query) or die(mysqli_error($conn));

 	if($result){
        header ("Location: canciones.php");
        
         
 	}else{
 		echo "Ha ocurrido un error al crear la cancion";
 	}


}

else{

	$query="INSERT INTO `cancion`(`codigoID`,`nombre`, `artista`, `album`,`genero`,`fecha_creacion`,`duracion`,`id_lista_reproduccion`) VALUES ('$_POST[codigoID]','$_POST[name]','$_POST[artista]','$_POST[album]','$_POST[genero]','$_POST[fecha_creacion]','$_POST[duracion]','$_POST[identificador]')";
	$result = mysqli_query($conn, $query) or die(mysqli_error($conn));

 	if($result){
        header ("Location: canciones.php");
        
         
 	}else{
 		echo "Ha ocurrido un error al crear la cancion";
 	}
	
}

?>