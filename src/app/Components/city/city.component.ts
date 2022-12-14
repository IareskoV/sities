import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-city',
  templateUrl: './city.component.html',
  styleUrls: ['./city.component.scss']
})
export class CityComponent implements OnInit {
  routeSub: any;
  sites:sites[]  =[{
    image: 'loading',
    item: 'loading',
    name: 'loading',
    text: 'loading',
  }]

  constructor(private http: HttpClient ,private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.routeSub = this.route.params.subscribe(params => {

      this.http.get<answer>("http://127.0.0.1:5000/city",{params: {name:params['id']}}).subscribe(ans=>{
        console.log(ans.results.bindings)
        if(ans.results.bindings.length){
        let temp = ans.results.bindings.map(item=>{
          return{
            image: item.image.value,
            item: item.item.value.replace('http://dbpedia.org/resource/',''),
            name: item.name.value,
            text: item.text.value
          }
        })
        this.sites = temp
        console.log(temp)
      }
      else{
        this.sites=[{
          image:'',
          item:"",
          text:"",
          name:"Sory we cannot find historical buildings of this place",
        }]
      }

      })
    });

  }

}
type answer = {
  head:any,
  results:{
    bindings:Asites[]
}
}
type Asites ={
  image:{
    value:string
  },
  item:{
    value:string
  },
  name:{
    value:string
  },
  text:{
    value:string
  }
}
type sites = {
  image:string
  item:string
  name:string
  text:string

}
