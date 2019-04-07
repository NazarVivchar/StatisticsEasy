import {Component, OnInit} from '@angular/core';
import * as Highcharts from 'highcharts';
import {ApiService} from '../../APIs/api.service';

@Component({
  selector: 'app-main-reg-chart',
  templateUrl: './main-reg-chart.component.html',
  styleUrls: ['./main-reg-chart.component.css']
})
export class MainRegChartComponent implements OnInit {
  Highcharts = Highcharts;
  array: string = "";
  array_reg: string = "";
  updateFlag:boolean;
  points_reg: number[][] = [];
  points: number[][] = [];
  info: any[];
  demoSet:number[][] = [];

  optFromInputString: string;
  chartOptions: Highcharts.Options;
  predict(){
    this.optFromInputString = `
  {
    "title": { "text": "Highcharts chart" },
    "xAxis": {"min":${this.points[0][0]}},
    "series":[{
      "data": [${this.array.slice(0,-1)}],
      "zones": [{
        "value": 7.2,
        "dashStyle": "solid",
        "color": "black"
      }]

    },{
      "data": [${this.array_reg.slice(0,-1)}],
      "zones": [{
        "value": 100,
        "dashStyle": "solid",
        "color": "red"
      }]
    }]
  }
  `;
 
    
    this.chartOptions =
         JSON.parse(this.optFromInputString);
     
    
    
    
    this.updateFlag = true;
  }
  getSomeInfo() {
    this.api.getDemoRegression().subscribe(
     (data: any[]) => {
           this.info = data;
           console.log(this.info);
           let chart_reg_x:number[] = this.info[0].chart_reg_x;
            let  chart_reg_y:number[] = this.info[1].chart_reg_y;
            let chart_x:number[]  = this.info[2].chart_x;
            let chart_y:number[] = this.info[3].chart_y;
            for(let i in chart_x)
            {
              this.points.push([chart_x[i],chart_y[i]]);
              
            }
            for(let i in chart_reg_x)
            {
              this.points_reg.push([chart_reg_x[i],chart_reg_y[i]]);
              
            }
            for (let i of this.points_reg){
              this.array_reg += '['+i.join()+'],';
            }
            
            for (let i of this.points){
              this.array += '['+i.join()+'],';
            }
       console.log(this.points_reg[0][0]);
            console.log(this.array_reg.slice(0,-1));
            this.optFromInputString = `
            {
              "title": { "text": "Highcharts chart" },
              "xAxis": {"min":${this.points[0][0]}},
              "series": [{
                "data": [${this.array.slice(0,-1)}],
                "zones": [{
                  "value": 7.2,
                  "dashStyle": "solid",
                  "color": "black"
                }]
              }, {
                "data": []
              }]
            }
            `;
            this.chartOptions = JSON.parse(this.optFromInputString);
     },
       error => {
       console.log(error);
     }
   );
 }
  constructor(private api: ApiService) { 
    this.getSomeInfo();
    
  }

  ngOnInit() {

  }

}
