import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-cite',
  templateUrl: './cite.component.html',
  styleUrls: ['./cite.component.scss']
})
export class CiteComponent implements OnInit {
  routeSub: any;
  constructor(private http: HttpClient ,private route: ActivatedRoute) { }
  title = 'loading'
  text = 'loading'
  ngOnInit(): void {
    this.routeSub = this.route.params.subscribe(params => {

      this.http.get<string[]>("http://127.0.0.1:5000/cite",{params: {name:params['id']}}).subscribe(ans=>{

        this.title = ans[0]
        this.text = ans[1]


      })
    });
  }

}
