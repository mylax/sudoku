import { Component, OnInit} from '@angular/core';
import { InitnumService} from '../initnum.service';
import { ActivatedRoute, Params} from '@angular/router';

@Component({
  selector: 'app-board',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.css']
})
export class BoardComponent implements OnInit {
  rows: number[];
  columns: number[];
  data: any;

  constructor(
    private initnum: InitnumService,
    private route: ActivatedRoute) {
    this.rows = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    this.columns = [1, 2, 3];
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
    this.route.params.subscribe((params: Params) => {
      console.log(params);
      let id2 = +this.route.snapshot.paramMap.get('id')
      this.getHeroes(id2);
    })
  }
  getHeroes(id): void {
    this.initnum.getHeroes(id).subscribe(heroes => this.data = heroes)
  }
  see() {
    console.log(this.data);
  }
}
