import {Component, OnInit} from '@angular/core';
import * as Highcharts from 'highcharts';
import {ApiService} from '../../APIs/api.service';

@Component({
  selector: 'app-main-dnn-chart',
  templateUrl: './main-dnn-chart.component.html',
  styleUrls: ['./main-dnn-chart.component.css']
})
export class MainDnnChartComponent implements OnInit {
  Highcharts = Highcharts;
  array: string = "";
  array_dnn: string = "";
  updateFlag:boolean;
  points_dnn: number[][] = [];
  points: number[][] = [];
  info: any[];
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
        "value": 100,
        "dashStyle": "solid",
        "color": "black"
      }]

    },{
      "data": [${this.array_dnn.slice(0,-1)}],
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
    this.api.getDemoDnn().subscribe(
     (data: any[]) => {
           this.info = data;
           let chart_dnn_x:number[] = this.info[0].chart_dnn_x;
            let  chart_dnn_y:number[] = this.info[1].chart_dnn_y;
       console.log(chart_dnn_x);
       console.log(chart_dnn_y);
            let chart_x:number[]  = this.info[2].chart_x;
            let chart_y:number[] = this.info[3].chart_y;
            for(let i in chart_x)
            {
              this.points.push([chart_x[i],chart_y[i]]);
              
            }
       this.points_dnn.push([chart_x[chart_x.length - 1], chart_y[chart_x.length - 1]]);
            for(let i in chart_dnn_x)
            {
              this.points_dnn.push([chart_dnn_x[i],chart_dnn_y[i]]);
              
            }
            
            for (let i of this.points_dnn){
              this.array_dnn += '['+i.join()+'],';
            }
            
            for (let i of this.points){
              this.array += '['+i.join()+'],';
            }
       console.log(this.points_dnn[0][0]);
            console.log(this.array_dnn.slice(0,-1));
            this.optFromInputString = `
            {
              "title": { "text": "Highcharts chart" },
              "xAxis": {"min":${this.points[0][0]}},
              "series": [{
                "data": [${this.array.slice(0,-1)}],
                "zones": [{
                  "value": 50,
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
