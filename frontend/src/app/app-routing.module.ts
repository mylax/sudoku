import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {RouterModule, Routes} from '@angular/router';
import {BoardComponent} from './board/board.component';
import {MenuRightComponent} from './menu-right/menu-right.component';

const routes: Routes = [
  { path: ':id', component: BoardComponent},
  { path: '', redirectTo: '/0', pathMatch: 'full'}
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}