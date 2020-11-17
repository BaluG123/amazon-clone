var button=document.querySelector('button')
function randomcolor(){
  letters='0123456789ABCDEF'
  color="#"
  for (var i=0;i<6;i++){
    var r=Math.floor(Math.random()*16)
    color=color+letters[r]
  }
  return color
}
function change(){
 var tshirt=document.querySelector('.tshirt')
 tshirt.style.background=randomcolor();
}
setInterval(change,2000)

$('select:nth-of-type(1)').click(function(){
  $('#five').text('price:4$')
})
