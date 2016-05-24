<!DOCTYPE html>
<html lang="en">
<!-- Include headsection and global navigation -->
% include("headdb.tpl")
% include("navleft.tpl")  
    <div class="container-fluid">
        <div class="row">
            <div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
                 
        %for i in sin:
                    <div class="header">
                    <h2> {{i['Header']}} </h2>
                    </div>
                    <div class="Ingress">
                    <p> {{i['Ingress']}} </p>
                    </div>
                    <div class="article_content">
                    <p> {{i['Content']}} </p>
                    </div>    
                    <p>{{i['Article_ID']}}</p>
        %end
            

<!-- Kommentarsfält -->


                <div class="form" id="commenting">
                    <form method ="post" action="/comment_form">
                        <div id="divforname">
                        <label for="name">Namn:</label>
                        <input type="text" id="name" name="name">
                        </div>
                        <div id="divforcomment">
                        <label for="comment">Kommentar:</label>
                        <textarea cols="50" type="text" id="comment" name="comment" ></textarea>
                        </div>
        %for i in sin:
                        <div id="dontchange">
                        <label for="Article_ID" >Ändra ej:</label>
                        <input type="text" name="Article_ID" value="{{i['Article_ID']}}" >
                        </div>
        %end
                        <input type="submit" value="Submit">
                    </form>
               
                </div>
                %for i in getc:
                <div id="actualcomment">
            
                <p id="namecomment">Namn:</p> <p>{{i['name']}} </p>    
                <p id="commentcomment">Kommentar:</p><p> {{i['comment']}}</p>        
            
                </div>
             %end   
            </div>
            </div>

        </div>
    </div>


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')</script>
    <script src="../../dist/js/bootstrap.min.js"></script>
    <!-- Just to make our placeholder images work. Don't actually copy the next line! -->
    <script src="../../assets/js/vendor/holder.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="../../assets/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>