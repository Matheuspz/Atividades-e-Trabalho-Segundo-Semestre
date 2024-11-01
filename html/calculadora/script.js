function Somar() {
    let x = document.getElementById("num1").value;
    let y = document.getElementById("num2").value;
    console.log(typeof(x))
    console.log(typeof(y))
    const newDiv = document.createElement("div");
    const newP = document.createElement("p");
    newDiv.append(newP)
    document.body.append(newDiv)
    
}