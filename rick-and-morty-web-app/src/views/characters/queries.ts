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