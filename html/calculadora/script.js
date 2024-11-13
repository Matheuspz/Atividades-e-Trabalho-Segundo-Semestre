let valorInicial = "";
let operador = "";
let resultado = "";

function atualizaDisplay(valor) {
    const visor = document.getElementById("visor");
    visor.value = visor.value + valor;
}
function limparVisor() {
    const visor = document.getElementById("visor");
    visor.value = "";
}
function deletar() {
    const visor = document.getElementById("visor");
    visor.value = visor.value.slice(0, -1);
}



function somar() {
    const visor = document.getElementById("visor");
    valorInicial = visor.value;
    operador = "+";
    visor.value = "";
}
function subtrair() {
    const visor = document.getElementById("visor");
    valorInicial = visor.value;
    operador = "-";
    visor.value = "";
}
function multiplicar() {
    const visor = document.getElementById("visor");
    valorInicial = visor.value;
    operador = "*";
    visor.value = "";
}
function dividir() {
    const visor = document.getElementById("visor");
    valorInicial = visor.value;
    operador = "/";
    visor.value = "";
}
function porcentagem() {
    const visor = document.getElementById("visor");
    valorInicial = visor.value;
    visor.value = parseFloat(valorInicial) / 100
}
function alternarSinal() {
    const visor = document.getElementById("visor");
    valorInvert = parseFloat(visor.value);
    visor.value = (-valorInvert).toString();
}



function calcular() {
    const visor = document.getElementById("visor");
    let valorFinal = visor.value;
    switch (operador) {
        case "+":
            resultado = parseFloat(valorInicial) + parseFloat(valorFinal);
            break;
        case "-":
            resultado = parseFloat(valorInicial) - parseFloat(valorFinal);
            break;
        case "*":
            resultado = parseFloat(valorInicial) * parseFloat(valorFinal);
            break;
        case "/":
            resultado = parseFloat(valorInicial) / parseFloat(valorFinal);
            break;
        default:
            return 0;
    }
    visor.value = resultado;
    valorInicial = "";
    operador = "";
}
