


var btn=document.getElementById("mmk");
var bb=document.getElementById("mmk12");
var hh=document.getElementsByClassName("section1");

btn.addEventListener("click",ckick);
bb.classList.remove("mmk1")
function ckick(){

    bb.classList.add("mmk1");
}
document.onclick= function(e)
{
    if(e.target.id !=='mmk')
    {
        bb.classList.remove("mmk1");
    }
}

