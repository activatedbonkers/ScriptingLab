var x = document.getElementById("myBtn");
    x.addEventListener("mouseover", myMouse1Function);
    x.addEventListener("mouseout", myMouse2Function);
          
    function myMouse1Function()
    {
        document.getElementById("demo").innerHTML += "Moused over!<br>";
    }
          
    function myMouse2Function()
    {
    document.getElementById("demo").innerHTML += "Moused out!<br>";
    }