<!DOCTYPE html>
<html lang="en">
<!-- Include headsection and global navigation -->
% include("headdb.tpl")
% include("navleft.tpl")  
    <div class="container-fluid">
        <p>en artikel</p>  
    </div>

<!-- Kommentarsfält -->

        <div class="comments">
                <form method ="post">

                    <label for="title">Namn:</label>
                    <input type="text" id="title">
                    <label for="content">Kommentar:</label>
                    <input type="text" id="content">
                    <input type="submit" value="Submit">
                </form>
                <p>
                    
                </p>
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