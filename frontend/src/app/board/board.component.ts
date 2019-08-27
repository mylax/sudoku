import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-board',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.css']
})
export class BoardComponent implements OnInit {
  rows: number[];
  columns: number[];
  data: any;

  constructor(private httpClient: HttpClient) {
    this.rows = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    this.columns = [1, 2, 3];
    this.data = [];
    this.httpClient.get("http://localhost:6002/get_game_start").subscribe((data)=>{
      this.data = data;
      console.log(data);
      });
   }

  find_id(row, column) {
    return column + (row-1) * 9;
  }

  find_val(row, column) {
    let id = this.find_id(row, column);
    let val = this.data[id];
    if (val) { return val};
    return "";
  }
  ngOnInit() {
  }
}
