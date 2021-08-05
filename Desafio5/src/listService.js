export const ListService = {
  createList(characterList) {
    let html = `
      <div class="card-deck">
        <div class="row">
    `;

    for (let i = 0; i < characterList.length; i++) {
      const character = characterList[i];
      html += `
          <div class="col-lg-4 mt-3">
              <div class="card">
                <img class="card-img-top" src="${character.thumbnail}" alt="${character.name}">
                <div class="card-body">
                    <h5 class="card-title">${character.name}</h5>
                    <p class="card-text">${character.description}</p>
                    <p class="card-text"><small class="text-muted">Última atualização ${character.modified}</small></p>
                </div>
              </div>
          </div>`;

      if ((i + 1) % 3 === 0) {
        html += `
          </div>
          <div class="row">
        `;
      }
    }
    html += "</div>";
    return html;
  },
};
