var btn = document.querySelector(".tbtnb");
var rate = document.querySelectorAll(".rate");
var nstar = document.querySelectorAll(".nstar");
var redes = document.querySelectorAll(".redes");
var hotel = document.getElementById("name");
var hotelname = document.getElementById("hotelname").innerHTML;
var n = 0;

$(document).ready(function () {
    $("#class").hide();
    $(".tbtnb").click(function () {
        $("#class").toggle(400);
    });
    $(".tbtnb").mouseenter(function() {
        btn.innerHTML = "<i class='bi bi-door-open-fill'></i>";
    });
    $(".tbtnb").mouseleave(function() {
        btn.innerHTML = "<i class='bi bi-search'></i>";
    });

});
var up=document.getElementById("up");
setInterval(function upf() {
    var uscroll=window.pageYOffset;
    if(uscroll>100){
        up.style.display="block";
    }
    else{
        up.style.display="none";
    }}, 1);


function type()
{
    if(n <= hotelname.length)
    {
        hotel.innerHTML=hotelname.slice(0, n);
        n++;
    }
    else{
        n=1;
    }
}

setInterval(function(){
    type();
}, 250);

for(var i=0; i<rate.length; i++)
{
    if (nstar[i].innerHTML >= 5)
    {
        nstar[i].innerHTML=5;
        for(var z=1; z<=nstar[i].innerHTML; z++)
        {
            rate[i].innerHTML+="<i class='bi bi-star-fill'></i>";
            if(redes[i].innerHTML.length > 30)
            {
                redes[i].innerHTML=redes[i].innerHTML.slice(0,30)+".....";
            }
        }
    }
    if (nstar[i].innerHTML <= 1)
        {
            nstar[i].innerHTML=1;
            for(var z=1; z<=nstar[i].innerHTML; z++)
            {
                rate[i].innerHTML+="<i class='bi bi-star-fill'></i>";
                if(redes[i].innerHTML.length > 30)
                {
                    redes[i].innerHTML=redes[i].innerHTML.slice(0,30)+".....";
                }
            }
        }
    if(nstar[i].innerHTML < 5 && nstar[i].innerHTML > 1)
        {
        nstar[i].innerHTML = nstar[i].innerHTML;
         for(var z=1; z <= nstar[i].innerHTML; z++ )
         {
               rate[i].innerHTML+="<i class='bi bi-star-fill'></i>";
                if(redes[i].innerHTML.length > 30)
                {
                    redes[i].innerHTML=redes[i].innerHTML.slice(0,30)+".....";
                }
         }
         }

}
