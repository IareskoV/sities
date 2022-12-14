import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';

@Component({
  selector: 'app-all-cities',
  templateUrl: './all-cities.component.html',
  styleUrls: ['./all-cities.component.scss']
})
export class AllCitiesComponent implements OnInit {
sities = ['loading']
  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.http.get<string[]>("http://127.0.0.1:5000/all").subscribe(ans=>{
      console.log(ans)
      this.sities = ans
    })
  }

}
