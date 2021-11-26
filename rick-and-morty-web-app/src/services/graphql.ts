import axios, { Axios } from 'axios';

export class GraphQLService {

  private http: Axios = axios
  private baseUrl = 'https://rickandmortyapi.com/graphql'
  

  get(query: string): unknown {
    return this.http.post(this.baseUrl, {
      query: query,
    });
  }
}