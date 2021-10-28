let tp=0
document.getElementById("sbutton").addEventListener("click",function(){
    tp+=document.getElementById("price").value*document.getElementById("number").value
        document.getElementById("cost").innerHTML=tp
        console.log(tp)
}) 