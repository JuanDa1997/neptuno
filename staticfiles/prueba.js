"Use strict";

// window.addEventListener("load", (event) => {
//   location.href = "http://127.0.0.1:8000/#body";
// });

const test = (event) => {
  const get_out = event.id;
  console.log("salio:" + get_out);
  switch (get_out) {
    case "google":
      validate_elemente_where_am_i(true);
      break;
    case "facebook":
      validate_elemente_where_am_i(true);
      break;

    case "youtube":
      validate_elemente_where_am_i(true);
      break;
    case "files":
      validate_elemente_where_am_i(true);
      break;
      
    default:
      break;
  }
};

const validate_elemente_where_am_i = (get_element) => {
  //ingresa a la funcion cada vez que salga de una etiqueta

  const go_to = get_element.id;
  switch (go_to) {
    case "google":
      location.href = "http://127.0.0.1:8000/trigger_onclick";

      break;

    case "youtube":
      location.href = "http://127.0.0.1:8000/view_youtube";

      break;

    case "facebook":
      location.href = "https://www.facebook.com/";

      break;

    case "files":
      location.href = "http://127.0.0.1:8000/view_list";

      break;

    default:
      break;
  }
};
