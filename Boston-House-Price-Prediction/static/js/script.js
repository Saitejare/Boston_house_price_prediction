function predictPrice(){

const data={

CRIM:document.getElementById("CRIM").value,
ZN:document.getElementById("ZN").value,
INDUS:document.getElementById("INDUS").value,
CHAS:document.getElementById("CHAS").value,
NOX:document.getElementById("NOX").value,
RM:document.getElementById("RM").value,
AGE:document.getElementById("AGE").value,
DIS:document.getElementById("DIS").value,
RAD:document.getElementById("RAD").value,
TAX:document.getElementById("TAX").value,
PTRATIO:document.getElementById("PTRATIO").value,
B:document.getElementById("B").value,
LSTAT:document.getElementById("LSTAT").value

};

fetch("/predict",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify(data)

})

.then(response=>response.json())

.then(result=>{

document.getElementById("price").innerHTML=

"$ "+result.price.toLocaleString();

});

}