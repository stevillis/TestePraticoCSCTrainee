import { CharacterService } from "./marvelAPI";
import { ListService } from "./listService";

let listFilter = "";
const loading = document.querySelector("#loading"),
  inputElement = document.querySelector("#characterFilter"),
  heroList = document.querySelector("#heroList"),
  attribution = document.querySelector("#attribution");

inputElement.addEventListener("keyup", (event) => {
  listFilter = event.target.value;
  setList();
});

function setList() {
  loading.innerHTML = "Carregando...";

  CharacterService.listAll()
    .then(filterList)
    .then(ListService.createList)
    .then((html) => {
      heroList.innerHTML = html;
      attribution.innerHTML = CharacterService.attributionHTML;
      loading.innerHTML = "";
    });
}

function filterList(characterList) {
  return characterList.filter((character) =>
    character.name.includes(listFilter.toLowerCase())
  );
}

setList();
