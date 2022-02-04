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
        <li class="nav nav-pills">
            <a class="nav-link active" href="../listaReproduccion/listaReproduccion.php">Listas</a>
        </li>
        <li class="nav nav-item">
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
                        Editar lista
                    </div>
                    <div class="card-body">
                        <!--formulario para insertar una persona mediante el metodo post-->
                        <form action="update_l.php" class="form-group" method="post">
                            <div class="form-group">
                                <label for="codigoID">CodigoID</label>
                                <input type="text" readonly name="CodigoID" value=<?=$_GET["codigoID"];?> id="CodigoID" class="form-control">
                            </div>
                            <div class="form-group">
                                <label for="">Nombre</label>
                                <input type="text" name="nombre" value='<?=$_GET["nombre"];?>' id="name" class="form-control">
                            </div>
                            <div class="form-group">
                                <label for="">Plataforma</label>
                                <input type="text" name="plataforma" value='<?=$_GET["plataforma"];?>' id="plataforma" class="form-control">
                            </div>
                            <div class="form-group">
                                <label for="">Cantidad de canciones</label>
                                <input type="text" name="cantidad_canciones" value=<?=$_GET["cantidad_canciones"];?> id="cantidad_canciones" class="form-control">
                            </div>

                            <div class="form-group">
                                <input type="submit" class="btn btn-primary" value="Guardar">
                                <a href="listaReproduccion.php" class="btn btn-danger">descartar</a>
                                
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
                        Insertar lista
                    </div>
                    <div class="card-body">
                        <!--formulario para insertar una persona mediante el metodo post-->
                        <form action="insert_l.php" class="form-group" method="post">
                            <div class="form-group">
                                <label for="codigoID">CodigoID</label>
                                <input type="text" name="codigoID" id="codigoID" class="form-control">
                            </div>
                            <div class="form-group">
                                <label for="">Nombre</label>
                                <input type="text" name="name" id="name" class="form-control">
                            </div>
                            <div class="form-group">
                                <label for="">Plataforma</label>
                                <input type="text" name="plataforma" id="plataforma" class="form-control">
                            </div>
                            <div class="form-group">
                                <label for="">Cantidad de canciones</label>
                                <input type="text" name="cantidad_canciones" id="cantidad_canciones" class="form-control">
                            </div>

                            <div class="form-group">
                                <input type="submit" class="btn btn-primary" value="insertar">
                                <a href="listaReproduccion.php" class="btn btn-success">Reiniciar</a>
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
                            <th scope="col">Plataforma</th>
                            <th scope="col">Cantidad de canciones</th>
                            <th scope="col">Opciones</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php 
                        require('select_l.php');
                        if($result){
                            foreach ($result as $fila){
                        ?>
                        <tr>
                            <td><?=$fila['codigoID'];?></td>
                            <td><?=$fila['nombre'];?></td>

                            <td><?=$fila['plataforma'];?></td>

                            <td><?=$fila['cantidad_canciones'];?></td>
                            <td>

                                <form action="delete_l.php" method="POST">
                                    <input type="text" value=<?=$fila['codigoID'];?> hidden>
                                    <input type="text" name="d" value=<?=$fila['codigoID'];?> hidden>
                                    <button class="btn btn-danger" title="eliminar" type="submit"><i
                                            class="fas fa-trash-alt"></i></button>
                                </form>
                            </td>
                            <td class="mx-0 pr-2">
                                <form action="listaReproduccion.php" method="GET">
                                    
                                    <input type="text" name="codigoID" value=<?=$fila['codigoID'];?> hidden>
                                    <input type="text" name="nombre" value='<?=$fila['nombre'];?>' hidden>
                                    <input type="text" name="plataforma" value='<?=$fila['plataforma'];?>' hidden>
                                    <input type="text" name="cantidad_canciones" value=<?=$fila['cantidad_canciones'];?> hidden>

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