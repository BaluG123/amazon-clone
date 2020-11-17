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
  var h1=document.querySelector('h1')
  h1.style.color=randomcolor()

}
setInterval(change,1000)
