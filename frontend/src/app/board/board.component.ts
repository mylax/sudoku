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
  ids: number[];
  val: number[];

  constructor(private httpClient: HttpClient) {
    this.rows = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    this.columns = [1, 2, 3];
    this.ids = [];
    this.val = [];
    this.httpClient.get("http://localhost:6002/get_game_start").subscribe((data)=>{
      for(var i in data){
        this.ids.push(Number(i));
        this.val.push(data[i]);
      }
      console.log(this.ids);
      console.log(this.val);

    });
   }

  find_id(row, column) {
    return column + (row-1) * 9;
  }
  find_val(row, column) {
    var id = this.find_id(row, column);
    var id_of_val = this.ids.indexOf(id);
    if (id_of_val !== -1) {
      return this.val[id_of_val];
    }
    return ""
  }
  ngOnInit() {
  }
}
