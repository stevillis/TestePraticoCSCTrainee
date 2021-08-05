export const CharacterService = {
  get url() {
    const API_KEY = "8d4c7ec2f2107066d1150e1a2e7a3f67",
      ts = "1",
      HASH = "33d9d78cb734071a03fae5392a5ccd4e";

    return `http://gateway.marvel.com/v1/public/characters?apikey=${API_KEY}&ts=${ts}&hash=${HASH}`;
  },
  list: [],
  attributionHTML: "",
  listAll() {
    if (this.list.length) {
      return Promise.resolve(this.list);
    } else {
      return fetch(`${this.url}`)
        .then((response) => response.json())
        .then((response) => {
          this.attributionHTML = response.attributionHTML;
          return response.data.results;
        })
        .then((results) => {
          return results.map((character) => {
            const charObj = {
              name: character.name,
              description:
                character.description.length > 60
                  ? character.description.slice(0, 57) + "..."
                  : character.description,
              modified: new Date(character.modified).toLocaleDateString(),
              thumbnail:
                character.thumbnail.path + "." + character.thumbnail.extension,
            };

            return charObj;
          });
        })
        .then((list) => {
          this.list = list;
          return list;
        });
    }
  },
};
