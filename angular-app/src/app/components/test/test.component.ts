import {Component, OnInit} from '@angular/core';
import {FileUploader} from 'ng2-file-upload';
import {ApiService} from '../../APIs/api.service';

@Component({
  selector: 'app-test',
  templateUrl: './test.component.html',
  styleUrls: ['./test.component.css']
})
export class TestComponent implements OnInit {
  info: any[];
  alpha: number;
  beta: number;
  uploader: FileUploader = new FileUploader(
      { url: 'http://127.0.0.1:8000/regression_info/', removeAfterUpload: false, autoUpload: true
         }
      );
  constructor(private api: ApiService) {
    this.getSomeInfo();
  }
  getSomeInfo() {
     this.api.getDemoRegression().subscribe(
      (data: any[]) => {
            this.info = data;
            console.log(this.info);
            console.log(this.info[0].alpha);
            this.alpha = this.info[0].alpha;
            this.beta = this.info[1].beta;
            console.log(this.beta);
      },
        error => {
        console.log(error);
      }
    );
  }
  ngOnInit() {
  }






}
