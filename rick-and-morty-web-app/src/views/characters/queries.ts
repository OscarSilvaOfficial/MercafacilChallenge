export const CHARACTERS = `
query {
  characters(page: 1) {
    info {
      count
    }
    results {
      id,
      name,
      image,
      species,
      location {
        name
      },
      episode {
        name
      }
    }
  }
}
`