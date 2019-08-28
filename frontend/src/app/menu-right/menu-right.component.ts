import { Component, OnInit } from '@angular/core';
import { IdsService} from '../ids.service';

@Component({
  selector: 'app-menu-right',
  templateUrl: './menu-right.component.html',
  styleUrls: ['./menu-right.component.css']
})
export class MenuRightComponent implements OnInit {
  id_dat: any;

  constructor(private ids: IdsService) {
   }

  ngOnInit() {
    this.getIds2();
  }
  getIds2() {
    this.ids.getIds().subscribe(ids => this.id_dat = ids)
  }
  see() {
    console.log(this.id_dat);
  }
}
