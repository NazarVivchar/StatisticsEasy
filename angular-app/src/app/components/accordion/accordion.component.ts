import {Component, OnInit} from '@angular/core';
import {animate, state, style, transition, trigger} from "@angular/animations";

@Component({
  selector: 'app-accordion',
  templateUrl: './accordion.component.html',
  styleUrls: ['./accordion.component.css'],
  animations: [
  trigger(
      'enterAnimationTop', [
        state('true', style({transform: 'translateY(0) ', opacity: 1})),
      state('false', style({transform: 'translateY(-300%) ', opacity: 0, display: 'none',})),
      transition('true => false', [style({display: 'none'}), animate('1s ease-in-out')]),
      transition('false => true', [style({
        height: '0',
        display: 'block',
        position: 'absolute'
      }), animate('1s ease-in-out')]),
      ]),
    ]
})
export class AccordionComponent implements OnInit {
private visible = new Array(4).fill(false);
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
