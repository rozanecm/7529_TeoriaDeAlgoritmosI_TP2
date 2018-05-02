$=jQuery

function hacerControl(){

    let o={}

    o.clickea=function(x,y,ctrl,alt){
        console.log(x,y,ctrl,alt)
    }

    o.grafo={
        vertices:[],
        aristas:[]
    }

    return o;
}

function redibujar(ctx,grafo){
    ctx.clearRect(0,0,800,800);
    

    for(let a of grafo.aristas){
        ctx.beginPath();
        ctx.moveTo(a.x1,a.y1)
        ctx.lineTo(a.x2,a.y2);
        ctx.stroke();
    }

    for(let v of grafo.vertices){
        ctx.moveTo(v.x,v.y)
        ctx.beginPath();
        ctx.arc(v.x,v.y,20,0,2*Math.PI);
        ctx.fill()
    }
}

$(document).ready(function(){
    console.log("hola?")

    var c = document.getElementById("canvas");
    var ctx = c.getContext("2d");

    let control=hacerControl()



    $(canvas).on("click",(e)=>{
        control.clickea(e.offsetX,e.offsetY,e.ctrlKey,e.altKey)
        console.log(e)
        redibujar(ctx,control.grafo)
    })

    

})