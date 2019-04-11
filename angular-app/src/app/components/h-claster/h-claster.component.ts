import {Component, OnInit} from '@angular/core';
import {FileUploader} from 'ng2-file-upload';
import {ApiService} from '../../APIs/api.service';
import * as Highcharts from 'highcharts';
import {animate, style, transition, trigger} from "@angular/animations";
import {Router} from "@angular/router";
import { DomSanitizer } from '@angular/platform-browser';
@Component({
  selector: 'app-h-claster',
  templateUrl: './h-claster.component.html',
  styleUrls: ['./h-claster.component.css'],
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
export class HClasterComponent implements OnInit {
  uploader: FileUploader = new FileUploader(
    {
      url: 'http://127.0.0.1:8000/h_claster_info/', removeAfterUpload: false, autoUpload: true
    }
  );
  visible: boolean;
  visible1: boolean;
  visible2: boolean;
  info: any[];
  Highcharts = Highcharts;
  array: string = "";
  array_reg: string = "";
  updateFlag: boolean;
  points_reg: number[][] = [];
  points: number[][] = [];
  hover1: boolean;
  hover2: boolean;
  optFromInputString: string;
  chartOptions: Highcharts.Options;
  base64Image: string;
  base64Image1: string;
  base64Image2: string;
  image_visible: boolean;

  constructor(private api: ApiService, private router: Router, private sanitizer:DomSanitizer) {
    this.api = api;
    this.visible = false;
  }

  getReg() {
    this.getSomeInfo();
  }

  getSomeInfo() {
    this.api.getHCluster().subscribe(
      (data: any[]) => {
        console.log(data);
        // console.log(JSON.parse(data[0]));
        this.base64Image = "data:image/png;base64, " +  data[0].hierarcial_preview;
        this.base64Image1 = "data:image/png;base64, " +  data[1].hierarcial_dendrogram;
        this.base64Image2 = "data:image/png;base64, " +  data[2].hierarcial_result;
        console.log(this.base64Image);
        this.image_visible = true;
      },
      error => {
        console.log(error);
      }
    );
  }
   transform() {
     return this.sanitizer.bypassSecurityTrustResourceUrl(this.base64Image);
   }
   transform1() {
     return this.sanitizer.bypassSecurityTrustResourceUrl(this.base64Image1);
   }
   transform2() {
     return this.sanitizer.bypassSecurityTrustResourceUrl(this.base64Image2);
   }

  ngOnInit() {
    window.scrollTo(0, 0);
    setTimeout(() => {
      this.visible = true;
      this.visible1 = true;
      this.image_visible = false;
    }, 10);

  }

  changeElement() {
    this.visible1 = !this.visible1;
    this.visible2 = !this.visible2;
  }
}

