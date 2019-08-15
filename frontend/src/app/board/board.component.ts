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
  init: number[];
  val: number[];

  constructor(private httpClient: HttpClient) {
    this.rows = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    this.columns = [1, 2, 3];
   }

  ngOnInit() {
  }

  get_sudoku() {
    this.httpClient.get("http://localhost:6001/create_sudoku").subscribe((data)=>{
      this.init = data["init"];
      this.val = data["val"];
    });
  }
  
  
}
