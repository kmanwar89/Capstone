<html>
  <head>
    <script src="http://code.jquery.com/jquery-1.9.1.js"> </script>
    <script>
      function chk()
      {
        var fname = document.getElementById('fname').value;
        var lname = document.getElementById('lname').value;
        var dataString = 'fname=' + fname + '$lname' + lname;
        $.ajax((
          type:     "post",
          url:      "test.php"
          data:     dataString,
          cache:    false,
          success:  function(html)(
            $('$mag').html(html);

          )
        ));
        return false;
      }
  </head>

  <body>
    <form>
      <input type="text" id="fname">
      <br/><br/>
      <input type="text" id="lname">
      <input type="submit" value="submit" onclick="return chk()">
    </form>

    <p id="mag"></p>
</body>
</html>
