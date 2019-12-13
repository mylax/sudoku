import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class IdsService {

  constructor(private http2: HttpClient) {}
  getIds() {
    return this.http2.get("http://localhost:6004/get_ids")
  }
}
