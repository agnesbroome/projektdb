<!DOCTYPE html>
<html lang="en">
<!-- Include headsection and global navigation -->
% include("headdb.tpl")
% include("navleft.tpl")
    
    <div class="container-fluid">
      %for i in articlelist: 
            <div class="col-xs-6 col-sm-3 placeholder" id="onearticle">
                <h4>{{i["Header"]}}</h4>
                <span class="text-muted">{{i["Ingress"]}}</span>
            </div>
%end
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