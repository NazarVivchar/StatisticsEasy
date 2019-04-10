import {Component, OnInit} from '@angular/core';
import {FileUploader} from 'ng2-file-upload';
import {ApiService} from '../../APIs/api.service';
import * as Highcharts from 'highcharts';
import {animate, style, transition, trigger} from "@angular/animations";
import {Router} from "@angular/router";

@Component({
  selector: 'app-exp-mov-avg',
  templateUrl: './exp-mov-avg.component.html',
  styleUrls: ['./exp-mov-avg.component.css'],
  animations: [
    trigger(
      'enterAnimationLeft', [
        transition(':enter', [
          style({transform: 'translateX(-100%)', opacity: 0}),
          animate('2s ease-in', style({transform: 'translateX(0)', opacity: 1}))
        ]),
        transition(':leave', [
          style({transform: 'translateX(0)', opacity: 1, position: 'absolute'}),
          animate('1s', style({transform: 'translateX(-100%)', opacity: 0}))
        ])
      ]),
    trigger(
      'enterAnimationRight', [
        transition(':enter', [
          style({transform: 'translateX(100%)', opacity: 0}),
          animate('2s ease-in', style({transform: 'translateX(0)', opacity: 1}))
        ]),
        transition(':leave', [
          style({transform: 'translateX(0)', opacity: 1, position: 'absolute'}),
          animate('1s', style({transform: 'translateX(100%)', opacity: 0}),)
        ])
      ]),
    trigger(
      'enterAnimationTop', [
        transition(':enter', [
          style({transform: 'translateY(-100%)', opacity: 0}),
          animate('2s ease-in-out', style({transform: 'translateY(0)', opacity: 1}))
        ]),
        transition(':leave', [
          style({transform: 'translateY(0)', opacity: 1, position: 'absolute'}),
          animate('1s', style({transform: 'translateY(-100%)', opacity: 0}))
        ])
      ]),
    trigger(
      'enterAnimationBottom', [
        transition(':enter', [
          style({transform: 'translateY(100%)', opacity: 0}),
          animate('2s ease-in-out', style({transform: 'translateY(0)', opacity: 1}))
        ]),
        transition(':leave', [
          style({transform: 'translateY(0)', opacity: 1, position: 'absolute'}),
          animate('1s', style({transform: 'translateY(100%)', opacity: 0}))
        ])
      ])
  ]
})

export class ExpMovAvgComponent implements OnInit {

  uploader: FileUploader = new FileUploader(
    {
      url: 'http://127.0.0.1:8000/exp_ma_info/', removeAfterUpload: false, autoUpload: true
       }
    );
  visible = false;
  visible1 = false;
  visible2 = false;
  hover1: boolean;
  hover2: boolean;
    info:any[];
    Highcharts = Highcharts;
    array: string = "";
    aray_movavg: string = "";
    updateFlag:boolean;
    points_movavg: number[][] = [];
    points: number[][] = [];

    optFromInputString: string;
    chartOptions: Highcharts.Options;
    predict(){
      this.optFromInputString = `
    {
      "title": { "text": "Exponential moving averages" },
      "xAxis": {"min":${this.points[0][0]}},
      "plotOptions": {
              "series": {
                   "marker": {
                      "enabled": false
                }
            }
             },
      "series":[{
        "data": [${this.array.slice(0,-1)}],
        "zones": [{
          "value": 1000,
          "dashStyle": "solid",
          "color": "#919eba"
        }]
  
      },{
        "data": [${this.aray_movavg.slice(0,-1)}],
        "zones": [{
          "value": 1000,
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

  constructor(private api: ApiService, private router: Router) {
    this.api  = api;
   }

   getDnn(){
    this.getSomeInfo();
  }
  getSomeInfo() {
    this.api.getExpMovingAverages().subscribe(
     (data: any[]) => {
           this.info = data;
            console.log(this.info);
            this.updateFlag = false;
            this.points = [];
            this.points_movavg = [];
            this.array = "";
            this.aray_movavg = "";
           let chart_reg_x:number[] = this.info[0].chart_reg_x;
            let  chart_reg_y:number[] = this.info[1].chart_reg_y;
            let chart_x:number[]  = this.info[2].chart_x;
            let chart_y:number[] = this.info[3].chart_y;
            for(let i in chart_x)
            {
              this.points.push([chart_x[i],chart_y[i]]);

            }
       this.points_movavg.push([chart_x[chart_x.length - 1], chart_y[chart_x.length - 1]]);
            for(let i in chart_reg_x)
            {
              this.points_movavg.push([chart_reg_x[i],chart_reg_y[i]]);

            }
            for (let i of this.points_movavg){
              this.aray_movavg += '['+i.join()+'],';
            }
            this.aray_movavg = this.aray_movavg.slice(this.aray_movavg.indexOf(']')+2,this.aray_movavg.length)
            for (let i of this.points){
              this.array += '['+i.join()+'],';
            }

       console.log('This Array');
       console.log(this.array);
       console.log(this.points_movavg[0][0]);
            console.log(this.aray_movavg.slice(0,-1));
            let min =
            this.optFromInputString = `
            {
              "title": { "text": "Exponential moving averages" },
              "xAxis": {"min":${this.points[0][0]}},
              "plotOptions": {
              "series": {
                   "marker": {
                      "enabled": false
                }
            }
             },
              "series": [{
                "data": [${this.array.slice(0,-1)}],
                "zones": [{
                  "value": 1000,
                  "dashStyle": "solid",
                  "color": "#141D2E"
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

  ngOnInit() {
    window.scrollTo(0, 0);
    setTimeout(() => {
      this.visible = true;
      this.visible1 = true;
    }, 10);

  }

  changeElement() {
    this.visible1 = !this.visible1;
    this.visible2 = !this.visible2;
  }
}
