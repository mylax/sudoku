import { Component, OnInit} from '@angular/core';
import { InitnumService} from '../initnum.service';
import { ActivatedRoute, Params} from '@angular/router';
import { FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-board',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.css']
})
export class BoardComponent implements OnInit {
  rows: number[];
  columns: number[];
  data: any;
  checkoutForm;
  test: any;

  constructor(
    private initnum: InitnumService,
    private route: ActivatedRoute,
    private formBuilder: FormBuilder) {
    this.rows = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    this.columns = [1, 2, 3];
    this.test = this.create_dict(81);
    this.checkoutForm = this.formBuilder.group(this.test);
   }

  create_dict(n) {
    let result = {};
    for (let i = 1; i <= n; i++) {
      result[i] = ""
    }
    console.log(result);
    return result;
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
  isEnabled(row, column) {
    if(this.find_val(row,  column) === "") {
      return null
    }
    return ''
  }

  ngOnInit() {
    this.route.params.subscribe((params: Params) => {
      this.getHeroes(params["id"]);
    })
  }
  getHeroes(id): void {
    this.initnum.getHeroes(id).subscribe(heroes => this.data = heroes)
  }
  see() {
    console.log(this.data);
  }
  onSubmit(customerData) {
    console.warn("your oder has been submitted", customerData);
  }
}
