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

const return_menu = () =>{
  location.href = "http://127.0.0.1:8000/#body";

}

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
        console.log("ir a: " + value_touch);
        
      }
    }
    //si los valores en x tiempo no coincide significa que el stado cambió
  }, 3000);
};

addEventListener("mousemove", listening);

//////////////////////////////////////////////////////////////////////

//addEventListener("mousemove", prueba);

//siempre leyendo

/* const activate_modal = (info_modal) => {
  //busca el modal
  const value_to_change = document.querySelector("#value_to_change");
  value_to_change.innerHTML = info_modal;

  //buca la clase con el nombre modal
  const modal = document.querySelector(".modal");

  //activa el modal
  const myModal = new bootstrap.Modal(modal, {});

  myModal.show();
}; */

/* 
const target_tag = document.querySelector("#google");

const search = () => {
  location.href = "http://127.0.0.1:8000/trigger_onclick";
  target_tag.removeEventListener("mousemove", search);
}; */

//addEventListener("mousemove", event_click);

/* const open_web = () => {
  const value_to_change = document.querySelector("#value_to_change");
  value_to_change.innerHTML;
  window.open(value_to_change.innerHTML);
  close_modal();
};

const close_modal = () => {
  const block_event = document.querySelector(".modal-backdrop");
  const modal = document.querySelector(".modal");
  modal.style.display = "none";

  block_event.remove();
}; */

/* 
const target_tag = document.querySelector("#google");

const event_click = (event) => {
  const element_where_am_i = event.target.id;

  setTimeout(() => {
    if (element_where_am_i === "google") {
      location.href = "http://127.0.0.1:8000/trigger_onclick";
      target_tag.removeEventListener("mousemove", event_click);
    }
  }, 3000);
};

addEventListener("mousemove", event_click);
 */
