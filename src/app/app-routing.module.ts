import { Component, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AllCitiesComponent } from './Components/all-cities/all-cities.component';
import { CiteComponent } from './Components/cite/cite.component';
import { CityComponent } from './Components/city/city.component';

const routes: Routes = [
  {
    path : "all",
    component:AllCitiesComponent
  },
  {
    path:":id",
    component:CityComponent,
    },
  {
    path:'site/:id',
    component:CiteComponent
  }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
