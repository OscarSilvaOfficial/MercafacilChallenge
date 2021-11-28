export interface ICharacter {
  id: number | string;
  name: string;
  image: string;
  species: string;
  location: ILocation;
  episode: IEpisede
}

export interface ILocation {
  name: string;
}

export interface IEpisede {
  name: string;
}