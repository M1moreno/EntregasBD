<!-- En esta pagina puede encontrar mas informacion acerca de la estructura de un documento html 
    http://www.iuma.ulpgc.es/users/jmiranda/docencia/Tutorial_HTML/estruct.htm-->
<!DOCTYPE html>
<html lang="en">
<!--cabezera del html -->

<head>
    <!--configuraciones basicas del html-->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <!--titrulo de la pagina-->
    <title>inicio</title>
    <!--CDN de boostraps: Libreria de estilos SCSS y CSS para darle unas buena apariencia a la aplicacion
    para mas informacion buscar documentacion de boostraps en: https://getbootstrap.com/docs/4.3/getting-started/introduction/ -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <!--CDN de forntawesome: Libreria de estilos SCSS y CSS incluir icononos y formas 
     para mas informacio : https://fontawesome.com/start-->
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css"
        integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">
</head>

<body>
    <!--Barra de navegacion-->
    <ul class="nav">
        <li class="nav-item">
            <a class="nav-link active" href="../index.html">inicio</a>
        </li>
        <li class="nav-item">
            <a class="nav-link active" href="../listaReproduccion/listaReproduccion.php">Listas</a>
        </li>
        <li class="nav nav-pills">
            <a class="nav-link active" href="../canciones/canciones.php">Canciones</a>
        </li>
    </ul>
    <div class="container mt-3">
        <div class="row">
            <?php
                if(isset($_GET["codigoID"])){
             ?>
            <div class="col-6 px-2">
                <div class="card">
                    <div class="card-header">
                        Editar cancion
                    </div>
                    <div class="card-body">
                        <!--formulario para insertar una persona mediante el metodo post-->
                        <form action="update_c.php" class="form-group" method="post">
                            <div class="form-group">
                                <label for="codigoID">CodigoID</label>
                                <input type="text" readonly name="codigoID" value='<?=$_GET["codigoID"];?>' id="codigoID" class="form-control">
                            </div>
                            <div class="form-group">
                                <label for="">Nombre</label>
                                <input type="text" name="nombre" value='<?=$_GET["nombre"];?>' id="name" class="form-control">
                            </div>
                            <div class="form-group">
                                <label for="">Artista</label>
                                <input type="text" name="artista" value='<?=$_GET["artista"];?>' id="artista" class="form-control">
                            </div>
                            <div class="form-group">
                                <label for="">Album</label>
                                <input type="text" name="album" value='<?=$_GET["album"];?>' id="album" class="form-control">
                            </div>
                            <div class="form-group">
                                <label for="">Genero</label>
                                <input type="text" name="genero" value='<?=$_GET["genero"];?>' id="genero" class="form-control">
                            </div>
                            <div class="form-group">
                                <label for="">Fecha de creacion</label>
                                <input type="date" name="fecha_creacion" value='<?=$_GET["fecha_creacion"];?>' id="fecha_creacion" class="form-control">
                            </div>
                            <div class="form-group">
                                <label for="">Duracion</label>
                                <input type="text" name="duracion" value='<?=$_GET["duracion"];?>' id="duracion" class="form-control">
                            </div>
                            <div class="form-group">
                                <label for="">Lista</label>
                                <div class="form-check">
                                    <input class="form-check-input" onclick="cambioLista(this);" type="radio" name="exampleRadios2" id="exampleRadios2"
                                        value="lista" checked>
                                    <label class="form-check-label" for="exampleRadios1">
                                        Lista
                                    </label>
                                </div>
                            </div>
                            <div id="selectList" class="form-group">
                                <label for="exampleFormControlSelect2">Listas</label>
                                <select name="identificador" id="identificador" multiple class="form-control" id="exampleFormControlSelect2">
                                    <?php
                                    require('select_l.php');
                                    if($result){
                                        foreach ($result as $fila){
                                    ?>
                                            <option value=<?=$fila['codigoID'];?>  ><b>ID:</b> <?=$fila['codigoID'];?><b> - Nombre: </b><?=$fila['nombre'];?></option>
                                    <?php
                                        }
                                    }
                        
                                    ?>    
                                      
                                </select>
                            </div>
                            <!--librerias para usar jquery-->
                            <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
                            <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>
                             <!--controlador de los tipo radio-->
                            <script>
                                $("#selectList").hide();
                                function cambioLista(myRadio) {
                                    
                                    
                                    if(myRadio.value==="lista"){
                                       
                                        $("#selectList").show();
                                    }
                                    $("#identificador").val('');
                                }
                            </script>

                            <div class="form-group">
                                <input type="submit" class="btn btn-primary" value="Guardar">
                                <a href="canciones.php" class="btn btn-danger">descartar</a>
                                
                            </div>

                        </form>

                    </div>
                </div>
            </div>
            <?php
           }
        else{
             ?>
            <div class="col-6 px-2">
                <div class="card">
                    <div class="card-header">
                        Insertar cancion
                    </div>
                    <div class="card-body">
                        <!--formulario para insertar una persona mediante el metodo post-->
                        <form action="insert_c.php" class="form-group" method="post">
                            <div class="form-group">
                                <label for="codigoID">CodigoID</label>
                                <input type="text" name="codigoID" id="codigoID" class="form-control">
                            </div>
                            <div class="form-group">
                                <label for="">Nombre</label>
                                <input type="text" name="name" id="name" class="form-control">
                            </div>
                            <div class="form-group">
                                <label for="">Artista</label>
                                <input type="text" name="artista" id="artista" class="form-control">
                            </div>
                            <div class="form-group">
                                <label for="">Album</label>
                                <input type="text" name="album" id="album" class="form-control">
                            </div>
                            <div class="form-group">
                                <label for="codigoID">Genero</label>
                                <input type="text" name="genero" id="genero" class="form-control">
                            </div>
                            <div class="form-group">
                                <label for="codigoID">Fecha de creacion</label>
                                <input type="date" name="fecha_creacion" id="fecha_creacion" class="form-control">
                            </div>
                            <div class="form-group">
                                <label for="codigoID">Duracion</label>
                                <input type="text" name="duracion" id="duracion" class="form-control">
                            </div>
                            <div class="form-group">
                                <label for="">Lista</label>
                                <div class="form-check">
                                    <input class="form-check-input" onclick="cambioLista(this);" type="radio" name="exampleRadios2" id="exampleRadios2"
                                        value="lista" checked>
                                    <label class="form-check-label" for="exampleRadios1">
                                        Lista
                                    </label>
                                </div>
                            </div>
                            <div id="selectList" class="form-group">
                                <label for="exampleFormControlSelect2">Listas</label>
                                <select name="identificador" id="identificador" multiple class="form-control" id="exampleFormControlSelect2">
                                    <?php
                                    require('select_l.php');
                                    if($result){
                                        foreach ($result as $fila){
                                    ?>
                                            <option value=<?=$fila['codigoID'];?>  ><b>ID:</b> <?=$fila['codigoID'];?><b> - Nombre: </b><?=$fila['nombre'];?></option>
                                    <?php
                                        }
                                    }
                        
                                    ?>    
                                      
                                </select>
                            </div>
                            <!--librerias para usar jquery-->
                            <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
                            <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>
                             <!--controlador de los tipo radio-->
                            <script>
                                $("#selectList").hide();
                                function cambioLista(myRadio) {
                                    
                                    
                                    if(myRadio.value==="lista"){
                                       
                                        $("#selectList").show();
                                    }
                                    $("#identificador").val('');
                                }
                            </script>

                            <div class="form-group">
                                <input type="submit" class="btn btn-primary" value="insertar">
                                <a href="canciones.php" class="btn btn-success">Reiniciar</a>
                            </div>

                        </form>

                    </div>
                </div>
            </div>

            <?php
        }
        ?>
            <div class="col-6 px-2">

                <table class="table border-rounded">
                    <thead class="thead-dark">
                        <tr>
                            <th scope="col">CodigoID</th>
                            <th scope="col">Nombre</th>
                            <th scope="col">Artista</th>
                            <th scope="col">Album</th>
                            <th scope="col">Genero</th>
                            <th scope="col">FechaCreacion</th>
                            <th scope="col">Duracion</th>
                            <th scope="col">Lista</th>
                            <th scope="col">Opciones</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php 
                        require('select_c.php');
                        if($result){
                            foreach ($resultC as $fila){
                        ?>
                        <tr>
                            <td><?=$fila['codigoID'];?></td>
                            <td><?=$fila['nombre'];?></td>
                            <td><?=$fila['artista'];?></td>
                            <td><?=$fila['album'];?></td>
                            <td><?=$fila['genero'];?></td>
                            <td><?=$fila['fecha_creacion'];?></td>
                            <td><?=$fila['duracion'];?></td>
                            <td><?=$fila['id_lista_reproduccion'];?></td>
                            <td>

                                <form action="delete_c.php" method="POST">
                                    <input type="text" value=<?=$fila['codigoID'];?> hidden>
                                    <input type="text" name="d" value=<?=$fila['codigoID'];?> hidden>
                                    <button class="btn btn-danger" title="eliminar" type="submit"><i
                                            class="fas fa-trash-alt"></i></button>
                                </form>
                            </td>
                            <td class="mx-0 pr-2">
                                <form action="canciones.php" method="GET">
                                    
                                    <input type="text" name="codigoID" value='<?=$fila['codigoID'];?>' hidden>
                                    <input type="text" name="nombre" value='<?=$fila['nombre'];?>' hidden>
                                    <input type="text" name="artista" value='<?=$fila['artista'];?>' hidden>
                                    <input type="text" name="album" value='<?=$fila['album'];?>' hidden>
                                    <input type="text" name="genero" value='<?=$fila['genero'];?>' hidden>
                                    <input type="date" name="fecha_creacion" value='<?=$fila['fecha_creacion'];?>' hidden>
                                    <input type="text" name="duracion" value='<?=$fila['duracion'];?>' hidden>
                                    <input type="text" name="id_lista_reproduccion" value='<?=$fila['id_lista_reproduccion'];?>' hidden>


                                    <button class="btn btn-primary" title="editar" type="submit"><i
                                            class="far fa-edit"></i></button>
                                </form>
                            </td>



                        </tr>
                        <?php                    

                                }
                            }
                            
                            ?>
                    </tbody>
                </table>

            </div>
        </div>


    </div>




</body>

</html>