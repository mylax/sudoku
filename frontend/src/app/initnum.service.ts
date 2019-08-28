import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class InitnumService {
  constructor(private http: HttpClient) {}
  getHeroes(id: string){
    return this.http.get("http://localhost:6002/get_game_start/" + id)
  }
}
