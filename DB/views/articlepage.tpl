<!DOCTYPE html>
<html lang="en">
<!-- Include headsection and global navigation -->
% include("headdb.tpl")
% include("navleft.tpl")  
    <div class="container-fluid">
        <p>en artikel</p>  
    </div>

<!-- Kommentarsfält -->

    <div class="form-group1">
        <label for="usr">Namn:</label>
        <input type="text" class="form-control1" id="usr">
        <label for="comment">Kommentar:</label>
        <textarea class="form-control2 form-group2" rows="5" id="comment"></textarea>
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