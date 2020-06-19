function normal(){
    var close = document.getElementById('closebtn');
    close.addEventListener("click", function(){
        document.getElementById('message').style.display="none";
        })
    }

    function closeItSelve() {
        document.getElementById('message').style.display="none";
      }
      setTimeout(closeItSelve, 5000);

normal();