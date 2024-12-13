function appendToDisplay(value){
    document.getElementById("tela").value += value;
}
function clearDisplay(){
    document.getElementById("tela").value ="";
} 
function calculate(){
    try{
        const result= eval(document.getElementById("tela").value);
        document.getElementById("tela").value = result;
    }catch (erro){
        alert("calcuro errado")
    }
}