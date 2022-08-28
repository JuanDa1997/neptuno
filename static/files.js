//NOTAAAA, FUNCIONA PARA LOS ELEMENTOS DENTRO DEL LISTADO,
//SI SE MUEVE A OTRO ELEMENTO DEL DOM
//el addeventlistener externo se activa

let iterator = 0;
let validator = 0;

//evento onmousemove call function en DOM
const prueba = (event) => {
  const trigger = event.innerText;
  if (iterator++) {
    document.getElementById("date-time").value = iterator;
  }
};

const return_menu = () => {
  location.href = "http://54.185.79.64:8000/#body";
};

//valido si el valor númerico del doom, corresponde
//al valor estático que le paso por variable

const state = document.getElementById("date-time");

const listening = (event) => {
  const id_div = event.target.id;
  const state = document.getElementById("date-time").value;
  const not_contains = new RegExp("<head>");
  const value_touch = event.target.innerText;

  const validate_value_touch = value_touch.match(not_contains);

  setTimeout(() => {
    if (state == iterator && value_touch != not_contains) {
      if (id_div >= 0 && id_div != "") {
        const path_file =
          "C:/Users/Juan David Ruiz/OneDrive/Desktop/" + value_touch;

        window.open(path_file);
      }
    }
    //si los valores en x tiempo no coincide significa que el stado cambió
  }, 3000);
};

addEventListener("mousemove", listening);


function readSingleFile(e) {
  var file = e.target.files[0];
  if (!file) {
    return;
  }
  var reader = new FileReader();
  reader.onload = function (e) {
    var contents = e.target.result;
    // Display file content
    displayContents(contents);
  };
  reader.readAsText(file);
}

function displayContents(contents) {
  var element = document.getElementById("file-content");
  element.innerHTML = contents;
}

document.getElementById('file-input').addEventListener('change', readSingleFile, false);
