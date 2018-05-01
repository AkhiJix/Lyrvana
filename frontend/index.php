 <!DOCTYPE html>
  <html>
    <head>
//      <!--Import Google Icon Font-->
//      <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
      <!--Import materialize.css-->
      <link type="text/css" rel="stylesheet" href="css/materialize.min.css"  media="screen,projection"/>
      <!--Import custom styles-->
      <link type="text/css" rel="stylesheet" href="css/styles.css"  media="screen,projection"/>
      <!--Import Montserrat Font-->
      <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet">

      <!--Let browser know website is optimized for mobile-->
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    </head>

    <body style="background-color:rgb(24,24,24)">
        <br/><br/>
        <div class="container">
            <div class="row">
                <div class="col s12 m8 offset-m2 l8 offset-l2">
                    <form id="target" autocomplete="off">
                        <nav class="grey darken-1" style="border-radius:50px">
                            <div class="nav-wrapper">
                                    <div class="input-field">
                                        <input name="search" style="border-radius:50px" id="search" type="search" required>
                                        <label class="label-icon" for="search"><i class="material-icons">search</i></label>
                                        <i class="material-icons">close</i>
                                    </div>
                            </div>
                        </nav>
                        <br/>
                        <div class="center">
                        <label>
                            <input name="cat" type="radio" value="1" checked />
                            <span>Artist</span>
                        </label>
                        <label>
                            <input name="cat" type="radio" value="2" />
                            <span>Song Name</span>
                        </label>
                        <label>
                            <input name="cat" type="radio" value="3" />
                            <span>Lyrics</span>
                        </label>
                        </div>
                    </form>
                </div>
            </div>
            <div class="row" style="color:white;">
                <div class="col s12 m10 offset-m1">
                    <h6 id="sr" style="display:none" class="center">Found <span id="srN"></span> results (<span id="srT"></span> ms) for <span id="srCat"></span> "<span id='srA'></span>"</h6>
                    <ul id="srList">

                    </ul>
                </div>
            </div>
        </div>

      <!--JavaScript at end of body for optimized loading-->
      <script type="text/javascript" src="js/materialize.min.js"></script>
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
      <script src="js/elasticsearch.jquery.min.js"></script>
      <script type="text/javascript" src="js/scripts.js"></script>

    </body>
  </html>