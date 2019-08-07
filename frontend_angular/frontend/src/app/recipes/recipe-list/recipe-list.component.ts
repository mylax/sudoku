import { Component, OnInit } from '@angular/core';

import { Recipe} from '../recipe.model'
@Component({
  selector: 'app-recipe-list',
  templateUrl: './recipe-list.component.html',
  styleUrls: ['./recipe-list.component.css']
})
export class RecipeListComponent implements OnInit {
  recipes: Recipe[] = [
    new Recipe('A test Recipe', 'This is simply a test', 'https://www.wellplated.com/wp-content/uploads/2017/12/Hoppin-John-recipe.jpg'),
    new Recipe('A test Recipe', 'This is simply a test', 'https://www.wellplated.com/wp-content/uploads/2017/12/Hoppin-John-recipe.jpg')
  ];
  constructor() { }

  ngOnInit() {
  }

}
