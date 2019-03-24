import { Component, OnInit } from '@angular/core';
import {forEach} from "@angular/router/src/utils/collection";

@Component({
  selector: 'app-accordion',
  templateUrl: './accordion.component.html',
  styleUrls: ['./accordion.component.css']
})
export class AccordionComponent implements OnInit {
private visible = new Array(4).fill(false);;
  constructor() {}

  ngOnInit() {
  }

  changeVisibility(id: number) {
    // this.hover = false;
    const temp = !this.visible[id];
    this.visible = new Array(10).fill(false);
    this.visible[id] = temp;
    console.log(id);
  }


}
