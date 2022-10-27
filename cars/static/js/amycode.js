var div = document.getElementById('bg2701')
var images = [
"url('/static/images/bg_1.jpg')",
"url('/static/images/bg_2.jpg')",
"url('/static/images/car-5.jpg')",
"url('/static/images/car-6.jpg')",
"url('/static/images/car-7.jpg')",
"url('/static/images/car-8.jpg')",
"url('/static/images/car-9.jpg')",
"url('/static/images/car-10.jpg')",
]

setInterval( function(){
    var bg = images[Math.floor(Math.random()* images.length)]

    div.style.backgroundImage = bg
}, 1600)